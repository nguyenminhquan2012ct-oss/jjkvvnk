@echo off
title JJK-VVNK Bot | QU4N.TH3.D3V
color 0D
cls
echo.
echo    ___           _           _       QU4N.TH3.D3V
echo   / (_)___ _ __ ^| ^|__  _   ^|_ ___
echo  / /^| / __^| '_ \^| '_ \^| ^| ^| ^| __/ _ \
echo / / ^| \__ \ ^|_) ^| ^|_) ^| ^|_^| ^| ^|  __/
echo /_/  ^|_^|___/ .__/^|_.__/ \__, ^|^\__\___^|
echo             ^|_^|          ^|___/
echo.
echo  ========================================
echo   JJK-VVNK Self-Bot v6.0 - Terminal UI
echo  ========================================
echo.
echo  [1] Chay Bot
echo  [2] Cai Dat / Doi Token
echo  [3] Xem Log
echo  [0] Thoat
echo.
set /p choice="  Chon: "

if "%choice%"=="1" goto RUN
if "%choice%"=="2" goto SETUP
if "%choice%"=="3" goto LOG
if "%choice%"=="0" exit

:SETUP
echo.
echo  Dang mo launcher...
powershell -ExecutionPolicy Bypass -File "%~dp0launch.ps1"
goto MENU

:RUN
echo.
echo  Dang khoi dong bot...
if not exist config.json (
    echo  Chua co config! Chay launcher de cai dat truoc.
    powershell -ExecutionPolicy Bypass -File "%~dp0launch.ps1"
    goto MENU
)
for /f "tokens=*" %%i in ('powershell -Command "(Get-Content config.json -Raw | ConvertFrom-Json).Token"') do set BOT_TOKEN=%%i
set DISCORD_TOKEN=%BOT_TOKEN%
python -m pip install -r requirements.txt -q 2>nul
python main.py
pause
goto MENU

:LOG
echo.
echo  Dang xem log (Ctrl+C de dung)...
if not exist config.json (
    echo  Chua co config!
    pause
    goto MENU
)
for /f "tokens=*" %%i in ('powershell -Command "(Get-Content config.json -Raw | ConvertFrom-Json).Token"') do set BOT_TOKEN=%%i
set DISCORD_TOKEN=%BOT_TOKEN%
python main.py
pause
goto MENU

:MENU
cls
echo.
echo    ___           _           _       QU4N.TH3.D3V
echo   / (_)___ _ __ ^| ^|__  _   ^|_ ___
echo  / /^| / __^| '_ \^| '_ \^| ^| ^| ^| __/ _ \
echo / / ^| \__ \ ^|_) ^| ^|_) ^| ^|_^| ^| ^|  __/
echo /_/  ^|_^|___/ .__/^|_.__/ \__, ^|^\__\___^|
echo             ^|_^|          ^|___/
echo.
echo  ========================================
echo   JJK-VVNK Self-Bot v6.0 - Terminal UI
echo  ========================================
echo.
echo  [1] Chay Bot
echo  [2] Cai Dat / Doi Token
echo  [3] Xem Log
echo  [0] Thoat
echo.
set /p choice="  Chon: "

if "%choice%"=="1" goto RUN
if "%choice%"=="2" goto SETUP
if "%choice%"=="3" goto LOG
if "%choice%"=="0" exit
goto MENU
