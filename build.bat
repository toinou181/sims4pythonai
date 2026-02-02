@echo off
REM Script de construction pour créer l'exécutable avec PyInstaller (Windows)

echo 🚀 Construction de l'exécutable Sims4ModCreator...
echo.

REM Vérifier que PyInstaller est installé
where pyinstaller >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ PyInstaller n'est pas installé
    echo Installation en cours...
    pip install pyinstaller
)

REM Nettoyer les anciens builds
echo 🧹 Nettoyage des anciens builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM Construire l'exécutable
echo ⚙️  Construction de l'exécutable...
pyinstaller sims4_mod_creator.spec

REM Vérifier le succès
if exist "dist\Sims4ModCreator.exe" (
    echo.
    echo ✅ Exécutable créé avec succès!
    echo 📁 L'exécutable se trouve dans le dossier 'dist\'
    echo.
    echo Pour l'utiliser:
    echo   dist\Sims4ModCreator.exe
) else (
    echo.
    echo ❌ Erreur lors de la création de l'exécutable
    echo Vérifiez les logs ci-dessus pour plus de détails
    exit /b 1
)
