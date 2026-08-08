@echo off
title JJK-VVNK Bot
cls
color 0D

echo.
echo    ___           _           _       QU4N.TH3.D3V
echo   / (^ _)___ _ __ ^| ^|__  _   ^|_ ___ 
echo  / /^| / __^| '_ \^| '_ \^| ^| ^| ^| __/ _ \
echo / / ^| \__ \ ^|_) ^| ^|_) ^| ^|_^| ^| ^|  __/ 
echo /_/  ^|_^|___/ .__/^|_.__/ \__, ^|^\__\___^| 
echo             ^|_^|          ^|___/          
echo.
echo  ========================================
echo   JJK-VVNK Self-Bot v6.0
echo  ========================================
echo.

if not exist config.json (
    echo  [!] Chua co config.json!
    echo  [?] Dang tao file config...
    echo.
    set /p token="  Nhap Discord Token: "
    set /p prefix="  Nhap Prefix (Enter = .): "
    if "!prefix!"=="" set prefix=.

    powershell -Command "$t='%token%'; $p='%prefix%'; if($p -eq ''){$p='.'}; @{Token=$t;Prefix=$p} | ConvertTo-Json | Set-Content config.json -Encoding UTF8"
    echo  [OK] Da luu config.json!
    echo.
)

echo  [*] Dang kiem tra thu vien...
python -m pip install -r requirements.txt 2>nul
if %errorlevel%==0 (
    echo.
    echo  [OK] Thu vien da san sang!
) else (
    echo.
    echo  [!] Co loi xay ra, thu chay lai...
)
echo.

for /f "tokens=*" %%i in ('powershell -Command "(Get-Content config.json -Raw | ConvertFrom-Json).Token"') do set BOT_TOKEN=%%i
set DISCORD_TOKEN=%BOT_TOKEN%

echo  [OK] Token da load!
echo  [*] Dang khoi dong bot...
echo  ========================================
echo.
python main.py
echo.
echo  ========================================
echo  [*] Bot da dung.
pause
