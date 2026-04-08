#!/usr/bin/env python3
# =============================================================================
# agent_veille.py
# Agent de veille hebdomadaire – Résumé automatique via Claude API
# =============================================================================
# Cet agent interroge Claude pour produire un résumé hebdomadaire structuré
# sur les thématiques de veille : IA éthique & gouvernance des données.
#
# Usage :
#   python3 agent_veille.py                    # Résumé semaine courante
#   python3 agent_veille.py --save             # Sauvegarde dans un fichier .md
#   python3 agent_veille.py --topic "AI Act"   # Résumé sur un topic spécifique
# =============================================================================

import argparse
import json
import os
import sys
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv
load_dotenv()

# ── Configuration ─────────────────────────────────────────────────────────────
ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
MODEL             = "claude-sonnet-4-20250514"
MAX_TOKENS        = 2000

# Thématiques de veille par défaut
THEMATIQUES = [
    "usage éthique de l'IA en entreprise",
    "gouvernance des données et protection de la vie privée",
    "AI Act européen et conformité",
    "recommandations CNIL 2025",
    "biais algorithmiques et IA responsable",
]


def get_semaine_courante() -> str:
    """Retourne la plage de dates de la semaine courante."""
    aujourd_hui  = datetime.now()
    debut_semaine = aujourd_hui - timedelta(days=aujourd_hui.weekday())
    fin_semaine   = debut_semaine + timedelta(days=6)
    return (
        f"{debut_semaine.strftime('%d/%m/%Y')} "
        f"au {fin_semaine.strftime('%d/%m/%Y')}"
    )


def construire_prompt(thematiques: list, semaine: str, topic_custom: str = None) -> str:
    """
    Construit le prompt envoyé à Claude pour générer le résumé de veille.
    """
    if topic_custom:
        sujet = f"le sujet spécifique : **{topic_custom}**"
    else:
        sujet = f"les thématiques suivantes :\n" + "\n".join(
            f"  - {t}" for t in thematiques
        )

    return f"""Tu es un expert en veille technologique spécialisé en Intelligence Artificielle éthique et gouvernance des données.

Ta mission : produire un **résumé de veille hebdomadaire** professionnel et structuré pour la semaine du {semaine}, destiné à des entreprises du mouvement Impact France.

Le résumé doit couvrir {sujet}

## Format attendu (en Markdown)

Produis un document structuré avec exactement ces sections :

### 📰 Résumé de veille – Semaine du {semaine}

#### 🔑 Faits marquants de la semaine
- 3 à 5 actualités clés récentes sur les thématiques
- Pour chaque fait : titre, description courte, pourquoi c'est important

#### 📊 Tendances observées
- 2 à 3 tendances de fond qui se confirment cette semaine

#### ⚖️ Point réglementaire
- Focus sur l'actualité réglementaire (AI Act, RGPD, CNIL)
- Ce que les entreprises doivent surveiller

#### 💡 Recommandation de la semaine
- Une action concrète que les entreprises Impact France peuvent mettre en place immédiatement

#### 🔗 Ressources à ne pas manquer
- 3 ressources (articles, publications, outils) avec liens et description courte

#### 📅 À surveiller la semaine prochaine
- 2 événements ou publications attendus

---

Sois précis, factuel et concis. Utilise des données récentes de 2024-2025.
Adapte le ton pour des dirigeants et équipes data de PME engagées."""


def appeler_claude_api(prompt: str) -> str:
    """
    Appelle l'API Anthropic Claude et retourne le texte généré.
    """
    headers = {
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01",
        "x-api-key": os.getenv("ANTHROPIC_API_KEY"),
    }

    payload = {
        "model":      MODEL,
        "max_tokens": MAX_TOKENS,
        "messages": [
            {
                "role":    "user",
                "content": prompt,
            }
        ],
    }

    try:
        print("🤖 Interrogation de Claude en cours...")
        response = requests.post(
            ANTHROPIC_API_URL,
            headers=headers,
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()

        # Extraction du texte de la réponse
        for block in data.get("content", []):
            if block.get("type") == "text":
                return block["text"]

        return "Erreur : aucun contenu textuel dans la réponse."

    except requests.exceptions.Timeout:
        return "❌ Erreur : timeout lors de l'appel à l'API Claude."
    except requests.exceptions.HTTPError as e:
        return f"❌ Erreur HTTP : {e.response.status_code} – {e.response.text}"
    except Exception as e:
        return f"❌ Erreur inattendue : {str(e)}"


def sauvegarder_resume(contenu: str, semaine: str) -> str:
    """
    Sauvegarde le résumé dans un fichier Markdown daté.
    """
    os.makedirs("resumes_veille", exist_ok=True)

    # Nom de fichier avec date
    date_str  = datetime.now().strftime("%Y-%m-%d")
    nom_fichier = f"resumes_veille/veille_{date_str}.md"

    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"# Résumé de veille – {semaine}\n\n")
        f.write(f"*Généré automatiquement par l'agent de veille FastIA*\n")
        f.write(f"*Date de génération : {datetime.now().strftime('%d/%m/%Y à %H:%M')}*\n\n")
        f.write("---\n\n")
        f.write(contenu)

    return nom_fichier


def afficher_banniere():
    """Affiche la bannière de l'agent."""
    print("\n" + "=" * 60)
    print("  🔍 AGENT DE VEILLE FASTIA")
    print("  IA Éthique & Gouvernance des Données")
    print("=" * 60 + "\n")


def main():
    # ── Parsing des arguments ─────────────────────────────────────────────
    parser = argparse.ArgumentParser(
        description="Agent de veille hebdomadaire IA éthique & gouvernance données"
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Sauvegarde le résumé dans un fichier Markdown"
    )
    parser.add_argument(
        "--topic",
        type=str,
        default=None,
        help="Thématique spécifique à analyser (ex: 'AI Act', 'CNIL 2025')"
    )
    parser.add_argument(
        "--liste-themes",
        action="store_true",
        help="Affiche les thématiques de veille configurées"
    )
    args = parser.parse_args()

    afficher_banniere()

    # ── Affichage des thématiques ─────────────────────────────────────────
    if args.liste_themes:
        print("📋 Thématiques de veille configurées :")
        for i, t in enumerate(THEMATIQUES, 1):
            print(f"  {i}. {t}")
        print()
        return

    # ── Génération du résumé ──────────────────────────────────────────────
    semaine = get_semaine_courante()

    if args.topic:
        print(f"🎯 Topic spécifique : {args.topic}")
    else:
        print(f"📅 Semaine : {semaine}")
        print(f"📌 Thématiques : {len(THEMATIQUES)} sujets de veille\n")

    # Construction du prompt
    prompt = construire_prompt(THEMATIQUES, semaine, args.topic)

    # Appel à l'API Claude
    resume = appeler_claude_api(prompt)

    # Affichage du résumé
    print("\n" + "─" * 60)
    print(resume)
    print("─" * 60 + "\n")

    # Sauvegarde optionnelle
    if args.save:
        fichier = sauvegarder_resume(resume, semaine)
        print(f"✅ Résumé sauvegardé : {fichier}")

    print("✅ Agent de veille terminé !\n")


if __name__ == "__main__":
    main()
