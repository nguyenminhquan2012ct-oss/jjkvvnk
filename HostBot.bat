```bat
@echo off
setlocal EnableExtensions EnableDelayedExpansion

title HostBot
color 0D
cls

echo.
echo                                                      QU4N.TH3.D3V
echo   ██╗   ██╗██╗   ██╗███╗   ██╗██╗  ██╗
echo   ██║   ██║██║   ██║████╗  ██║██║ ██╔╝
echo   ██║   ██║██║   ██║██╔██╗ ██║█████╔╝
echo   ╚██╗ ██╔╝╚██╗ ██╔╝██║╚██╗██║██╔═██╗
echo    ╚████╔╝  ╚████╔╝ ██║ ╚████║██║  ██╗
echo     ╚═══╝    ╚═══╝  ╚═╝  ╚═══╝╚═╝  ╚═╝
echo.
echo  ========================================
echo   HostBot v6.0 - Discord Self-Bot
echo  ========================================
echo.

REM ============================================================
REM  KIEM TRA PYTHON
REM ============================================================

where python >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Khong tim thay Python!
    echo.
    echo  Hay cai Python va chon "Add Python to PATH".
    echo.
    pause
    exit /b 1
)

echo  [OK] Python da san sang.
echo.

REM ============================================================
REM  TAO CONFIG NEU CHUA CO
REM ============================================================

if not exist "config.json" (
    echo  [!] Chua co config.json!
    echo  [?] Dang tao file config...
    echo.

    set "token="
    set "prefix="

    set /p "token=  Nhap Discord Token: "
    set /p "prefix=  Nhap Prefix (Enter = .): "

    if "!prefix!"=="" set "prefix=."

    powershell -NoProfile -Command "$t='!token!'; $p='!prefix!'; @{Token=$t;Prefix=$p} | ConvertTo-Json | Set-Content -LiteralPath 'config.json' -Encoding UTF8"

    if errorlevel 1 (
        echo.
        echo  [ERROR] Khong the tao config.json!
        pause
        exit /b 1
    )

    echo.
    echo  [OK] Da luu config.json!
    echo.
)

REM ============================================================
REM  KIEM TRA CONFIG
REM ============================================================

if not exist "config.json" (
    echo  [ERROR] config.json khong ton tai!
    pause
    exit /b 1
)

echo  [*] Dang kiem tra config.json...

powershell -NoProfile -Command "$c=Get-Content -LiteralPath 'config.json' -Raw | ConvertFrom-Json; if ([string]::IsNullOrWhiteSpace($c.Token)) { exit 1 }"

if errorlevel 1 (
    echo  [ERROR] Token trong config.json dang rong hoac khong hop le!
    pause
    exit /b 1
)

echo  [OK] config.json hop le.
echo.

REM ============================================================
REM  CAI THU VIEN
REM ============================================================

if not exist "requirements.txt" (
    echo  [WARNING] Khong tim thay requirements.txt!
    echo  [!] Bo qua buoc cai thu vien.
    echo.
) else (
    echo  [*] Dang kiem tra thu vien...

    python -m pip install -r requirements.txt

    if errorlevel 1 (
        echo.
        echo  [ERROR] Cai thu vien that bai!
        echo  [!] Kiem tra Internet va requirements.txt.
        echo.
        pause
        exit /b 1
    )

    echo.
    echo  [OK] Thu vien da san sang!
    echo.
)

REM ============================================================
REM  LOAD TOKEN
REM ============================================================

set "BOT_TOKEN="

for /f "usebackq tokens=*" %%i in (`powershell -NoProfile -Command "(Get-Content -LiteralPath 'config.json' -Raw | ConvertFrom-Json).Token"`) do (
    set "BOT_TOKEN=%%i"
)

if "!BOT_TOKEN!"=="" (
    echo  [ERROR] Khong doc duoc Token tu config.json!
    pause
    exit /b 1
)

set "DISCORD_TOKEN=!BOT_TOKEN!"

echo  [OK] Token da load!
echo.
echo  [*] Dang khoi dong bot...
echo  ========================================
echo.

REM ============================================================
REM  CHAY BOT
REM ============================================================

if not exist "main.py" (
    echo  [ERROR] Khong tim thay main.py!
    echo.
    pause
    exit /b 1
)

python main.py

set "BOT_EXIT_CODE=!errorlevel!"

echo.
echo  ========================================

if not "!BOT_EXIT_CODE!"=="0" (
    echo  [ERROR] Bot dung voi ma loi: !BOT_EXIT_CODE!
) else (
    echo  [OK] Bot da dung.
)

echo  ========================================
echo.

pause
exit /b !BOT_EXIT_CODE!
```
