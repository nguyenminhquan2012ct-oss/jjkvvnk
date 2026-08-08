@echo off
setlocal EnableExtensions EnableDelayedExpansion

title HostBot
color 0D
cls

echo.
echo                                                    QU4N.TH3.D3V
echo  ██╗   ██╗██╗   ██╗███╗   ██╗██╗  ██╗
echo  ██║   ██║██║   ██║████╗  ██║██║ ██╔╝
echo  ██║   ██║██║   ██║██╔██╗ ██║█████═╝ 
echo  ╚██╗ ██╔╝╚██╗ ██╔╝██║╚██╗██║██╔═██╗ 
echo   ╚████╔╝  ╚████╔╝ ██║ ╚████║██║  ██╗
echo    ╚═══╝    ╚═══╝  ╚═╝  ╚═══╝╚═╝  ╚═╝
echo.
echo  ========================================
echo   HostBot v6.0 - Discord Self-Bot
echo  ========================================
echo.

REM ============================================================
REM  CHECK PYTHON
REM ============================================================

echo  [1/5] Checking Python...

where python >nul 2>&1

if errorlevel 1 (
    echo.
    echo  [ERROR] Python was not found.
    echo.
    echo  Please install Python and enable:
    echo  Add Python to PATH
    echo.
    pause
    exit /b 1
)

for /f "tokens=*" %%A in ('python --version 2^>^&1') do (
    set "PYTHON_VERSION=%%A"
)

echo  [ OK ] !PYTHON_VERSION!
echo.

REM ============================================================
REM  CHECK PIP
REM ============================================================

echo  [2/5] Checking pip...

python -m pip --version >nul 2>&1

if errorlevel 1 (
    echo.
    echo  [ERROR] pip is not available.
    echo.
    pause
    exit /b 1
)

echo  [ OK ] pip is available.
echo.

REM ============================================================
REM  CONFIGURATION
REM ============================================================

echo  [3/5] Checking configuration...

if not exist "config.json" (
    echo.
    echo  [INFO] config.json not found.
    echo  [INFO] Creating configuration...
    echo.

    set "token="
    set "prefix=."

    set /p "token=  Discord Token: "
    set /p "prefix=  Prefix [Enter = .]: "

    if "!prefix!"=="" set "prefix=."

    powershell -NoProfile -Command "$config = @{Token='!token!'; Prefix='!prefix!'}; $config | ConvertTo-Json | Set-Content -LiteralPath 'config.json' -Encoding UTF8"

    if errorlevel 1 (
        echo.
        echo  [ERROR] Failed to create config.json.
        echo.
        pause
        exit /b 1
    )

    echo.
    echo  [ OK ] config.json created.
    echo.
)

REM ============================================================
REM  VALIDATE CONFIG
REM ============================================================

if not exist "config.json" (
    echo  [ERROR] config.json is missing.
    echo.
    pause
    exit /b 1
)

powershell -NoProfile -Command "$c=Get-Content -LiteralPath 'config.json' -Raw | ConvertFrom-Json; if ([string]::IsNullOrWhiteSpace($c.Token)) { exit 1 }"

if errorlevel 1 (
    echo.
    echo  [ERROR] Token is missing or invalid.
    echo  [INFO ] Edit config.json and try again.
    echo.
    pause
    exit /b 1
)

echo  [ OK ] config.json is valid.
echo.

REM ============================================================
REM  DEPENDENCIES
REM ============================================================

echo  [4/5] Checking dependencies...

if exist "requirements.txt" (
    python -m pip install -r requirements.txt

    if errorlevel 1 (
        echo.
        echo  [ERROR] Failed to install dependencies.
        echo.
        echo  Check your Internet connection and
        echo  requirements.txt.
        echo.
        pause
        exit /b 1
    )

    echo.
    echo  [ OK ] Dependencies ready.
) else (
    echo  [WARN] requirements.txt not found.
    echo  [INFO] Skipping dependency installation.
)

echo.

REM ============================================================
REM  APPLICATION
REM ============================================================

echo  [5/5] Checking application...

if not exist "main.py" (
    echo.
    echo  [ERROR] main.py was not found.
    echo.
    echo  Current directory:
    echo  %CD%
    echo.
    pause
    exit /b 1
)

echo  [ OK ] main.py found.
echo.

REM ============================================================
REM  START HOSTBOT
REM ============================================================

echo  ========================================
echo.
echo          STARTING HOSTBOT...
echo.
echo  ========================================
echo.

python main.py

set "EXIT_CODE=!errorlevel!"

echo.
echo  ========================================

if "!EXIT_CODE!"=="0" (
    echo  [ OK ] HostBot stopped normally.
) else (
    echo  [ERROR] HostBot exited with code !EXIT_CODE!
)

echo  ========================================
echo.

pause
exit /b !EXIT_CODE!
```
