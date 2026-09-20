<#
    Sube los commits locales a cherrera0001/MACI leyendo el token desde .env

    USO
      .\push_github.ps1

    Por que existe este script:
    el token se lee del archivo .env, nunca se escribe en la linea de comandos
    y por tanto no queda en el historial de PowerShell. Tampoco se imprime en
    pantalla ni en los mensajes de error.

    .env esta en .gitignore. Verificalo con:  git check-ignore -v .env
#>

$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

# --- Leer .env -----------------------------------------------------------
if (-not (Test-Path '.env')) {
    Write-Host "No existe .env. Copia .env.example a .env y pon tu token." -ForegroundColor Red
    exit 1
}

$vars = @{}
Get-Content '.env' | ForEach-Object {
    $linea = $_.Trim()
    if ($linea -and -not $linea.StartsWith('#') -and $linea.Contains('=')) {
        $i = $linea.IndexOf('=')
        $vars[$linea.Substring(0, $i).Trim()] = $linea.Substring($i + 1).Trim()
    }
}

$usuario = $vars['GITHUB_USER']

# Se prefiere el token clasico (scope 'repo'): los fine-grained requieren
# configurar Repository access y Contents, y por defecto no ven privados.
$token = $null
foreach ($clave in @('GITHUB_TOKEN_CLASIC', 'GITHUB_TOKEN_CLASSIC', 'GITHUB_TOKEN')) {
    if (-not [string]::IsNullOrWhiteSpace($vars[$clave])) {
        $token = $vars[$clave].Trim()
        Write-Host "usando $clave" -ForegroundColor DarkGray
        break
    }
}

if ([string]::IsNullOrWhiteSpace($usuario)) { $usuario = 'cherrera0001' }

if ([string]::IsNullOrWhiteSpace($token)) {
    Write-Host ""
    Write-Host "GITHUB_TOKEN esta vacio en .env" -ForegroundColor Red
    Write-Host ""
    Write-Host "1. Inicia sesion en GitHub como $usuario"
    Write-Host "2. Genera el token en:"
    Write-Host "   https://github.com/settings/tokens/new?scopes=repo"
    Write-Host "3. Pegalo en .env, en la linea GITHUB_TOKEN="
    Write-Host ""
    exit 1
}

# --- Comprobar que el token es de la cuenta correcta ---------------------
Write-Host "Verificando el token..." -NoNewline
try {
    $yo = Invoke-RestMethod -Uri 'https://api.github.com/user' -Headers @{
        Authorization = "Bearer $token"
        'User-Agent'  = 'MACI-push'
    }
} catch {
    Write-Host " FALLO" -ForegroundColor Red
    Write-Host "El token no es valido o esta revocado. Genera uno nuevo." -ForegroundColor Red
    exit 1
}
Write-Host " ok -> $($yo.login)" -ForegroundColor Green

if ($yo.login -ne $usuario) {
    Write-Host ""
    Write-Host "CUIDADO: el token pertenece a '$($yo.login)', no a '$usuario'." -ForegroundColor Yellow
    Write-Host "Este repositorio es personal. Revisa que no estes usando el token laboral." -ForegroundColor Yellow
    exit 1
}

# --- Comprobar acceso al repositorio -------------------------------------
Write-Host "Verificando acceso al repositorio..." -NoNewline
try {
    $repo = Invoke-RestMethod -Uri "https://api.github.com/repos/$usuario/MACI" -Headers @{
        Authorization = "Bearer $token"
        'User-Agent'  = 'MACI-push'
    }
} catch {
    Write-Host " FALLO" -ForegroundColor Red
    Write-Host ""
    if ($token.StartsWith('github_pat_')) {
        Write-Host "El token es FINE-GRAINED y no alcanza a ver el repositorio." -ForegroundColor Yellow
        Write-Host "Estos tokens no usan scopes: requieren configurar al crearlos" -ForegroundColor Yellow
        Write-Host "  Repository access  -> All repositories (o incluir MACI)" -ForegroundColor Yellow
        Write-Host "  Permissions        -> Contents: Read and write" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Mas simple: genera uno CLASICO (empieza con ghp_) en" -ForegroundColor Cyan
        Write-Host "  https://github.com/settings/tokens/new?scopes=repo" -ForegroundColor Cyan
    } else {
        Write-Host "No se ve $usuario/MACI con este token." -ForegroundColor Red
        Write-Host "Revisa que tenga el scope 'repo' y que el repositorio exista." -ForegroundColor Red
    }
    exit 1
}
$vis = if ($repo.private) { 'privado' } else { 'publico' }
Write-Host " ok -> $($repo.full_name) ($vis)" -ForegroundColor Green

if (-not $repo.permissions.push) {
    Write-Host "El token no tiene permiso de escritura. Necesita el scope 'repo'." -ForegroundColor Red
    exit 1
}

# --- Push ----------------------------------------------------------------
# La URL se arma en memoria: el token no pasa por la linea de comandos.
$url = "https://${usuario}:${token}@github.com/$usuario/MACI.git"

Write-Host ""
Write-Host "Subiendo commits..." -ForegroundColor Cyan

# git escribe su progreso en stderr incluso cuando termina bien. Con
# ErrorActionPreference='Stop', PowerShell 5.1 convierte esas lineas en
# NativeCommandError y aborta el script pese a que el push fue correcto.
# Se baja la preferencia solo alrededor de la llamada y se juzga por el
# codigo de salida, que es la unica senal fiable.
$previo = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
$salida = & git push -u $url main 2>&1
$codigo = $LASTEXITCODE
$ErrorActionPreference = $previo

# Nunca imprimir el token si aparece en un mensaje de error.
$salida = $salida -replace [regex]::Escape($token), '***TOKEN***'
$salida | ForEach-Object { Write-Host $_ }

if ($codigo -ne 0) {
    Write-Host ""
    Write-Host "El push fallo (codigo $codigo)." -ForegroundColor Red
    exit $codigo
}

# git push -u con URL explicita no fija el upstream: se hace aparte.
& git branch --set-upstream-to=origin/main main 2>&1 | Out-Null

Write-Host ""
Write-Host "Listo. Commits en https://github.com/$usuario/MACI" -ForegroundColor Green
Write-Host "El remote sigue siendo el normal; el token solo se uso para esta subida." -ForegroundColor DarkGray
