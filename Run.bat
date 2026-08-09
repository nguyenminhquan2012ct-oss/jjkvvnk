@echo off
chcp 65001 >nul 2>&1
title HostBot v6.4
color 0D
cls

echo.
echo   =========================================
echo    HostBot v6.4 - Discord Self-Bot
echo   =========================================
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
    echo  Config not found.
    set /p "TK=  Discord Token: "
    echo {"token":"%TK%","prefix":"."} > config.json
    echo  [OK] Done.
    echo.
)

if exist "requirements.txt" (
    echo  Installing dependencies...
    python -m pip install -r requirements.txt --quiet 2>nul
    echo.
)

echo  Starting bot...
echo  (Ctrl+C to stop)
echo.

:restart
python main.py
echo.
echo  [!] Bot stopped. Restarting in 3 seconds...
timeout /t 3 /nobreak >nul
goto restart
