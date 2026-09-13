# Netanya Surf & SUP

**Live page:** https://cdn.jsdelivr.net/gh/golosovsky/netanya-surf-dashboard@master/index.html

Repo: https://github.com/golosovsky/netanya-surf-dashboard Dashboard

Ultra-minimal static web app for Eli Golosovsky’s Netanya (Israel) softboard (~7 ft) and SUP decisions.

## Thresholds (hard)

| Board | Rule |
|-------|------|
| **Surf** (softboard) | significant wave height **≥ 60 cm** |
| **SUP** | significant wave height **≤ 20 cm** |
| **Neither** | ~21–59 cm — flat for softboard / too choppy for SUP |

## Daily recommendation rule

- Timezone: **Asia/Jerusalem**
- Daytime window: **07:00–18:00** local (inclusive)
- Representative height: **median** of daytime hourly `wave_height` values
- Display and thresholds use **centimetres** (API returns metres × 100)
- City callouts (Today / Tomorrow) use the **median across beaches** of each beach’s daytime median
- Per-beach row shows today’s daytime median (and a tomorrow hint)

## Beaches

Poleg, Sironit, Kontiki / Amphi, Herzl Beach, Blue Bay, Hasharon — approx. coastal coords. Nearby spots often share one Open-Meteo marine grid cell; the app still lists each name and fetches once per unique ~0.01° cell.

## Data

- [Open-Meteo Marine API](https://marine-api.open-meteo.com/v1/marine) — `models=ncep_gfswave016`
- Hourly: `wave_height`, `wave_period`, `wave_direction`
- Optional wind from Open-Meteo Forecast API
- Client-side `fetch`; last good payload cached in `localStorage`

## Local serve

```bash
cd /workspace/netanya-surf-dashboard
python3 -m http.server 8765
```

Open http://127.0.0.1:8765/

## Deploy (GitHub Pages)

Drop this folder as the Pages root (or copy `index.html` into `/docs`). No build step.

## Threshold unit checks

```bash
python3 test_thresholds.py
```

See `VERIFY.md` for live API and Surf-Forecast cross-checks.
