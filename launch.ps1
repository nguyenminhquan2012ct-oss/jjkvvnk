# ============================================================
#  QU4N.TH3.D3V TERMINAL UI - JJK-VVNK BOT LAUNCHER
#  Chay: powershell -ExecutionPolicy Bypass -File launch.ps1
# ============================================================
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Stop"
$Host.UI.RawUI.WindowTitle = "JJK-VVNK Bot | QU4N.TH3.D3V"

$CONFIG_FILE = "config.json"

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
    Write-Color "  ================================================" DarkCyan
    Write-Color "    JJK-VVNK SELF-BOT v6.0 | Terminal UI Edition" White
    Write-Color "  ================================================" DarkCyan
    Write-Host ""
}

# ========================= MENU CHINH =========================
function Show-Menu {
    param([bool]$IsConfigured)

    if ($IsConfigured) {
        $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
        $mask = if ($cfg.Token.Length -gt 8) { $cfg.Token.Substring(0,4) + "****" + $cfg.Token.Substring($cfg.Token.Length-4) } else { "****" }
        Write-Color "  +-------------------------------------------+" Magenta
        Write-Color "  |  Token:  $mask" White
        Write-Color "  |  Prefix: $($cfg.Prefix)" Green
        Write-Color "  |  Status: SAN SANG" Green
        Write-Color "  +-------------------------------------------+" Magenta
        Write-Host ""
    }

    Write-Color "  +-------------------------------------------+" Cyan
    Write-Color "  |                                           |" Cyan
    Write-Color "  |  [1] CHAY BOT                        |" Cyan -NoNewline; Write-Color "]" Green; Write-Host ""
    Write-Color "  |  [2] CAI DAT / DOI TOKEN             |" Cyan -NoNewline; Write-Color "]" Yellow; Write-Host ""
    Write-Color "  |  [3] XEM LOG                         |" Cyan -NoNewline; Write-Color "]" Red; Write-Host ""
    Write-Color "  |  [4] SUA config.json                 |" Cyan -NoNewline; Write-Color "]" Magenta; Write-Host ""
    Write-Color "  |  [5] MO THU MUC BOT                 |" Cyan -NoNewline; Write-Color "]" DarkGray; Write-Host ""
    Write-Color "  |  [0] THOAT                           |" Cyan -NoNewline; Write-Color "]" Red; Write-Host ""
    Write-Color "  |                                           |" Cyan
    Write-Color "  +-------------------------------------------+" Cyan
    Write-Host ""
}

# ========================= SETUP =========================
function Start-Setup {
    Write-Color "  +-------------------------------------------+" Yellow
    Write-Color "  |  CAI DAT BOT JJK-VVNK                    |" Yellow
    Write-Color "  +-------------------------------------------+" Yellow
    Write-Host ""

    $existingToken = ""
    if (Test-Path $CONFIG_FILE) {
        $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
        $existingToken = $cfg.Token
        Write-Color "  Token hien tai: $($existingToken.Substring(0, [Math]::Min(8, $existingToken.Length)))..." DarkGray
        Write-Color "  Nhan Enter de giu nguyen, hoac dan token moi:" DarkGray
    } else {
        Write-Color "  DAN Discord Token cua ban:" White
        Write-Color "  (Lay tai: https://discord.com/developers/applications)" DarkGray
    }
    Write-Host ""
    $newToken = Read-Host "  Token"
    if ([string]::IsNullOrWhiteSpace($newToken)) { $newToken = $existingToken }

    if ([string]::IsNullOrWhiteSpace($newToken)) {
        Write-Color "  LOI Token khong duoc de trong!" Red
        Start-Sleep -Seconds 2
        return $false
    }

    $existingPrefix = "."
    if (Test-Path $CONFIG_FILE) {
        $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
        $existingPrefix = $cfg.Prefix
    }
    Write-Host ""
    Write-Color "  PREFIX cho bot (mac dinh: .):" White
    $newPrefix = Read-Host "  Prefix [$existingPrefix]"
    if ([string]::IsNullOrWhiteSpace($newPrefix)) { $newPrefix = $existingPrefix }

    @{ Token = $newToken; Prefix = $newPrefix } | ConvertTo-Json | Set-Content $CONFIG_FILE -Encoding UTF8
    Write-Host ""
    Write-Color "  OK Da luu config!" Green

    Write-Host ""
    Write-Color "  Dang cai thu vien..." White
    if (Test-Path "requirements.txt") {
        python -m pip install -r requirements.txt --quiet 2>&1 | Out-Null
        Write-Color "  OK Da cai xong!" Green
    }

    Start-Sleep -Seconds 1
    return $true
}

# ========================= CHAY BOT =========================
function Start-Bot {
    if (-not (Test-Path $CONFIG_FILE)) {
        Write-Color "  LOI Chua co config! Chon [2] de cai dat." Red
        Start-Sleep -Seconds 2
        return
    }

    $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
    $env:BOT_TOKEN = $cfg.Token
    $env:DISCORD_TOKEN = $cfg.Token

    Clear-Host
    Write-Host ""
    Write-Color "  +-------------------------------------------+" Green
    Write-Color "  |  BOT DANG CHAY...                         |" Green
    Write-Color "  |  Nhan Ctrl+C de dung                      |" DarkGray
    Write-Color "  +-------------------------------------------+" Green
    Write-Host ""

    try {
        python main.py
    } catch {
        Write-Color "  LOI: $_" Red
        Start-Sleep -Seconds 3
    }
}

# ========================= XEM LOG =========================
function Show-Log {
    Clear-Host
    Write-Color "  LOG BOT (Ctrl+C de thoat)" Magenta
    Write-Color "  -----------------------------------" DarkGray

    $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
    $env:BOT_TOKEN = $cfg.Token
    $env:DISCORD_TOKEN = $cfg.Token

    try {
        python main.py 2>&1 | ForEach-Object { Write-Color "  $_" White }
    } catch {
        Write-Color "  Log ended." DarkGray
    }
    Start-Sleep -Seconds 2
}

# ========================= MAIN LOOP =========================
function Main {
    $running = $true
    while ($running) {
        $isConfigured = Test-Path $CONFIG_FILE
        Show-Banner
        Show-Menu $isConfigured
        $choice = Read-Host "  Chon [0-5]"

        switch ($choice) {
            "1" { Start-Bot }
            "2" { Start-Setup | Out-Null }
            "3" { Show-Log }
            "4" {
                if (Test-Path $CONFIG_FILE) {
                    notepad $CONFIG_FILE
                } else {
                    Write-Color "  LOI Chua co config!" Red
                    Start-Sleep -Seconds 2
                }
            }
            "5" { explorer.exe "." }
            "0" { $running = $false }
            default {
                Write-Color "  Chon sai!" Yellow
                Start-Sleep -Seconds 1
            }
        }
    }
}

# ========================= KHOI CHAY =========================
if (-not (Test-Path $CONFIG_FILE)) {
    Show-Banner
    Write-Color "  Chao mung ban den voi JJK-VVNK Bot!" White
    Write-Color "  Bat dau cai dat..." Green
    Write-Host ""
    Start-Sleep -Seconds 1
    $setupDone = Start-Setup
    if (-not $setupDone) { exit 1 }
}

Main
