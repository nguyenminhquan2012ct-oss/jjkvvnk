# ============================================================
#  QU4N.TH3.D3V TERMINAL UI - JJK-VVNK BOT LAUNCHER
#  Chế độ Terminal UI để host bot trên PowerShell
#  Chạy: powershell -ExecutionPolicy Bypass -File launch.ps1
# ============================================================
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Stop"
$Host.UI.RawUI.WindowTitle = "JJK-VVNK Bot | QU4N.TH3.D3V"

$ESC = [char]27
$CONFIG_FILE = "config.json"
$BOT_FILE = "main.py"

# ========================= BANNER =========================
function Show-Banner {
    Clear-Host
    Write-Host ""
    Write-Host "${ESC}[38;2;180;0;255m        ___           _           _       ${ESC}[38;2;100;100;100mQU4N.TH3.D3V${ESC}[0m"
    Write-Host "${ESC}[38;2;180;0;255m       / (_)___ _ __ | |__  _   _| |_ ___ ${ESC}[0m"
    Write-Host "${ESC}[38;2;180;0;255m      / /| / __| '_ \| '_ \| | | | __/ _ \${ESC}[0m"
    Write-Host "${ESC}[38;2;180;0;255m     / / | \__ \ |_) | |_) | |_| | ||  __/ ${ESC}[0m"
    Write-Host "${ESC}[38;2;180;0;255m    /_/  |_|___/ .__/|_.__/ \__, |\__\___| ${ESC}[0m"
    Write-Host "${ESC}[38;2;180;0;255m              |_|          |___/          ${ESC}[0m"
    Write-Host ""
    Write-Host "${ESC}[38;2;255;0;0m  ╔═══════════════════════════════════════════════════╗${ESC}[0m"
    Write-Host "${ESC}[38;2;255;0;0m  ║${ESC}[0m  ${ESC}[38;2;255;255;255m⚔️  JJK-VVNK SELF-BOT v6.0 | Terminal UI${ESC}[0m      ${ESC}[38;2;255;0;0m║${ESC}[0m"
    Write-Host "${ESC}[38;2;255;0;0m  ╚═══════════════════════════════════════════════════╝${ESC}[0m"
    Write-Host ""
}

# ========================= MENU CHÍNH =========================
function Show-Menu {
    param([bool]$IsConfigured)

    if ($IsConfigured) {
        $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
        $mask = if ($cfg.Token.Length -gt 8) { $cfg.Token.Substring(0,4) + "****" + $cfg.Token.Substring($cfg.Token.Length-4) } else { "****" }
        Write-Host "${ESC}[38;2;180;0;255m  ┌─────────────────────────────────────────────┐${ESC}[0m"
        Write-Host "${ESC}[38;2;180;0;255m  │${ESC}[0m  ${ESC}[38;2;255;255;255mToken:${ESC}[0m  ${ESC}[38;2;255;255;0m$mask${ESC}[0m                          ${ESC}[38;2;180;0;255m│${ESC}[0m"
        Write-Host "${ESC}[38;2;180;0;255m  │${ESC}[0m  ${ESC}[38;2;255;255;255mPrefix:${ESC}[0m ${ESC}[38;2;0;255;0m$($cfg.Prefix)${ESC}[0m                                ${ESC}[38;2;180;0;255m│${ESC}[0m"
        Write-Host "${ESC}[38;2;180;0;255m  │${ESC}[0m  ${ESC}[38;2;255;255;255mStatus:${ESC}[0m ${ESC}[38;2;0;255;0m✅ Sẵn sàng${ESC}[0m                           ${ESC}[38;2;180;0;255m│${ESC}[0m"
        Write-Host "${ESC}[38;2;180;0;255m  └─────────────────────────────────────────────┘${ESC}[0m"
        Write-Host ""
    }

    Write-Host "${ESC}[38;2;0;170;255m  ╔═══════════════════════════════════════════╗${ESC}[0m"
    Write-Host "${ESC}[38;2;0;170;255m  ║${ESC}[0m                                           ${ESC}[38;2;0;170;255m│${ESC}[0m"
    Write-Host "${ESC}[38;2;0;170;255m  ║${ESC}[0m  ${ESC}[38;2;0;255;0m[1]${ESC}[0m 🚀 Chạy Bot                          ${ESC}[38;2;0;170;255m│${ESC}[0m"
    Write-Host "${ESC}[38;2;0;170;255m  ║${ESC}[0m  ${ESC}[38;2;255;255;0m[2]${ESC}[0m ⚙️  Cài Đặt / Đổi Token              ${ESC}[38;2;0;170;255m│${ESC}[0m"
    Write-Host "${ESC}[38;2;0;170;255m  ║${ESC}[0m  ${ESC}[38;2;255;0;0m[3]${ESC}[0m 📊 Xem Log                          ${ESC}[38;2;0;170;255m│${ESC}[0m"
    Write-Host "${ESC}[38;2;0;170;255m  ║${ESC}[0m  ${ESC}[38;2;180;0;255m[4]${ESC}[0m 🔧 Sửa config.json                   ${ESC}[38;2;0;170;255m│${ESC}[0m"
    Write-Host "${ESC}[38;2;0;170;255m  ║${ESC}[0m  ${ESC}[38;2;100;100;100m[5]${ESC}[0m 📁 Mở thư mục bot                    ${ESC}[38;2;0;170;255m│${ESC}[0m"
    Write-Host "${ESC}[38;2;0;170;255m  ║${ESC}[0m  ${ESC}[38;2;255;0;0m[0]${ESC}[0m ❌ Thoát                              ${ESC}[38;2;0;170;255m│${ESC}[0m"
    Write-Host "${ESC}[38;2;0;170;255m  ║${ESC}[0m                                           ${ESC}[38;2;0;170;255m│${ESC}[0m"
    Write-Host "${ESC}[38;2;0;170;255m  ╚═══════════════════════════════════════════╝${ESC}[0m"
    Write-Host ""
}

# ========================= SETUP =========================
function Start-Setup {
    Write-Host "${ESC}[38;2;0;170;255m  ┌─────────────────────────────────────────────┐${ESC}[0m"
    Write-Host "${ESC}[38;2;0;170;255m  │${ESC}[0m  ${ESC}[38;2;255;255;255m⚙️  CÀI ĐẶT BOT JJK-VVNK${ESC}[0m              ${ESC}[38;2;0;170;255m│${ESC}[0m"
    Write-Host "${ESC}[38;2;0;170;255m  └─────────────────────────────────────────────┘${ESC}[0m"
    Write-Host ""

    # Token
    $existingToken = ""
    if (Test-Path $CONFIG_FILE) {
        $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
        $existingToken = $cfg.Token
        Write-Host "${ESC}[38;2;100;100;100m  Token hiện tại: $($existingToken.Substring(0, [Math]::Min(8, $existingToken.Length)))...${ESC}[0m"
        Write-Host "${ESC}[38;2;100;100;100m  Nhấn Enter để giữ nguyên, hoặc dán token mới:${ESC}[0m"
    } else {
        Write-Host "${ESC}[38;2;255;255;255m  📌 Dán Discord Token của bạn:${ESC}[0m"
        Write-Host "${ESC}[38;2;100;100;100m  (Lấy tại: https://discord.com/developers/applications)${ESC}[0m"
    }
    Write-Host ""
    $newToken = Read-Host "${ESC}[38;2;0;255;0m  Token${ESC}[0m"
    if ([string]::IsNullOrWhiteSpace($newToken)) { $newToken = $existingToken }

    if ([string]::IsNullOrWhiteSpace($newToken)) {
        Write-Host "${ESC}[38;2;255;0;0m  ❌ Token không được để trống!${ESC}[0m"
        Start-Sleep -Seconds 2
        return $false
    }

    # Prefix
    $existingPrefix = "."
    if (Test-Path $CONFIG_FILE) {
        $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
        $existingPrefix = $cfg.Prefix
    }
    Write-Host ""
    Write-Host "${ESC}[38;2;255;255;255m  📌 Prefix cho bot (mặc định: .):${ESC}[0m"
    $newPrefix = Read-Host "${ESC}[38;2;0;255;0m  Prefix [$existingPrefix]${ESC}[0m"
    if ([string]::IsNullOrWhiteSpace($newPrefix)) { $newPrefix = $existingPrefix }

    # Lưu config
    @{ Token = $newToken; Prefix = $newPrefix } | ConvertTo-Json | Set-Content $CONFIG_FILE -Encoding UTF8
    Write-Host ""
    Write-Host "${ESC}[38;2;0;255;0m  ✅ Đã lưu config!${ESC}[0m"

    # Cài dependencies
    Write-Host ""
    Write-Host "${ESC}[38;2;255;255;255m  📦 Đang cài thư viện...${ESC}[0m"
    if (Test-Path "requirements.txt") {
        python -m pip install -r requirements.txt --quiet 2>&1 | Out-Null
        Write-Host "${ESC}[38;2;0;255;0m  ✅ Đã cài xong!${ESC}[0m"
    }

    Start-Sleep -Seconds 1
    return $true
}

# ========================= CHẠY BOT =========================
function Start-Bot {
    if (-not (Test-Path $CONFIG_FILE)) {
        Write-Host "${ESC}[38;2;255;0;0m  ❌ Chưa có config! Chọn [2] để cài đặt.${ESC}[0m"
        Start-Sleep -Seconds 2
        return
    }

    $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
    $env:BOT_TOKEN = $cfg.Token
    $env:DISCORD_TOKEN = $cfg.Token

    Clear-Host
    Write-Host ""
    Write-Host "${ESC}[38;2;180;0;255m  ╔═══════════════════════════════════════════╗${ESC}[0m"
    Write-Host "${ESC}[38;2;180;0;255m  ║${ESC}[0m  ${ESC}[38;2;0;255;0m🚀 BOT ĐANG CHẠY...${ESC}[0m                      ${ESC}[38;2;180;0;255m│${ESC}[0m"
    Write-Host "${ESC}[38;2;180;0;255m  ║${ESC}[0m  ${ESC}[38;2;100;100;100mNhấn Ctrl+C để dừng${ESC}[0m                   ${ESC}[38;2;180;0;255m│${ESC}[0m"
    Write-Host "${ESC}[38;2;180;0;255m  ╚═══════════════════════════════════════════╝${ESC}[0m"
    Write-Host ""

    try {
        python main.py
    } catch {
        Write-Host "${ESC}[38;2;255;0;0m  ❌ Lỗi: $_${ESC}[0m"
        Start-Sleep -Seconds 3
    }
}

# ========================= XEM LOG =========================
function Show-Log {
    Clear-Host
    Write-Host "${ESC}[38;2;180;0;255m  📊 LOG BOT (Ctrl+C để thoát)${ESC}[0m"
    Write-Host "${ESC}[38;2;100;100;100m  ─────────────────────────────────${ESC}[0m"

    $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
    $env:BOT_TOKEN = $cfg.Token
    $env:DISCORD_TOKEN = $cfg.Token

    try {
        python main.py 2>&1 | ForEach-Object { Write-Host "${ESC}[38;2;255;255;255m  $_${ESC}[0m" }
    } catch {
        Write-Host "${ESC}[38;2;100;100;100m  Log ended.${ESC}[0m"
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
        $choice = Read-Host "${ESC}[38;2;0;255;0m  Chọn [0-5]${ESC}[0m"

        switch ($choice) {
            "1" { Start-Bot }
            "2" { Start-Setup | Out-Null }
            "3" { Show-Log }
            "4" {
                if (Test-Path $CONFIG_FILE) {
                    notepad $CONFIG_FILE
                } else {
                    Write-Host "${ESC}[38;2;255;0;0m  ❌ Chưa có config!${ESC}[0m"
                    Start-Sleep -Seconds 2
                }
            }
            "5" { explorer.exe "." }
            "0" { $running = $false }
            default {
                Write-Host "${ESC}[38;2;255;255;0m  Chọn sai!${ESC}[0m"
                Start-Sleep -Seconds 1
            }
        }
    }
}

# ========================= KHỞI CHẠY =========================
if (-not (Test-Path $CONFIG_FILE)) {
    Show-Banner
    Write-Host "${ESC}[38;2;255;255;255m  Chào mừng bạn đến với JJK-VVNK Bot!${ESC}[0m"
    Write-Host "${ESC}[38;2;0;255;0m  Bắt đầu cài đặt...${ESC}[0m"
    Write-Host ""
    Start-Sleep -Seconds 1
    $setupDone = Start-Setup
    if (-not $setupDone) { exit 1 }
}

Main
