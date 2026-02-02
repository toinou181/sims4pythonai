"""
Sims 4 Mod Creator with AI
Créateur de mods pour Les Sims 4 utilisant l'IA (Google AI Studio et Vertex AI)
"""

import os
import sys
import json
from pathlib import Path
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()


class AIProvider:
    """Classe de base pour les fournisseurs d'IA"""
    
    def generate_code(self, prompt: str) -> str:
        """Génère du code Python pour un mod Sims 4"""
        raise NotImplementedError


class GoogleAIStudioProvider(AIProvider):
    """Fournisseur utilisant Google AI Studio (Gemini)"""
    
    def __init__(self, api_key: Optional[str] = None):
        import google.generativeai as genai
        
        self.api_key = api_key or os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY non définie. Veuillez configurer le fichier .env")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_code(self, prompt: str) -> str:
        """Génère du code Python pour un mod Sims 4 avec Gemini"""
        full_prompt = f"""Tu es un expert en création de mods pour Les Sims 4.
Génère un code Python complet et fonctionnel pour un mod basé sur cette demande:

{prompt}

Le code doit:
- Être compatible avec Les Sims 4
- Utiliser les bonnes importations de la bibliothèque de modding Sims 4
- Inclure des commentaires en français
- Être prêt à être utilisé directement

Code Python:"""
        
        response = self.model.generate_content(full_prompt)
        return response.text


class VertexAIProvider(AIProvider):
    """Fournisseur utilisant Google Vertex AI"""
    
    def __init__(self, project_id: Optional[str] = None, location: Optional[str] = None):
        from google.cloud import aiplatform
        
        self.project_id = project_id or os.getenv('GOOGLE_CLOUD_PROJECT')
        self.location = location or os.getenv('GOOGLE_CLOUD_LOCATION', 'us-central1')
        
        if not self.project_id:
            raise ValueError("GOOGLE_CLOUD_PROJECT non défini. Veuillez configurer le fichier .env")
        
        aiplatform.init(project=self.project_id, location=self.location)
        
        # Importer après l'initialisation
        from vertexai.preview.generative_models import GenerativeModel
        self.model = GenerativeModel("gemini-pro")
    
    def generate_code(self, prompt: str) -> str:
        """Génère du code Python pour un mod Sims 4 avec Vertex AI"""
        full_prompt = f"""Tu es un expert en création de mods pour Les Sims 4.
Génère un code Python complet et fonctionnel pour un mod basé sur cette demande:

{prompt}

Le code doit:
- Être compatible avec Les Sims 4
- Utiliser les bonnes importations de la bibliothèque de modding Sims 4
- Inclure des commentaires en français
- Être prêt à être utilisé directement

Code Python:"""
        
        response = self.model.generate_content(full_prompt)
        return response.text


class Sims4ModCreator:
    """Créateur de mods pour Les Sims 4 avec IA"""
    
    def __init__(self, ai_provider: str = "gemini"):
        """
        Initialise le créateur de mods
        
        Args:
            ai_provider: "gemini" pour Google AI Studio ou "vertex" pour Vertex AI
        """
        self.ai_provider_name = ai_provider
        self.output_dir = Path("generated_mods")
        self.output_dir.mkdir(exist_ok=True)
        
        # Initialiser le fournisseur d'IA
        if ai_provider == "gemini":
            self.ai_provider = GoogleAIStudioProvider()
        elif ai_provider == "vertex":
            self.ai_provider = VertexAIProvider()
        else:
            raise ValueError(f"Fournisseur d'IA non supporté: {ai_provider}")
    
    def create_mod(self, description: str, mod_name: str) -> Path:
        """
        Crée un mod Sims 4 basé sur une description
        
        Args:
            description: Description du mod à créer
            mod_name: Nom du mod
            
        Returns:
            Chemin vers le fichier du mod créé
        """
        print(f"\n🎮 Création du mod '{mod_name}'...")
        print(f"📝 Description: {description}")
        print(f"🤖 Utilisation de: {self.ai_provider_name}")
        
        # Générer le code avec l'IA
        print("\n⏳ Génération du code avec l'IA...")
        try:
            generated_code = self.ai_provider.generate_code(description)
        except Exception as e:
            print(f"\n❌ Erreur lors de la génération: {e}")
            raise
        
        # Nettoyer le code (enlever les balises markdown si présentes)
        code = self._clean_code(generated_code)
        
        # Sauvegarder le mod
        mod_filename = f"{mod_name.replace(' ', '_').lower()}.py"
        mod_path = self.output_dir / mod_filename
        
        with open(mod_path, 'w', encoding='utf-8') as f:
            f.write(code)
        
        print(f"\n✅ Mod créé avec succès: {mod_path}")
        return mod_path
    
    def _clean_code(self, code: str) -> str:
        """Nettoie le code généré (enlève les balises markdown)"""
        lines = code.split('\n')
        cleaned_lines = []
        in_code_block = False
        
        for line in lines:
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
            # Only include lines that are not code fence markers
            cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def create_mod_package(self, mod_path: Path) -> Path:
        """
        Crée un package de mod prêt à être installé dans Les Sims 4
        
        Args:
            mod_path: Chemin vers le fichier Python du mod
            
        Returns:
            Chemin vers le package créé
        """
        print(f"\n📦 Création du package pour {mod_path.name}...")
        
        # Créer un dossier pour le package
        package_name = mod_path.stem
        package_dir = self.output_dir / package_name
        package_dir.mkdir(exist_ok=True)
        
        # Copier le fichier Python
        import shutil
        shutil.copy(mod_path, package_dir / mod_path.name)
        
        # Créer un fichier README
        readme_path = package_dir / "README.txt"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(f"""MOD POUR LES SIMS 4: {package_name}
            
Généré automatiquement avec Sims4PythonAI

INSTALLATION:
1. Copiez le fichier .py dans votre dossier Mods des Sims 4
   (Documents/Electronic Arts/The Sims 4/Mods/)
2. Activez les mods et scripts dans les paramètres du jeu
3. Redémarrez le jeu

ATTENTION:
- Testez toujours les mods dans un jeu de sauvegarde séparé
- Vérifiez la compatibilité avec votre version du jeu
- Faites des sauvegardes régulières
""")
        
        print(f"✅ Package créé: {package_dir}")
        return package_dir


def print_banner():
    """Affiche la bannière du programme"""
    banner = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     🎮 SIMS 4 MOD CREATOR WITH AI 🤖                     ║
║                                                           ║
║     Créez des mods pour Les Sims 4 avec l'IA            ║
║     Powered by Google AI Studio & Vertex AI              ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""
    print(banner)


def interactive_mode():
    """Mode interactif pour créer des mods"""
    print_banner()
    
    # Choisir le fournisseur d'IA
    print("\n🤖 Choisissez votre fournisseur d'IA:")
    print("1. Google AI Studio (Gemini) - Recommandé")
    print("2. Google Vertex AI")
    
    choice = input("\nVotre choix (1 ou 2): ").strip()
    
    if choice == "1":
        ai_provider = "gemini"
    elif choice == "2":
        ai_provider = "vertex"
    else:
        print("❌ Choix invalide. Utilisation de Gemini par défaut.")
        ai_provider = "gemini"
    
    try:
        creator = Sims4ModCreator(ai_provider=ai_provider)
    except Exception as e:
        print(f"\n❌ Erreur lors de l'initialisation: {e}")
        print("\n💡 Assurez-vous d'avoir configuré le fichier .env avec vos clés API")
        return
    
    while True:
        print("\n" + "="*60)
        print("\n📝 Décrivez le mod que vous souhaitez créer")
        print("(ou tapez 'quit' pour quitter):\n")
        
        description = input("> ").strip()
        
        if description.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Au revoir!")
            break
        
        if not description:
            print("❌ Description vide. Veuillez réessayer.")
            continue
        
        mod_name = input("\n📛 Nom du mod: ").strip()
        if not mod_name:
            mod_name = "custom_mod"
        
        try:
            # Créer le mod
            mod_path = creator.create_mod(description, mod_name)
            
            # Créer le package
            package_path = creator.create_mod_package(mod_path)
            
            print("\n" + "="*60)
            print("\n🎉 Mod créé avec succès!")
            print(f"\n📁 Fichiers disponibles dans: {creator.output_dir}")
            
        except Exception as e:
            print(f"\n❌ Erreur: {e}")
            print("Veuillez réessayer avec une description différente.")


def main():
    """Point d'entrée principal"""
    if len(sys.argv) > 1:
        # Mode ligne de commande
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print_banner()
            print("""
UTILISATION:

Mode interactif:
    python sims4_mod_creator.py

Mode ligne de commande:
    python sims4_mod_creator.py --description "Description du mod" --name "Nom du mod" [--provider gemini|vertex]

Options:
    --description, -d   Description du mod à créer
    --name, -n          Nom du mod
    --provider, -p      Fournisseur d'IA (gemini ou vertex, défaut: gemini)
    --help, -h          Affiche cette aide

Exemples:
    python sims4_mod_creator.py -d "Un mod qui ajoute des interactions sociales amusantes" -n "FunSocial"
    python sims4_mod_creator.py -d "Un mod pour gagner plus d'argent" -n "MoneyBoost" -p vertex
""")
            return
        
        # Parser les arguments
        args = {}
        i = 1
        while i < len(sys.argv):
            if sys.argv[i] in ['--description', '-d']:
                args['description'] = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] in ['--name', '-n']:
                args['name'] = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] in ['--provider', '-p']:
                args['provider'] = sys.argv[i + 1]
                i += 2
            else:
                i += 1
        
        if 'description' not in args:
            print("❌ Erreur: --description est requis")
            print("Utilisez --help pour voir l'aide")
            return
        
        print_banner()
        
        provider = args.get('provider', 'gemini')
        name = args.get('name', 'custom_mod')
        
        try:
            creator = Sims4ModCreator(ai_provider=provider)
            mod_path = creator.create_mod(args['description'], name)
            package_path = creator.create_mod_package(mod_path)
            
            print("\n🎉 Mod créé avec succès!")
            print(f"📁 Fichiers disponibles dans: {creator.output_dir}")
        except Exception as e:
            print(f"\n❌ Erreur: {e}")
            sys.exit(1)
    else:
        # Mode interactif par défaut
        interactive_mode()


if __name__ == "__main__":
    main()
