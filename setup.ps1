# ============================================================
#  JJK-VVNK BOT - 1-CLICK INSTALLER
#  Chạy: irm https://raw.githubusercontent.com/nguyenminhquan2012ct-oss/jjkvvnk/main/setup.ps1 | iex
# ============================================================
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Stop"

$REPO_URL = "https://github.com/nguyenminhquan2012ct-oss/jjkvvnk"
$INSTALL_DIR = "$env:USERPROFILE\JJK-VVNK"

# ========================= BANNER =========================
function Show-Banner {
    Clear-Host
    Write-Host ""
    Write-Host "`e[38;2;180;0;255m        ___           _           _       `e[38;2;100;100;100mQU4N.TH3.D3V`e[0m"
    Write-Host "`e[38;2;180;0;255m       / (_)___ _ __ | |__  _   _| |_ ___ `e[0m"
    Write-Host "`e[38;2;180;0;255m      / /| / __| '_ \| '_ \| | | | __/ _ \`e[0m"
    Write-Host "`e[38;2;180;0;255m     / / | \__ \ |_) | |_) | |_| | ||  __/ `e[0m"
    Write-Host "`e[38;2;180;0;255m    /_/  |_|___/ .__/|_.__/ \__, |\__\___| `e[0m"
    Write-Host "`e[38;2;180;0;255m              |_|          |___/          `e[0m"
    Write-Host ""
    Write-Host "`e[38;2;255;0;0m  ╔═══════════════════════════════════════════════╗`e[0m"
    Write-Host "`e[38;2;255;0;0m  ║`e[0m  `e[38;2;255;255;255m⚡ JJK-VVNK SELF-BOT v6.0 — 1-CLICK INSTALL`e[0m  `e[38;2;255;0;0m║`e[0m"
    Write-Host "`e[38;2;255;0;0m  ╚═══════════════════════════════════════════════╝`e[0m"
    Write-Host ""
}

# ========================= KIỂM TRA =========================
function Test-Requirements {
    Write-Host "`e[38;2;0;170;255m  [1/4] Kiểm tra hệ thống...`e[0m"

    # Python
    try {
        $pyVer = python --version 2>&1
        Write-Host "`e[38;2;0;255;0m    ✅ Python: $pyVer`e[0m"
    } catch {
        Write-Host "`e[38;2;255;0;0m    ❌ Python chưa cài! Tải tại: https://python.org`e[0m"
        return $false
    }

    # Git
    try {
        $gitVer = git --version 2>&1
        Write-Host "`e[38;2;0;255;0m    ✅ Git: $gitVer`e[0m"
    } catch {
        Write-Host "`e[38;2;255;255;0m    ⚠️  Git không có (không bắt buộc)`e[0m"
    }

    # pip
    try {
        pip --version 2>&1 | Out-Null
        Write-Host "`e[38;2;0;255;0m    ✅ pip: OK`e[0m"
    } catch {
        Write-Host "`e[38;2;255;0;0m    ❌ pip chưa cài!`e[0m"
        return $false
    }

    return $true
}

# ========================= TẢI BOT =========================
function Install-Bot {
    Write-Host ""
    Write-Host "`e[38;2;0;170;255m  [2/4] Tải bot từ GitHub...`e[0m"

    if (Test-Path $INSTALL_DIR) {
        Write-Host "`e[38;2;255;255;0m    ⚠️  Thư mục đã tồn tại: $INSTALL_DIR`e[0m"
        $overwrite = Read-Host "`e[38;2;255;255;0m    Ghi đè? (y/n)$`e[0m"
        if ($overwrite -ne "y") {
            Write-Host "`e[38;2;0;255;0m    Giữ nguyên thư mục cũ.`e[0m"
            return $true
        }
        Remove-Item $INSTALL_DIR -Recurse -Force
    }

    try {
        Write-Host "`e[38;2;0;255;0m    📥 Đang clone repo...`e[0m"
        git clone $REPO_URL $INSTALL_DIR 2>&1 | Out-Null
        Write-Host "`e[38;2;0;255;0m    ✅ Đã tải xong!`e[0m"
        return $true
    } catch {
        Write-Host "`e[38;2;255;0;0m    ❌ Lỗi clone. Thử tải zip...`e[0m"
        try {
            $zipUrl = "$REPO_URL/archive/refs/heads/main.zip"
            $zipPath = "$env:TEMP\jjk-vvnk.zip"
            Invoke-WebRequest -Uri $zipUrl -OutFile $zipPath
            Expand-Archive -Path $zipPath -DestinationPath $env:TEMP -Force
            Move-Item "$env:TEMP\jjkvvnk-main" $INSTALL_DIR -Force
            Remove-Item $zipPath -Force
            Write-Host "`e[38;2;0;255;0m    ✅ Đã tải zip xong!`e[0m"
            return $true
        } catch {
            Write-Host "`e[38;2;255;0;0m    ❌ Không thể tải bot: $_`e[0m"
            return $false
        }
    }
}

# ========================= CÀI ĐẶT =========================
function Setup-Bot {
    Write-Host ""
    Write-Host "`e[38;2;0;170;255m  [3/4] Cài đặt dependencies...`e[0m"
    Set-Location $INSTALL_DIR

    try {
        pip install -r requirements.txt --quiet 2>&1 | Out-Null
        Write-Host "`e[38;2;0;255;0m    ✅ Đã cài xong dependencies!`e[0m"
    } catch {
        Write-Host "`e[38;2;255;255;0m    ⚠️  Một số thư viện có thể chưa cài được`e[0m"
    }
}

# ========================= CONFIG =========================
function Set-Config {
    Write-Host ""
    Write-Host "`e[38;2;0;170;255m  [4/4] Cấu hình bot...`e[0m"

    $configFile = "$INSTALL_DIR\config.json"

    Write-Host ""
    Write-Host "`e[38;2;255;255;255m  📌 Dán Discord Token của bạn:`e[0m"
    Write-Host "`e[38;2;100;100;100m  (Lấy tại: https://discord.com/developers/applications)`e[0m"
    Write-Host ""
    $token = Read-Host "`e[38;2;0;255;0m  Token`e[0m"

    if ([string]::IsNullOrWhiteSpace($token)) {
        Write-Host "`e[38;2;255;0;0m  ❌ Token không được trống!`e[0m"
        return $false
    }

    Write-Host ""
    Write-Host "`e[38;2;255;255;255m  📌 Prefix cho bot (Enter = .):`e[0m"
    $prefix = Read-Host "`e[38;2;0;255;0m  Prefix`e[0m"
    if ([string]::IsNullOrWhiteSpace($prefix)) { $prefix = "." }

    @{ Token = $token; Prefix = $prefix } | ConvertTo-Json | Set-Content $configFile -Encoding UTF8
    Write-Host ""
    Write-Host "`e[38;2;0;255;0m  ✅ Đã lưu config!`e[0m"
    return $true
}

# ========================= HOÀN TẤT =========================
function Show-Done {
    Write-Host ""
    Write-Host "`e[38;2;255;0;0m  ╔═══════════════════════════════════════════════╗`e[0m"
    Write-Host "`e[38;2;255;0;0m  ║`e[0m  `e[38;2;0;255;0m✅ CÀI ĐẶT HOÀN TẤT!`e[0m                      `e[38;2;255;0;0m║`e[0m"
    Write-Host "`e[38;2;255;0;0m  ╚═══════════════════════════════════════════════╝`e[0m"
    Write-Host ""
    Write-Host "`e[38;2;255;255;255m  📁 Thư mục bot: $INSTALL_DIR`e[0m"
    Write-Host ""
    Write-Host "`e[38;2;0;170;255m  🚀 CÁCH CHẠY:`e[0m"
    Write-Host "`e[38;2;255;255;255m     1. Mở PowerShell`e[0m"
    Write-Host "`e[38;2;255;255;255m     2. cd $INSTALL_DIR`e[0m"
    Write-Host "`e[38;2;255;255;255m     3. .\launch.ps1`e[0m"
    Write-Host ""
    Write-Host "`e[38;2;255;255;255m  Hoặc双击 file `e[38;2;0;255;0mJJK-VVNK.bat`e[0m`e[38;2;255;255;255m trong thư mục bot`e[0m"
    Write-Host ""

    $runNow = Read-Host "`e[38;2;0;255;0m  Chạy bot ngay? (y/n)$`e[0m"
    if ($runNow -eq "y") {
        Set-Location $INSTALL_DIR
        $cfg = Get-Content "config.json" -Raw | ConvertFrom-Json
        $env:BOT_TOKEN = $cfg.Token
        $env:DISCORD_TOKEN = $cfg.Token
        Write-Host ""
        Write-Host "`e[38;2;0;255;0m  🚀 Đang khởi động bot...`e[0m"
        Write-Host ""
        python main.py
    }
}

# ========================= MAIN =========================
Show-Banner

if (-not (Test-Requirements)) {
    Write-Host ""
    Read-Host "`e[38;2;255;0;0m  Nhấn Enter để thoát`e[0m"
    exit 1
}

if (-not (Install-Bot)) {
    Write-Host ""
    Read-Host "`e[38;2;255;0;0m  Nhấn Enter để thoát`e[0m"
    exit 1
}

Setup-Bot
Set-Config | Out-Null
Show-Done
