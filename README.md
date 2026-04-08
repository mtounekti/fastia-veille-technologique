# 🔍 Veille Technologique – IA Éthique & Gouvernance des Données
### Mission Impact France | FastIA 2025

---

## 📋 Description

Ce dépôt contient le travail de veille technologique réalisé dans le cadre du **Brief M0 – Rituel de Veille** chez FastIA.

Un client du mouvement **Impact France** nous a confié une mission de veille sur deux thématiques prioritaires :
- 🤖 **Usage éthique de l'IA** au sein des entreprises
- 🔒 **Gouvernance des données** et protection de la vie privée

---

## 📁 Structure du dépôt

```
fastia-veille-technologique/
├── veille.md             # Document de veille complet livré au client
├── agent_veille.py       # Agent Python – résumés hebdomadaires automatiques
├── requirements.txt      # Dépendances Python
├── .gitignore            # Fichiers exclus (dont .env)
└── resumes_veille/       # Dossier de sauvegarde des résumés générés
    └── .gitkeep
```

---

## 🛠️ Rituel de veille mis en place

| Outil | Usage | Fréquence |
|---|---|---|
| 📱 **Pocket** | Sauvegarde & organisation des articles par tags | Quotidien |
| 📬 **Substack** | Newsletters spécialisées IA & données | Quotidien |
| 🔔 **Google Alerts** | Alertes sur mots-clés prioritaires | Automatique |
| 🤖 **Agent Claude API** | Résumés hebdomadaires automatisés | Hebdomadaire |

**Tags Pocket utilisés :**
`#ethique-ia` · `#rgpd` · `#ai-act` · `#gouvernance-data` · `#cnil`

**Newsletters suivies :**
- *The Algorithmic Bridge* – IA & Société
- *Import AI* – Recherche IA (Jack Clark)
- *AI Snake Oil* – Critique & fact-checking IA

---

## 📄 Document de veille (`veille.md`)

Le fichier `veille.md` est le **livrable principal** remis au client Impact France. Il couvre :

1. Contexte et objectifs de la mission
2. Rituel de veille mis en place
3. Axe 1 – Usage éthique de l'IA en entreprise
4. Axe 2 – Gouvernance des données & vie privée
5. Axe 3 – Réglementation : AI Act & RGPD 2025
6. Synthèse et recommandations
7. Sources et ressources

---

## 🤖 Agent de veille automatisé (`agent_veille.py`)

Script Python qui interroge l'**API Claude (Anthropic)** pour générer automatiquement un résumé de veille hebdomadaire structuré.

### Installation

```bash
# Cloner le repo
git clone https://github.com/mtounekti/fastia-veille-technologique.git
cd fastia-veille-technologique

# Créer un environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### Configuration

Crée un fichier `.env` à la racine du projet :

```bash
ANTHROPIC_API_KEY=sk-ant-ton-api-key-ici
```

> ⚠️ Ne jamais commiter le fichier `.env` — il est dans le `.gitignore`

### Utilisation

```bash
# Résumé de la semaine courante
python3 agent_veille.py

# Résumé sur un topic spécifique
python3 agent_veille.py --topic "AI Act 2025"

# Résumé + sauvegarde automatique en Markdown
python3 agent_veille.py --save

# Voir les thématiques configurées
python3 agent_veille.py --liste-themes
```

### Exemple de sortie

```
============================================================
  🔍 AGENT DE VEILLE FASTIA
  IA Éthique & Gouvernance des Données
============================================================

📅 Semaine : 06/04/2026 au 12/04/2026
📌 Thématiques : 5 sujets de veille

🤖 Interrogation de Claude en cours...

# 📰 Résumé de veille – Semaine du 06/04/2026 au 12/04/2026
## 🔑 Faits marquants de la semaine
...
```

---

## 🔗 Sources principales

- 🏛️ [CNIL – Recommandations IA & RGPD 2025](https://www.cnil.fr/fr/ia-et-rgpd-la-cnil-publie-ses-nouvelles-recommandations)
- 🇪🇺 [Parlement européen – AI Act](https://www.europarl.europa.eu/news/fr/press-room/20240307IPR20524)
- 📊 [BPI France – IA éthique et inclusive](https://bigmedia.bpifrance.fr/nos-dossiers/ia-ethique-et-inclusive-quels-enjeux-et-defis-pour-les-entreprises)
- 📖 [arXiv – Publications IA éthique](https://arxiv.org/search/?searchtype=all&query=AI+ethics+governance)

---

*Brief M0 – Rituel de Veille Technologique | FastIA 2025*