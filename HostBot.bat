@echo off
chcp 65001 >nul 2>&1
title HostBot
color 0D
cls
setlocal enabledelayedexpansion

echo.
echo                                                    QU4N.TH3.D3V
echo   =========================================
echo    V   V  V   V  VVVVV  V   V
echo    V   V  V   V  V      V  V
echo    V   V  V   V  V      V V
echo     V V   V   V  V      VV
echo      V    VVVVV  VVVVV  V   V
echo   =========================================
echo.
echo   HostBot v6.4 - Discord Self-Bot
echo   ========================================
echo.

where python >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python not found!
    pause
    exit /b 1
)

for /f "tokens=*" %%A in ('python --version 2^>^&1') do echo  [OK] %%A
echo.

if not exist "config.json" (
    echo  Config not found. Creating...
    echo.
    set /p "TK=  Discord Token: "
    echo {"token":"!TK!","prefix":"."} > config.json
    echo  [OK] Done.
    echo.
)

if exist "requirements.txt" (
    python -m pip install -r requirements.txt --quiet 2>nul
)

echo  Starting...
echo.

python console.py
pause
