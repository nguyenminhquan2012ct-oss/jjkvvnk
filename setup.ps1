# ============================================================
#  JJK-VVNK BOT - 1-CLICK INSTALLER
#  Chạy: irm https://raw.githubusercontent.com/nguyenminhquan2012ct-oss/jjkvvnk/main/setup.ps1 | iex
# ============================================================
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Stop"

$ESC = [char]27
$REPO_URL = "https://github.com/nguyenminhquan2012ct-oss/jjkvvnk"
$INSTALL_DIR = "$env:USERPROFILE\JJK-VVNK"

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
    Write-Host "${ESC}[38;2;255;0;0m  ╔═══════════════════════════════════════════════╗${ESC}[0m"
    Write-Host "${ESC}[38;2;255;0;0m  ║${ESC}[0m  ${ESC}[38;2;255;255;255m⚡ JJK-VVNK SELF-BOT v6.0 — 1-CLICK INSTALL${ESC}[0m  ${ESC}[38;2;255;0;0m║${ESC}[0m"
    Write-Host "${ESC}[38;2;255;0;0m  ╚═══════════════════════════════════════════════╝${ESC}[0m"
    Write-Host ""
}

# ========================= KIỂM TRA =========================
function Test-Requirements {
    Write-Host "${ESC}[38;2;0;170;255m  [1/4] Kiểm tra hệ thống...${ESC}[0m"

    # Python
    try {
        $pyVer = python --version 2>&1
        Write-Host "${ESC}[38;2;0;255;0m    ✅ Python: $pyVer${ESC}[0m"
    } catch {
        Write-Host "${ESC}[38;2;255;0;0m    ❌ Python chưa cài! Tải tại: https://python.org${ESC}[0m"
        return $false
    }

    # Git
    try {
        $gitVer = git --version 2>&1
        Write-Host "${ESC}[38;2;0;255;0m    ✅ Git: $gitVer${ESC}[0m"
    } catch {
        Write-Host "${ESC}[38;2;255;255;0m    ⚠️  Git không có (không bắt buộc)${ESC}[0m"
    }

    # pip (dùng python -m pip cho chắc)
    try {
        python -m pip --version 2>&1 | Out-Null
        Write-Host "${ESC}[38;2;0;255;0m    ✅ pip: OK${ESC}[0m"
    } catch {
        Write-Host "${ESC}[38;2;255;0;0m    ❌ pip chưa cài! Đang thử cài pip...${ESC}[0m"
        try {
            python -m ensurepip --upgrade 2>&1 | Out-Null
            Write-Host "${ESC}[38;2;0;255;0m    ✅ Đã cài pip!${ESC}[0m"
        } catch {
            Write-Host "${ESC}[38;2;255;0;0m    ❌ Không thể cài pip. Cài thủ công: python -m ensurepip${ESC}[0m"
            return $false
        }
    }

    return $true
}

# ========================= TẢI BOT =========================
function Install-Bot {
    Write-Host ""
    Write-Host "${ESC}[38;2;0;170;255m  [2/4] Tải bot từ GitHub...${ESC}[0m"

    if (Test-Path $INSTALL_DIR) {
        Write-Host "${ESC}[38;2;255;255;0m    ⚠️  Thư mục đã tồn tại: $INSTALL_DIR${ESC}[0m"
        $overwrite = Read-Host "${ESC}[38;2;255;255;0m    Ghi đè? (y/n)${ESC}[0m"
        if ($overwrite -ne "y") {
            Write-Host "${ESC}[38;2;0;255;0m    Giữ nguyên thư mục cũ.${ESC}[0m"
            return $true
        }
        Remove-Item $INSTALL_DIR -Recurse -Force
    }

    # Thử git clone trước
    try {
        Write-Host "${ESC}[38;2;0;255;0m    📥 Đang clone repo...${ESC}[0m"
        git clone $REPO_URL $INSTALL_DIR 2>&1 | Out-Null
        Write-Host "${ESC}[38;2;0;255;0m    ✅ Đã tải xong!${ESC}[0m"
        return $true
    } catch {
        Write-Host "${ESC}[38;2;255;255;0m    ⚠️  Git clone thất bại, thử tải zip...${ESC}[0m"
    }

    # Fallback: tải zip
    try {
        $zipUrl = "$REPO_URL/archive/refs/heads/main.zip"
        $zipPath = "$env:TEMP\jjk-vvnk.zip"
        Write-Host "${ESC}[38;2;0;255;0m    📥 Đang tải zip...${ESC}[0m"
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
        Invoke-WebRequest -Uri $zipUrl -OutFile $zipPath -UseBasicParsing
        Write-Host "${ESC}[38;2;0;255;0m    📦 Đang giải nén...${ESC}[0m"
        Expand-Archive -Path $zipPath -DestinationPath $env:TEMP -Force
        $extractedDir = Get-ChildItem "$env:TEMP\jjkvvnk-*" -Directory | Select-Object -First 1
        if ($extractedDir) {
            Move-Item $extractedDir.FullName $INSTALL_DIR -Force
        }
        Remove-Item $zipPath -Force
        Write-Host "${ESC}[38;2;0;255;0m    ✅ Đã tải zip xong!${ESC}[0m"
        return $true
    } catch {
        Write-Host "${ESC}[38;2;255;0;0m    ❌ Không thể tải bot: $_${ESC}[0m"
        return $false
    }
}

# ========================= CÀI ĐẶT =========================
function Setup-Bot {
    Write-Host ""
    Write-Host "${ESC}[38;2;0;170;255m  [3/4] Cài đặt dependencies...${ESC}[0m"
    Set-Location $INSTALL_DIR

    if (Test-Path "requirements.txt") {
        Write-Host "${ESC}[38;2;255;255;0m    📦 Đang cài... (có thể mất 1-2 phút)${ESC}[0m"
        try {
            python -m pip install -r requirements.txt --quiet 2>&1 | Out-Null
            Write-Host "${ESC}[38;2;0;255;0m    ✅ Đã cài xong dependencies!${ESC}[0m"
        } catch {
            Write-Host "${ESC}[38;2;255;255;0m    ⚠️  Một số thư viện chưa cài được, thử lại...${ESC}[0m"
            python -m pip install -r requirements.txt 2>&1
        }
    } else {
        Write-Host "${ESC}[38;2;255;255;0m    ⚠️  Không tìm thấy requirements.txt${ESC}[0m"
    }
}

# ========================= CONFIG =========================
function Set-Config {
    Write-Host ""
    Write-Host "${ESC}[38;2;0;170;255m  [4/4] Cấu hình bot...${ESC}[0m"

    $configFile = "$INSTALL_DIR\config.json"

    Write-Host ""
    Write-Host "${ESC}[38;2;255;255;255m  📌 Dán Discord Token của bạn:${ESC}[0m"
    Write-Host "${ESC}[38;2;100;100;100m  (Lấy tại: https://discord.com/developers/applications)${ESC}[0m"
    Write-Host ""
    $token = Read-Host "${ESC}[38;2;0;255;0m  Token${ESC}[0m"

    if ([string]::IsNullOrWhiteSpace($token)) {
        Write-Host "${ESC}[38;2;255;0;0m  ❌ Token không được trống!${ESC}[0m"
        return $false
    }

    Write-Host ""
    Write-Host "${ESC}[38;2;255;255;255m  📌 Prefix cho bot (Enter = .):${ESC}[0m"
    $prefix = Read-Host "${ESC}[38;2;0;255;0m  Prefix${ESC}[0m"
    if ([string]::IsNullOrWhiteSpace($prefix)) { $prefix = "." }

    @{ Token = $token; Prefix = $prefix } | ConvertTo-Json | Set-Content $configFile -Encoding UTF8
    Write-Host ""
    Write-Host "${ESC}[38;2;0;255;0m  ✅ Đã lưu config!${ESC}[0m"
    return $true
}

# ========================= HOÀN TẤT =========================
function Show-Done {
    Write-Host ""
    Write-Host "${ESC}[38;2;255;0;0m  ╔═══════════════════════════════════════════════╗${ESC}[0m"
    Write-Host "${ESC}[38;2;255;0;0m  ║${ESC}[0m  ${ESC}[38;2;0;255;0m✅ CÀI ĐẶT HOÀN TẤT!${ESC}[0m                      ${ESC}[38;2;255;0;0m║${ESC}[0m"
    Write-Host "${ESC}[38;2;255;0;0m  ╚═══════════════════════════════════════════════╝${ESC}[0m"
    Write-Host ""
    Write-Host "${ESC}[38;2;255;255;255m  📁 Thư mục bot: $INSTALL_DIR${ESC}[0m"
    Write-Host ""
    Write-Host "${ESC}[38;2;0;170;255m  🚀 CÁCH CHẠY:${ESC}[0m"
    Write-Host "${ESC}[38;2;255;255;255m     1. Double-click ${ESC}[38;2;0;255;0mJJK-VVNK.bat${ESC}[0m${ESC}[38;2;255;255;255m trong thư mục bot${ESC}[0m"
    Write-Host "${ESC}[38;2;255;255;255m     2. Hoặc chạy: ${ESC}[38;2;0;255;0mpowershell -ExecutionPolicy Bypass -File launch.ps1${ESC}[0m"
    Write-Host ""

    $runNow = Read-Host "${ESC}[38;2;0;255;0m  Chạy bot ngay? (y/n)${ESC}[0m"
    if ($runNow -eq "y") {
        Set-Location $INSTALL_DIR
        $cfg = Get-Content "config.json" -Raw | ConvertFrom-Json
        $env:BOT_TOKEN = $cfg.Token
        $env:DISCORD_TOKEN = $cfg.Token
        Write-Host ""
        Write-Host "${ESC}[38;2;0;255;0m  🚀 Đang khởi động bot...${ESC}[0m"
        Write-Host ""
        python main.py
    }
}

# ========================= MAIN =========================
Show-Banner

if (-not (Test-Requirements)) {
    Write-Host ""
    Read-Host "${ESC}[38;2;255;0;0m  Nhấn Enter để thoát${ESC}[0m"
    exit 1
}

if (-not (Install-Bot)) {
    Write-Host ""
    Read-Host "${ESC}[38;2;255;0;0m  Nhấn Enter để thoát${ESC}[0m"
    exit 1
}

Setup-Bot
Set-Config | Out-Null
Show-Done
