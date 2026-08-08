# ============================================================
#  JJK-VVNK BOT - 1-CLICK INSTALLER
#  Chay: irm https://raw.githubusercontent.com/nguyenminhquan2012ct-oss/jjkvvnk/main/setup.ps1 | iex
# ============================================================
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Stop"

$REPO_URL = "https://github.com/nguyenminhquan2012ct-oss/jjkvvnk"
$INSTALL_DIR = "$env:USERPROFILE\JJK-VVNK"

function Write-Color {
    param([string]$Text, [ConsoleColor]$Color = "White")
    Write-Host $Text -ForegroundColor $Color
}

# ========================= BANNER =========================
function Show-Banner {
    Clear-Host
    Write-Host ""
    Write-Color "        ___           _           _       QU4N.TH3.D3V" Purple
    Write-Color "       / (_)___ _ __ | |__  _   _| |_ ___ " Purple
    Write-Color "      / /| / __| '_ \_| '_ \_| | | | __/ _ \" Purple
    Write-Color "     / / | \__ \ |_) | |_) | |_| | ||  __/ " Purple
    Write-Color "    /_/  |_|___/ .__/|_.__/ \__, |\__\___| " Purple
    Write-Color "              |_|          |___/          " Purple
    Write-Host ""
    Write-Color "  ============================================" Red
    Write-Color "    JJK-VVNK SELF-BOT v6.0 - 1-CLICK INSTALL" White
    Write-Color "  ============================================" Red
    Write-Host ""
}

# ========================= KIEM TRA =========================
function Test-Requirements {
    Write-Color "  [1/4] Kiem tra he thong..." Cyan

    # Python
    try {
        $pyVer = python --version 2>&1
        Write-Color "    OK Python: $pyVer" Green
    } catch {
        Write-Color "    LOI Python chua cai! Tai tai: https://python.org" Red
        return $false
    }

    # Git
    try {
        $gitVer = git --version 2>&1
        Write-Color "    OK Git: $gitVer" Green
    } catch {
        Write-Color "    CANH BAO Git khong co (khong bat buoc)" Yellow
    }

    # pip
    $pipOk = $false
    try {
        $pipOutput = python -m pip --version 2>&1
        if ($pipOutput -match "pip") { $pipOk = $true }
    } catch {}

    if ($pipOk) {
        Write-Color "    OK pip: $pipOutput" Green
    } else {
        Write-Color "    DANG CAI pip..." Yellow
        try {
            python -m ensurepip --upgrade 2>&1 | Out-Null
            python -m pip install --upgrade pip 2>&1 | Out-Null
            Write-Color "    OK Da cai pip!" Green
        } catch {
            Write-Color "    LOI Khong the cai pip! Thu cong: python -m ensurepip --upgrade" Red
            return $false
        }
    }

    return $true
}

# ========================= TAI BOT =========================
function Install-Bot {
    Write-Host ""
    Write-Color "  [2/4] Tai bot tu GitHub..." Cyan

    if (Test-Path $INSTALL_DIR) {
        Write-Color "    CANH BAO Thu muc da ton tai: $INSTALL_DIR" Yellow
        $overwrite = Read-Host "    Ghi de? (y/n)"
        if ($overwrite -ne "y") {
            Write-Color "    Giu nguyen thu muc cu." Green
            return $true
        }
        Remove-Item $INSTALL_DIR -Recurse -Force
    }

    # Git clone
    try {
        Write-Color "    Dang clone repo..." White
        git clone $REPO_URL $INSTALL_DIR 2>&1 | Out-Null
        Write-Color "    OK Da tai xong!" Green
        return $true
    } catch {
        Write-Color "    CANH BAO Git clone that bai, thu tai zip..." Yellow
    }

    # Zip fallback
    try {
        $zipUrl = "$REPO_URL/archive/refs/heads/main.zip"
        $zipPath = "$env:TEMP\jjk-vvnk.zip"
        Write-Color "    Dang tai zip..." White
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
        Invoke-WebRequest -Uri $zipUrl -OutFile $zipPath -UseBasicParsing
        Write-Color "    Dang giai nen..." White
        Expand-Archive -Path $zipPath -DestinationPath $env:TEMP -Force
        $extractedDir = Get-ChildItem "$env:TEMP\jjkvvnk-*" -Directory | Select-Object -First 1
        if ($extractedDir) {
            Move-Item $extractedDir.FullName $INSTALL_DIR -Force
        }
        Remove-Item $zipPath -Force
        Write-Color "    OK Da tai zip xong!" Green
        return $true
    } catch {
        Write-Color "    LOI Khong the tai bot: $_" Red
        return $false
    }
}

# ========================= CAI DAT =========================
function Setup-Bot {
    Write-Host ""
    Write-Color "  [3/4] Cai dat dependencies..." Cyan
    Set-Location $INSTALL_DIR

    if (Test-Path "requirements.txt") {
        Write-Color "    Dang cai... (co the mat 1-2 phut)" Yellow
        try {
            python -m pip install -r requirements.txt 2>&1 | Out-Null
            Write-Color "    OK Da cai xong dependencies!" Green
        } catch {
            Write-Color "    CANH BAO Mot so thu vien chua cai duoc" Yellow
            python -m pip install -r requirements.txt 2>&1
        }
    } else {
        Write-Color "    CANH BAO Khong tim thay requirements.txt" Yellow
    }
}

# ========================= CONFIG =========================
function Set-Config {
    Write-Host ""
    Write-Color "  [4/4] Cau hinh bot..." Cyan

    $configFile = "$INSTALL_DIR\config.json"

    Write-Host ""
    Write-Color "  DAN Discord Token cua ban:" White
    Write-Color "  (Lay tai: https://discord.com/developers/applications)" DarkGray
    Write-Host ""
    $token = Read-Host "  Token"

    if ([string]::IsNullOrWhiteSpace($token)) {
        Write-Color "  LOI Token khong duoc trong!" Red
        return $false
    }

    Write-Host ""
    Write-Color "  PREFIX cho bot (Enter = .):" White
    $prefix = Read-Host "  Prefix"
    if ([string]::IsNullOrWhiteSpace($prefix)) { $prefix = "." }

    @{ Token = $token; Prefix = $prefix } | ConvertTo-Json | Set-Content $configFile -Encoding UTF8
    Write-Host ""
    Write-Color "  OK Da luu config!" Green
    return $true
}

# ========================= HOAN TAT =========================
function Show-Done {
    Write-Host ""
    Write-Color "  ============================================" Green
    Write-Color "    CAI DAT HOAN TAT!" Green
    Write-Color "  ============================================" Green
    Write-Host ""
    Write-Color "  Thu muc bot: $INSTALL_DIR" White
    Write-Host ""
    Write-Color "  CACH CHAY:" Cyan
    Write-Color "     1. Double-click file JJK-VVNK.bat" White
    Write-Color "     2. Hoac: powershell -ExecutionPolicy Bypass -File launch.ps1" White
    Write-Host ""

    $runNow = Read-Host "  Chay bot ngay? (y/n)"
    if ($runNow -eq "y") {
        Set-Location $INSTALL_DIR
        $cfg = Get-Content "config.json" -Raw | ConvertFrom-Json
        $env:BOT_TOKEN = $cfg.Token
        $env:DISCORD_TOKEN = $cfg.Token
        Write-Host ""
        Write-Color "  Dang khoi dong bot..." Green
        Write-Host ""
        python main.py
    }
}

# ========================= MAIN =========================
Show-Banner

if (-not (Test-Requirements)) {
    Write-Host ""
    Read-Host "  Nhan Enter de thoat"
    exit 1
}

if (-not (Install-Bot)) {
    Write-Host ""
    Read-Host "  Nhan Enter de thoat"
    exit 1
}

Setup-Bot
Set-Config | Out-Null
Show-Done
