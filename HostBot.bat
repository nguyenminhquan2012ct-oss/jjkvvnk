@echo off
chcp 65001 >nul 2>&1
title HostBot
color 0D
cls
setlocal enabledelayedexpansion

echo.
echo                                                    QU4N.TH3.D3V
echo   =============================================================
echo   HostBot v6.4 - Discord Self-Bot
echo   =============================================================
echo.

where python >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python not found!
    pause
    exit /b 1
)

for /f "tokens=*" %%A in ('python --version 2^>^&1') do echo  [OK] %%A
echo.

rem Luon bat nhap Token moi lan mo bat
set /p "TK=  Nhap Discord Token: "
if "!TK!"=="" (
    echo  [ERROR] Token khong duoc de trong!
    pause
    exit /b 1
)

echo {"token":"!TK!","prefix":"."} > config.json
echo  [OK] Da luu Token vao config.json.
echo.

if exist "requirements.txt" (
    python -m pip install -r requirements.txt --quiet 2>nul
)

echo  Starting Console...
echo.

python console.py
pause