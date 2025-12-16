@echo off
title Estimation de Rang - Serveur Web
color 0A

echo.
echo ========================================
echo   Estimation de Rang - Demarrage
echo   Republique Tunisienne
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] Verification de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [ERREUR] Python n'est pas installe!
    echo.
    echo Installez Python depuis: https://www.python.org
    echo.
    pause
    exit /b 1
)
python --version
echo [OK] Python detecte
echo.

echo [2/3] Demarrage du serveur web...
echo.
echo ========================================
echo   Le serveur sera accessible sur:
echo   http://localhost:5000
echo ========================================
echo.
echo Le navigateur va s'ouvrir automatiquement...
echo.
echo Appuyez sur Ctrl+C pour arreter le serveur
echo.

timeout /t 2 /nobreak >nul
start http://localhost:5000

python app.py

pause
