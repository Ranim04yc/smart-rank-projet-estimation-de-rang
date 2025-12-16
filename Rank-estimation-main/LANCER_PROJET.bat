@echo off
title Estimation de Rang
color 0B

echo.
echo ========================================
echo   LANCEMENT DU PROJET
echo   Republique Tunisienne
echo ========================================
echo.

cd /d "%~dp0"

echo Demarrage en cours...
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe!
    echo Installez Python depuis: https://www.python.org
    pause
    exit /b 1
)

echo Ouverture du navigateur dans 3 secondes...
timeout /t 3 /nobreak >nul
start http://localhost:5000

echo.
echo Serveur demarre sur http://localhost:5000
echo.
echo Appuyez sur Ctrl+C pour arreter
echo.

python app.py

