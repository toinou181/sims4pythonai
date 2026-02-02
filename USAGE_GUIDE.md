# Guide d'utilisation - Sims 4 Mod Creator with AI

## Table des matières

1. [Installation rapide](#installation-rapide)
2. [Configuration des clés API](#configuration-des-clés-api)
3. [Utilisation en mode interactif](#utilisation-en-mode-interactif)
4. [Utilisation en ligne de commande](#utilisation-en-ligne-de-commande)
5. [Création d'un exécutable](#création-dun-exécutable)
6. [Exemples concrets](#exemples-concrets)
7. [Résolution de problèmes](#résolution-de-problèmes)

---

## Installation rapide

### Prérequis
- Python 3.8+ installé
- pip (gestionnaire de paquets Python)
- Un compte Google (pour les API)

### Étapes d'installation

```bash
# 1. Cloner le repository
git clone https://github.com/toinou181/sims4pythonai.git
cd sims4pythonai

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Configurer les clés API (voir section suivante)
cp .env.example .env
# Éditez .env avec vos clés
```

---

## Configuration des clés API

### Option 1 : Google AI Studio (Recommandé - Gratuit)

Google AI Studio (Gemini) est la solution la plus simple pour commencer.

**Étapes :**

1. **Obtenir une clé API :**
   - Allez sur https://makersuite.google.com/app/apikey
   - Connectez-vous avec votre compte Google
   - Cliquez sur "Create API Key"
   - Copiez la clé générée

2. **Configurer le fichier .env :**
   ```env
   GOOGLE_API_KEY=votre_cle_api_ici
   ```

3. **C'est tout !** Vous êtes prêt à utiliser l'application.

### Option 2 : Google Vertex AI (Pour les utilisateurs avancés)

Vertex AI offre plus de contrôle mais nécessite un projet Google Cloud.

**Étapes :**

1. **Créer un projet Google Cloud :**
   - Allez sur https://console.cloud.google.com/
   - Créez un nouveau projet
   - Notez l'ID du projet

2. **Activer l'API Vertex AI :**
   - Dans la console Cloud, cherchez "Vertex AI API"
   - Activez l'API pour votre projet

3. **Configurer l'authentification :**
   ```bash
   # Installer gcloud CLI
   # Puis s'authentifier
   gcloud auth application-default login
   ```

4. **Configurer le fichier .env :**
   ```env
   GOOGLE_CLOUD_PROJECT=votre-project-id
   GOOGLE_CLOUD_LOCATION=us-central1
   ```

---

## Utilisation en mode interactif

Le mode interactif est le plus simple pour les débutants.

### Lancer l'application

```bash
python sims4_mod_creator.py
```

### Navigation

1. **Choisir le fournisseur d'IA :**
   ```
   🤖 Choisissez votre fournisseur d'IA:
   1. Google AI Studio (Gemini) - Recommandé
   2. Google Vertex AI
   
   Votre choix (1 ou 2): 1
   ```

2. **Décrire votre mod :**
   ```
   📝 Décrivez le mod que vous souhaitez créer:
   > Un mod qui fait que les Sims gagnent 5000§ en lisant un livre
   ```

3. **Nommer votre mod :**
   ```
   📛 Nom du mod: MoneyFromBooks
   ```

4. **L'IA génère le code :**
   - Le code est généré automatiquement
   - Un package est créé avec le mod et les instructions
   - Les fichiers sont sauvegardés dans `generated_mods/`

5. **Créer d'autres mods ou quitter :**
   - Tapez une nouvelle description pour un autre mod
   - Tapez `quit` pour quitter

---

## Utilisation en ligne de commande

Pour l'automatisation ou les scripts.

### Syntaxe de base

```bash
python sims4_mod_creator.py --description "Description du mod" --name "NomDuMod"
```

### Options disponibles

| Option | Raccourci | Description | Défaut |
|--------|-----------|-------------|--------|
| `--description` | `-d` | Description du mod (requis) | - |
| `--name` | `-n` | Nom du mod | `custom_mod` |
| `--provider` | `-p` | Fournisseur d'IA (`gemini` ou `vertex`) | `gemini` |
| `--help` | `-h` | Afficher l'aide | - |

### Exemples de commandes

```bash
# Exemple simple avec Gemini
python sims4_mod_creator.py -d "Mod qui augmente la vitesse d'apprentissage" -n "FastLearner"

# Exemple avec Vertex AI
python sims4_mod_creator.py \
  -d "Mod qui ajoute une nouvelle carrière de développeur" \
  -n "DevCareer" \
  -p vertex

# Mod pour gagner de l'argent
python sims4_mod_creator.py \
  --description "Les Sims gagnent 10000§ en dormant" \
  --name "DreamMoney"
```

---

## Création d'un exécutable

Pour distribuer l'application sans nécessiter Python.

### Windows

```cmd
REM Méthode 1 : Script automatique
build.bat

REM Méthode 2 : Commande directe
pip install pyinstaller
pyinstaller sims4_mod_creator.spec
```

### Linux / Mac

```bash
# Méthode 1 : Script automatique
./build.sh

# Méthode 2 : Commande directe
pip install pyinstaller
pyinstaller sims4_mod_creator.spec
```

### Résultat

L'exécutable sera créé dans `dist/` :
- **Windows** : `dist/Sims4ModCreator.exe`
- **Linux/Mac** : `dist/Sims4ModCreator`

### Utilisation de l'exécutable

```bash
# Windows
dist\Sims4ModCreator.exe --help
dist\Sims4ModCreator.exe -d "Description du mod" -n "NomMod"

# Linux/Mac
./dist/Sims4ModCreator --help
./dist/Sims4ModCreator -d "Description du mod" -n "NomMod"
```

⚠️ **Important** : Le fichier `.env` doit être dans le même dossier que l'exécutable !

---

## Exemples concrets

### Exemple 1 : Mod d'argent simple

**Description :** "Un mod qui donne 50000§ quand un Sim regarde la télévision"

**Commande :**
```bash
python sims4_mod_creator.py -d "Donne 50000§ quand un Sim regarde la TV" -n "TVMoney"
```

**Résultat :** Un fichier Python sera créé dans `generated_mods/tvmoney/`

### Exemple 2 : Mod de compétences

**Description :** "Les compétences s'apprennent 10 fois plus vite"

**Commande :**
```bash
python sims4_mod_creator.py -d "Les compétences s'apprennent 10 fois plus vite" -n "SuperSkills"
```

### Exemple 3 : Mod social

**Description :** "Ajoute une interaction 'Super câlin' qui met les deux Sims de très bonne humeur"

**Commande :**
```bash
python sims4_mod_creator.py \
  -d "Ajoute une interaction 'Super câlin' qui rend heureux" \
  -n "SuperHug"
```

### Exemple 4 : Mod de carrière

**Description :** "Triple le salaire de toutes les carrières"

**Commande :**
```bash
python sims4_mod_creator.py -d "Triple le salaire de toutes les carrières" -n "SalaryBoost"
```

---

## Résolution de problèmes

### Problème : "GOOGLE_API_KEY non définie"

**Cause :** Le fichier `.env` n'existe pas ou est vide.

**Solution :**
1. Copiez `.env.example` vers `.env`
2. Ajoutez votre clé API Google AI Studio
3. Vérifiez qu'il n'y a pas d'espaces avant/après la clé

### Problème : "ModuleNotFoundError: No module named 'X'"

**Cause :** Les dépendances ne sont pas installées.

**Solution :**
```bash
pip install -r requirements.txt
```

### Problème : "Failed to generate content"

**Cause :** Clé API invalide ou quota dépassé.

**Solution :**
1. Vérifiez que votre clé API est correcte
2. Vérifiez que vous n'avez pas dépassé le quota gratuit
3. Essayez avec une nouvelle clé API

### Problème : L'exécutable ne démarre pas

**Cause :** Fichier `.env` manquant ou antivirus bloquant.

**Solution :**
1. Assurez-vous que `.env` est dans le même dossier que l'exe
2. Ajoutez une exception dans votre antivirus pour l'exécutable
3. Lancez l'exécutable depuis un terminal pour voir les erreurs

### Problème : Le mod généré ne fonctionne pas dans le jeu

**Cause :** Les mods générés par IA peuvent nécessiter des ajustements.

**Solution :**
1. Vérifiez que les mods sont activés dans le jeu
2. Vérifiez que les scripts sont autorisés
3. Le code généré peut nécessiter des modifications manuelles
4. Consultez la documentation de modding Sims 4 pour ajuster le code

---

## Conseils d'utilisation

### Pour de meilleurs résultats

1. **Soyez précis dans vos descriptions :**
   - ❌ "Mod d'argent"
   - ✅ "Mod qui donne 10000§ quand le Sim cuisine"

2. **Mentionnez le contexte :**
   - ❌ "Plus rapide"
   - ✅ "Les Sims courent 2 fois plus vite"

3. **Spécifiez les valeurs :**
   - ❌ "Beaucoup d'argent"
   - ✅ "50000 simflouz"

### Limites de l'IA

- Les mods générés sont des **points de départ**
- Ils peuvent nécessiter des **ajustements manuels**
- Testez toujours dans une **sauvegarde de test**
- Vérifiez la **compatibilité** avec votre version du jeu

---

## Ressources utiles

- **Documentation Sims 4 Modding :** https://sims4studio.com/
- **Google AI Studio :** https://makersuite.google.com/
- **Google Vertex AI :** https://cloud.google.com/vertex-ai
- **PyInstaller :** https://pyinstaller.org/

---

**Bon modding ! 🎮**
