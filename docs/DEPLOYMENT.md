# Deployment: MACI en maci.c4a.cl

**Estado:** Dominio agregado a Vercel ✅ | DNS pendiente ⏳

## Arquitectura

```
GitHub (cherrera0001/MACI)
        ↓
    Vercel (maci project)
        ↓
    maci.c4a.cl (Cloudflare DNS)
        ↓
    Usuario navegador
```

## Configuración Realizada

### 1. Vercel (✅ Completado)

- **Proyecto:** maci (prj_lLD3lhsfxwbQFI1Q0fQB8twAunVe)
- **Dominio actual:** maci-rose.vercel.app
- **Dominio personalizado agregado:** maci.c4a.cl
- **Estado:** Verificado en Vercel, esperando DNS

### 2. Cloudflare DNS (⏳ Pendiente)

**Registro requerido:**
```
Tipo:    CNAME
Nombre:  maci
Apunta:  cname.vercel.app
TTL:     Auto (0)
Proxy:   DNS only (gris)
```

**Pasos para crear el registro:**

1. Accede a Cloudflare Dashboard: https://dash.cloudflare.com/
2. Selecciona dominio: c4a.cl
3. Ve a: DNS → Records
4. Click "Add record"
5. Rellena:
   - Type: CNAME
   - Name: maci
   - Content: cname.vercel.app
   - TTL: Auto
   - Proxy status: DNS only
6. Save

## Verificación

Después de crear el registro en Cloudflare (puede tardar 5-15 minutos):

```bash
# Verificar propagación DNS
nslookup maci.c4a.cl

# Verificar CNAME
dig maci.c4a.cl CNAME

# Probar acceso HTTPS
curl -I https://maci.c4a.cl

# Debería devolver:
# HTTP/2 200
# Content-Type: text/html
```

## Automatización (opcional)

Si tienes API token de Cloudflare:

```bash
# 1. Copiar archivo de configuración
cp .env.cloudflare.example .env.cloudflare

# 2. Editar .env.cloudflare con tus credenciales
# Obtenidas en https://dash.cloudflare.com/profile/api-tokens

# 3. Ejecutar script
bash 03_SCRIPTS/setup_cloudflare_dns.sh
```

## Flujo de Deploy

Cuando empujas a main:

```
git push origin main
        ↓
    GitHub Webhook
        ↓
    Vercel CI/CD
        ↓
    Build: npm/python tests
        ↓
    Deploy to maci-rose.vercel.app
        ↓
    Alias: maci.c4a.cl (después de DNS)
```

## Direcciones Activas

- **De desarrollo:** maci-rose.vercel.app
- **De producción:** maci.c4a.cl (después de DNS)
- **Git:** https://github.com/cherrera0001/MACI (main branch)

## Rollback

Si hay problemas:

1. DNS still pointing to maci-rose.vercel.app (sin cambios a c4a.cl)
2. Vercel project tiene historial de deployments
3. Puedes revertir en GitHub (git revert commit_hash)

## Monitoreo

- Vercel Dashboard: https://vercel.com/cherrera0001/maci
- Cloudflare Dashboard: https://dash.cloudflare.com/ (c4a.cl)
- Logs: `git log --oneline --graph`

---

**Última actualización:** 2026-09-27  
**Responsable:** Claude Code + Vercel + Cloudflare
