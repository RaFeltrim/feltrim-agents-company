<#
.SYNOPSIS
    Espelho LOCAL (PowerShell) do job `flag-words-check` em .github/workflows/ci.yml.

.DESCRIPTION
    Equivalente PowerShell do scripts/check-flag-words.sh, para usuarios Windows
    que preferem nao instalar Git Bash. O pre-commit ainda usa o .sh por
    portabilidade, mas este script existe para invocacao manual rapida:

        pwsh scripts/check-flag-words.ps1
        powershell -File scripts/check-flag-words.ps1

    Em divergencia entre este script e o CI, o CI eh a fonte de verdade.
    Mantenha as 4 checagens sincronizadas com .github/workflows/ci.yml.

.NOTES
    Requer ripgrep (rg) no PATH. Instale com:
        choco install ripgrep
        winget install BurntSushi.ripgrep.MSVC
#>

$ErrorActionPreference = "Stop"
$fail = 0

function Write-Fail($msg)  { Write-Host "FAIL: $msg" -ForegroundColor Red }
function Write-Pass($msg)  { Write-Host "OK:   $msg" -ForegroundColor Green }
function Write-Warn2($msg) { Write-Host "WARN: $msg" -ForegroundColor Yellow }

if (-not (Get-Command rg -ErrorAction SilentlyContinue)) {
    Write-Warn2 "ripgrep (rg) nao encontrado no PATH - skipping flag-words-check local."
    Write-Host "       Instale: choco install ripgrep   ou   winget install BurntSushi.ripgrep.MSVC"
    Write-Host "       O CI vai rodar essa checagem no push de qualquer forma."
    exit 0
}

# -----------------------------------------------------------------------------
# Check 1 - Caminhos absolutos
# -----------------------------------------------------------------------------
Write-Host "[1/4] Checking absolute paths..."

$searchPaths = @()
foreach ($p in @("core","governance","examples","docs","packs",
                 "README.md","CONTRIBUTING.md","CODE_OF_CONDUCT.md",
                 "SECURITY.md","CHANGELOG.md","CLAUDE.md","AGENTS.md","LICENSE")) {
    if (Test-Path $p) { $searchPaths += $p }
}

if ($searchPaths.Count -gt 0) {
    $rgArgs = @(
        "-i",
        "(C:\\Users\\[A-Za-z]+|/Users/[A-Za-z]+/|~/Desktop)"
    ) + $searchPaths + @(
        "--glob","!**/CHANGELOG.md",
        "--glob","!**/README.md",
        "--glob","!*.lock",
        "--glob","!scripts/check-flag-words.sh",
        "--glob","!scripts/check-flag-words.ps1"
    )
    $output = & rg @rgArgs 2>$null
    if ($LASTEXITCODE -eq 0 -and $output) {
        Write-Fail "absolute paths found:"
        $output | ForEach-Object { Write-Host "  $_" }
        $fail = 1
    }
}

# -----------------------------------------------------------------------------
# Check 2 - .env real commitado
# -----------------------------------------------------------------------------
Write-Host "[2/4] Checking committed .env files..."
$envFiles = git ls-files 2>$null | Where-Object {
    ($_ -match '^\.env$' -or $_ -match '^\.env\.[a-z]+$') -and $_ -ne '.env.example'
}
if ($envFiles) {
    Write-Fail "real .env file(s) commitado:"
    $envFiles | ForEach-Object { Write-Host "  $_" }
    $fail = 1
}

# -----------------------------------------------------------------------------
# Check 3 - Secrets
# -----------------------------------------------------------------------------
Write-Host "[3/4] Checking for likely secrets..."
$rgSecretArgs = @(
    "-i",
    "(api[_-]?key|token|password|secret)\s*[:=]\s*['""][A-Za-z0-9_-]{20,}",
    "--type-not","lock",
    "--glob","!**/CHANGELOG.md",
    "--glob","!**/SECURITY.md",
    "--glob","!**/SECURITY_AND_PRIVACY.md",
    "--glob","!**/.github/**",
    "--glob","!**/.env.example",
    "--glob","!scripts/check-flag-words.sh",
    "--glob","!scripts/check-flag-words.ps1"
)
$secretOutput = & rg @rgSecretArgs 2>$null
if ($LASTEXITCODE -eq 0 -and $secretOutput) {
    Write-Fail "likely secret commitado:"
    $secretOutput | ForEach-Object { Write-Host "  $_" }
    $fail = 1
}

# -----------------------------------------------------------------------------
# Check 4 - Committer email policy
# -----------------------------------------------------------------------------
Write-Host "[4/4] Checking committer email policy..."
$emails = git log -10 --format="%ae" 2>$null
$badEmails = $emails | Where-Object {
    $_ -and `
    $_ -notmatch '^[^@]+@users\.noreply\.github\.com$' -and `
    $_ -notmatch '^[^@]+@noreply\.github\.com$'
} | Sort-Object -Unique

if ($badEmails) {
    Write-Warn2 "commits encontrados com email fora da allowlist:"
    $badEmails | ForEach-Object { Write-Host "  $_" }
    Write-Host ""
    Write-Host "Configure git local com:"
    Write-Host "  git config user.email '<seu-user>@users.noreply.github.com'"
    Write-Host ""
    Write-Host "(NAO bloqueando o commit local - mas o CI vai bloquear o push.)"
}

# -----------------------------------------------------------------------------
if ($fail -eq 0) {
    Write-Pass "flag-words-check passou."
    exit 0
} else {
    Write-Fail "flag-words-check encontrou problemas. Corrija e tente de novo."
    exit 1
}
