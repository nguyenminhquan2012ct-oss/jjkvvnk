# ============================================================
#  QU4N.TH3.D3V TERMINAL UI - JJK-VVNK BOT LAUNCHER
#  Chế độ Terminal UI để host bot trên PowerShell
# ============================================================
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Stop"
$Host.UI.RawUI.WindowTitle = "JJK-VVNK Bot | QU4N.TH3.D3V"

$CONFIG_FILE = "config.json"
$BOT_FILE = "main.py"

# ========================= BANNER =========================
function Show-Banner {
    Clear-Host
    $c = @{
        R = "`e[38;2;255;0;0m"
        G = "`e[38;2;0;255;0m"
        B = "`e[38;2;0;170;255m"
        P = "`e[38;2;180;0;255m"
        Y = "`e[38;2;255;255;0m"
        W = "`e[38;2;255;255;255m"
        D = "`e[38;2;100;100;100m"
        E = "`e[0m"
    }
    Write-Host ""
    Write-Host "$($c.P)        ___           _           _       $($c.D)QU4N.TH3.D3V$($c.E)"
    Write-Host "$($c.P)       / (_)___ _ __ | |__  _   _| |_ ___ $($c.E)"
    Write-Host "$($c.P)      / /| / __| '_ \| '_ \| | | | __/ _ \`$($c.E)"
    Write-Host "$($c.P)     / / | \__ \ |_) | |_) | |_| | ||  __/ $($c.E)"
    Write-Host "$($c.P)    /_/  |_|___/ .__/|_.__/ \__, |\__\___| $($c.E)"
    Write-Host "$($c.P)              |_|          |___/          $($c.E)"
    Write-Host ""
    Write-Host "$($c.D)═══════════════════════════════════════════════════════════$($c.E)"
    Write-Host "$($c.R)  ⚔️  JJK-VVNK SELF-BOT v6.0  |  Terminal UI Edition    $($c.E)"
    Write-Host "$($c.D)═══════════════════════════════════════════════════════════$($c.E)"
    Write-Host ""
}

# ========================= MENU CHÍNH =========================
function Show-Menu {
    param([bool]$IsConfigured)
    $c = @{R="`e[38;2;255;0;0m";G="`e[38;2;0;255;0m";B="`e[38;2;0;170;255m";Y="`e[38;2;255;255;0m";W="`e[38;2;255;255;255m";D="`e[38;2;100;100;100m";E="`e[0m";P="`e[38;2;180;0;255m"}

    if ($IsConfigured) {
        $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
        $mask = if ($cfg.Token.Length -gt 8) { $cfg.Token.Substring(0,4) + "****" + $cfg.Token.Substring($cfg.Token.Length-4) } else { "****" }
        Write-Host "$($c.P)  ┌─────────────────────────────────────────────┐$($c.E)"
        Write-Host "$($c.P)  │$($c.E)  $($c.W)Token:$($c.E)  $($c.Y)$mask$($c.E)                          $($c.P)|$($c.E)"
        Write-Host "$($c.P)  │$($c.E)  $($c.W)Prefix:$($c.E) $($c.G)$($cfg.Prefix)$($c.E)                                $($c.P)|$($c.E)"
        Write-Host "$($c.P)  │$($c.E)  $($c.W)Status:$($c.E) $($c.G)✅ Sẵn sàng$($c.E)                           $($c.P)|$($c.E)"
        Write-Host "$($c.P)  └─────────────────────────────────────────────┘$($c.E)"
        Write-Host ""
    }

    Write-Host "$($c.B)  ╔═══════════════════════════════════════════╗$($c.E)"
    Write-Host "$($c.B)  ║$($c.E)                                           $($c.B)|$($c.E)"
    Write-Host "$($c.B)  ║$($c.E)  $($c.G)[1]$($c.E) 🚀 Chạy Bot                          $($c.B)|$($c.E)"
    Write-Host "$($c.B)  ║$($c.E)  $($c.Y)[2]$($c.E) ⚙️  Cài Đặt / Đổi Token              $($c.B)|$($c.E)"
    Write-Host "$($c.B)  ║$($c.E)  $($c.R)[3]$($c.E) 📊 Xem Log                          $($c.B)|$($c.E)"
    Write-Host "$($c.B)  ║$($c.E)  $($c.P)[4]$($c.E) 🔧 Sửa config.json                   $($c.B)|$($c.E)"
    Write-Host "$($c.B)  ║$($c.E)  $($c.D)[5]$($c.E) 📁 Mở thư mục bot                    $($c.B)|$($c.E)"
    Write-Host "$($c.B)  ║$($c.E)  $($c.R)[0]$($c.E) ❌ Thoát                              $($c.B)|$($c.E)"
    Write-Host "$($c.B)  ║$($c.E)                                           $($c.B)|$($c.E)"
    Write-Host "$($c.B)  ╚═══════════════════════════════════════════╝$($c.E)"
    Write-Host ""
}

# ========================= SETUP =========================
function Start-Setup {
    $c = @{R="`e[38;2;255;0;0m";G="`e[38;2;0;255;0m";B="`e[38;2;0;170;255m";Y="`e[38;2;255;255;0m";W="`e[38;2;255;255;255m";D="`e[38;2;100;100;100m";E="`e[0m";P="`e[38;2;180;0;255m"}

    Write-Host "$($c.B)  ┌─────────────────────────────────────────────┐$($c.E)"
    Write-Host "$($c.B)  │$($c.E)  $($c.W)⚙️  CÀI ĐẶT BOT JJK-VVNK$($c.E)              $($c.B)|$($c.E)"
    Write-Host "$($c.B)  └─────────────────────────────────────────────┘$($c.E)"
    Write-Host ""

    # Token
    $existingToken = ""
    if (Test-Path $CONFIG_FILE) {
        $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
        $existingToken = $cfg.Token
        Write-Host "$($c.D)  Token hiện tại: $($existingToken.Substring(0, [Math]::Min(8, $existingToken.Length)))...$($c.E)"
        Write-Host "$($c.D)  Nhấn Enter để giữ nguyên, hoặc dán token mới:$($c.E)"
    } else {
        Write-Host "$($c.W)  📌 Dán Discord Token của bạn:$($c.E)"
        Write-Host "$($c.D)  (Lấy tại: https://discord.com/developers/applications)$($c.E)"
    }
    Write-Host ""
    $newToken = Read-Host "$($c.G)  Token$($c.E)"
    if ([string]::IsNullOrWhiteSpace($newToken)) { $newToken = $existingToken }

    if ([string]::IsNullOrWhiteSpace($newToken)) {
        Write-Host "$($c.R)  ❌ Token không được để trống!$($c.E)"
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
    Write-Host "$($c.W)  📌 Prefix cho bot (mặc định: .):$($c.E)"
    $newPrefix = Read-Host "$($c.G)  Prefix [$existingPrefix]$($c.E)"
    if ([string]::IsNullOrWhiteSpace($newPrefix)) { $newPrefix = $existingPrefix }

    # Lưu config
    @{ Token = $newToken; Prefix = $newPrefix } | ConvertTo-Json | Set-Content $CONFIG_FILE -Encoding UTF8
    Write-Host ""
    Write-Host "$($c.G)  ✅ Đã lưu config!$($c.E)"

    # Cài dependencies
    Write-Host ""
    Write-Host "$($c.W)  📦 Đang cài thư viện...$($c.E)"
    if (Test-Path "requirements.txt") {
        pip install -r requirements.txt --quiet 2>&1 | Out-Null
        Write-Host "$($c.G)  ✅ Đã cài xong!$($c.E)"
    }

    Start-Sleep -Seconds 1
    return $true
}

# ========================= CHẠY BOT =========================
function Start-Bot {
    $c = @{R="`e[38;2;255;0;0m";G="`e[38;2;0;255;0m";B="`e[38;2;0;170;255m";Y="`e[38;2;255;255;0m";W="`e[38;2;255;255;255m";D="`e[38;2;100;100;100m";E="`e[0m";P="`e[38;2;180;0;255m"}

    if (-not (Test-Path $CONFIG_FILE)) {
        Write-Host "$($c.R)  ❌ Chưa có config! Chọn [2] để cài đặt.$($c.E)"
        Start-Sleep -Seconds 2
        return
    }

    $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
    $env:BOT_TOKEN = $cfg.Token
    $env:DISCORD_TOKEN = $cfg.Token

    Clear-Host
    Write-Host ""
    Write-Host "$($c.P)  ╔═══════════════════════════════════════════╗$($c.E)"
    Write-Host "$($c.P)  ║$($c.E)  $($c.G)🚀 BOT ĐANG CHẠY...$($c.E)                      $($c.P)|$($c.E)"
    Write-Host "$($c.P)  ║$($c.E)  $($c.D)Nhấn Ctrl+C để dừng$($c.E)                   $($c.P)|$($c.E)"
    Write-Host "$($c.P)  ╚═══════════════════════════════════════════╝$($c.E)"
    Write-Host ""

    try {
        python main.py
    } catch {
        Write-Host "$($c.R)  ❌ Lỗi: $_$($c.E)"
        Start-Sleep -Seconds 3
    }
}

# ========================= XEM LOG =========================
function Show-Log {
    Clear-Host
    $c = @{G="`e[38;2;0;255;0m";W="`e[38;2;255;255;255m";D="`e[38;2;100;100;100m";E="`e[0m";P="`e[38;2;180;0;255m"}
    Write-Host "$($c.P)  📊 LOG BOT (Ctrl+C để thoát)$($c.E)"
    Write-Host "$($c.D)  ─────────────────────────────────$($c.E)"

    $cfg = Get-Content $CONFIG_FILE -Raw | ConvertFrom-Json
    $env:BOT_TOKEN = $cfg.Token
    $env:DISCORD_TOKEN = $cfg.Token

    try {
        python main.py 2>&1 | ForEach-Object { Write-Host "$($c.W)  $_$($c.E)" }
    } catch {
        Write-Host "$($c.D)  Log ended.$($c.E)"
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
        $choice = Read-Host "$($c = @{G="`e[38;2;0;255;0m";E="`e[0m"}"$($c.G)  Chọn [0-5]$($c.E)")"

        switch ($choice) {
            "1" { Start-Bot }
            "2" { Start-Setup | Out-Null }
            "3" { Show-Log }
            "4" {
                if (Test-Path $CONFIG_FILE) {
                    notepad $CONFIG_FILE
                } else {
                    Write-Host "$($c.R)  ❌ Chưa có config!$($c.E)"
                    Start-Sleep -Seconds 2
                }
            }
            "5" { explorer.exe "." }
            "0" { $running = $false }
            default {
                Write-Host "$($c.Y)  Chọn sai!$($c.E)"
                Start-Sleep -Seconds 1
            }
        }
    }
}

# ========================= KHỞI CHẠY =========================
# Setup lần đầu nếu chưa có config
if (-not (Test-Path $CONFIG_FILE)) {
    Show-Banner
    Write-Host "$($c = @{G="`e[38;2;0;255;0m";W="`e[38;2;255;255;255m";E="`e[0m"}"  $($c.W)Chào mừng bạn đến với JJK-VVNK Bot!$($c.E)"
    Write-Host "$($c.G)  Bắt đầu cài đặt...$($c.E)"
    Write-Host ""
    Start-Sleep -Seconds 1
    $setupDone = Start-Setup
    if (-not $setupDone) { exit 1 }
}

Main
