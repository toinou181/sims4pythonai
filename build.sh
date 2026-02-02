#!/bin/bash
# Script de construction pour créer l'exécutable avec PyInstaller

echo "🚀 Construction de l'exécutable Sims4ModCreator..."
echo ""

# Vérifier que PyInstaller est installé
if ! command -v pyinstaller &> /dev/null; then
    echo "❌ PyInstaller n'est pas installé"
    echo "Installation en cours..."
    pip install pyinstaller
fi

# Nettoyer les anciens builds
echo "🧹 Nettoyage des anciens builds..."
rm -rf build/ dist/

# Construire l'exécutable
echo "⚙️  Construction de l'exécutable..."
pyinstaller sims4_mod_creator.spec

# Vérifier le succès
if [ -f "dist/Sims4ModCreator" ] || [ -f "dist/Sims4ModCreator.exe" ]; then
    echo ""
    echo "✅ Exécutable créé avec succès!"
    echo "📁 L'exécutable se trouve dans le dossier 'dist/'"
    echo ""
    echo "Pour l'utiliser:"
    if [ -f "dist/Sims4ModCreator.exe" ]; then
        echo "  dist\\Sims4ModCreator.exe"
    else
        echo "  ./dist/Sims4ModCreator"
    fi
else
    echo ""
    echo "❌ Erreur lors de la création de l'exécutable"
    echo "Vérifiez les logs ci-dessus pour plus de détails"
    exit 1
fi
