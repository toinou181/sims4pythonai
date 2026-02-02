"""
Script de démonstration du Sims 4 Mod Creator
Ce script montre comment utiliser le créateur de mods sans avoir besoin de clés API réelles
"""

import os
import sys
from pathlib import Path

# Ajouter le répertoire parent au path pour pouvoir importer sims4_mod_creator
sys.path.insert(0, str(Path(__file__).parent))

# Créer une classe de test qui simule un fournisseur d'IA
class MockAIProvider:
    """Fournisseur d'IA fictif pour la démonstration"""
    
    def generate_code(self, prompt: str) -> str:
        """Génère un exemple de code pour démonstration"""
        return f'''# Mod généré pour: {prompt}
import services
import sims4

# Ce mod a été généré automatiquement par Sims4PythonAI
# Description: {prompt}

class CustomMod:
    """Exemple de mod pour Les Sims 4"""
    
    def __init__(self):
        print("Mod initialisé!")
    
    def apply_modifications(self):
        """Applique les modifications du mod"""
        # Votre code de mod ici
        print("Modifications appliquées!")

# Initialiser le mod quand le jeu charge
mod_instance = CustomMod()
mod_instance.apply_modifications()
'''


def demo_without_api():
    """Démontre le fonctionnement sans clés API réelles"""
    print("="*70)
    print("DÉMONSTRATION DU SIMS 4 MOD CREATOR")
    print("="*70)
    print()
    print("Cette démonstration montre le fonctionnement du créateur de mods")
    print("sans nécessiter de clés API Google.")
    print()
    
    # Importer la classe Sims4ModCreator
    from sims4_mod_creator import Sims4ModCreator
    
    # Créer une instance avec un mock provider
    creator = Sims4ModCreator.__new__(Sims4ModCreator)
    creator.ai_provider_name = "demo"
    creator.output_dir = Path("generated_mods")
    creator.output_dir.mkdir(exist_ok=True)
    creator.ai_provider = MockAIProvider()
    
    # Créer un mod de démonstration
    description = "Un mod qui améliore les interactions sociales entre Sims"
    mod_name = "SocialBoost_Demo"
    
    print(f"📝 Création d'un mod de démonstration:")
    print(f"   Nom: {mod_name}")
    print(f"   Description: {description}")
    print()
    
    try:
        mod_path = creator.create_mod(description, mod_name)
        package_path = creator.create_mod_package(mod_path)
        
        print()
        print("="*70)
        print("✅ SUCCÈS!")
        print("="*70)
        print()
        print(f"Fichier du mod: {mod_path}")
        print(f"Package créé: {package_path}")
        print()
        print("Vous pouvez examiner les fichiers créés dans le dossier 'generated_mods/'")
        
        # Afficher un aperçu du code généré
        print()
        print("="*70)
        print("APERÇU DU CODE GÉNÉRÉ:")
        print("="*70)
        with open(mod_path, 'r', encoding='utf-8') as f:
            print(f.read())
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()


def demo_structure():
    """Affiche la structure du projet"""
    print()
    print("="*70)
    print("STRUCTURE DU PROJET")
    print("="*70)
    print()
    print("""
sims4pythonai/
│
├── sims4_mod_creator.py      # ⭐ Application principale
│   ├── AIProvider             # Classe de base pour les fournisseurs d'IA
│   ├── GoogleAIStudioProvider # Intégration Google AI Studio (Gemini)
│   ├── VertexAIProvider       # Intégration Google Vertex AI
│   └── Sims4ModCreator        # Créateur de mods principal
│
├── requirements.txt           # Dépendances Python
├── .env.example              # Exemple de configuration
├── .gitignore               # Fichiers à ignorer
│
├── sims4_mod_creator.spec    # Configuration PyInstaller
├── build.sh                  # Script de build (Linux/Mac)
├── build.bat                 # Script de build (Windows)
│
├── README.md                 # Documentation complète
└── demo.py                   # ⭐ Ce fichier de démonstration

Après génération:
└── generated_mods/           # Mods générés
    └── [nom_du_mod]/
        ├── [nom_du_mod].py   # Code du mod
        └── README.txt        # Instructions d'installation
""")


if __name__ == "__main__":
    print()
    print("🎮 Sims 4 Mod Creator - Démonstration")
    print()
    
    # Afficher la structure
    demo_structure()
    
    # Lancer la démo
    print()
    input("Appuyez sur Entrée pour lancer la démonstration...")
    print()
    
    demo_without_api()
    
    print()
    print("="*70)
    print("Pour utiliser le créateur avec de vraies clés API:")
    print("="*70)
    print()
    print("1. Copiez .env.example vers .env")
    print("2. Ajoutez votre clé API Google AI Studio")
    print("3. Lancez: python sims4_mod_creator.py")
    print()
    print("Consultez le README.md pour plus d'informations!")
    print()
