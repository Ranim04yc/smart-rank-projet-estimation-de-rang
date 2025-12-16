@echo off
echo ========================================
echo Lancement du Bot Telegram
echo ========================================
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe ou pas dans le PATH
    pause
    exit /b 1
)

REM Lancer le script Python
python run_bot.py

pause


