@echo off
chcp 65001 >nul 2>&1
setlocal EnableExtensions EnableDelayedExpansion

title HostBot
color 0D
cls

echo.
echo                                                    QU4N.TH3.D3V
echo   ██╗   ██╗██╗   ██╗███╗   ██╗██╗  ██╗
echo   ██║   ██║██║   ██║████╗  ██║██║ ██╔╝
echo   ██║   ██║██║   ██║██╔██╗ ██║█████═╝
echo   ╚██╗ ██╔╝╚██╗ ██╔╝██║╚██╗██║██╔═██╗
echo    ╚████╔╝  ╚████╔╝ ██║ ╚████║██║  ██╗
echo     ╚═══╝    ╚═══╝  ╚═╝  ╚═══╝╚═╝  ╚═╝
echo.
echo  ========================================
echo   HostBot v6.3 - Discord Self-Bot
echo  ========================================
echo.

REM === CHECK PYTHON ===
echo  [1/3] Checking Python...
where python >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python not found. Install Python and add to PATH.
    pause
    exit /b 1
)
for /f "tokens=*" %%A in ('python --version 2^>^&1') do set "PV=%%A"
echo  [OK] !PV!
echo.

REM === CHECK CONFIG ===
echo  [2/3] Checking config...
if not exist "config.json" (
    echo.
    echo  config.json not found. Creating...
    echo.
    set /p "TK=  Discord Token: "
    set /p "PX=  Prefix [.]: "
    if "!PX!"=="" set "PX=."

    echo {"token":"!TK!","prefix":"!PX!"} > "config.json"
    echo  [OK] config.json created.
    echo.
) else (
    echo  [OK] config.json found.
    echo.
)

REM === CHECK DEPS ===
echo  [3/3] Checking dependencies...
if exist "requirements.txt" (
    python -m pip install -r requirements.txt --quiet 2>nul
)
echo  [OK] Ready.
echo.

REM === START ===
echo  ========================================
echo        STARTING HOSTBOT...
echo  ========================================
echo.

python console.py

echo.
echo  ========================================
echo  HostBot stopped.
echo  ========================================
pause
