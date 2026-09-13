# Verification — Netanya Surf & SUP Dashboard

Date of checks: **2026-09-13** (Asia/Jerusalem evening / UTC afternoon).

## 1. Open-Meteo Marine API (live curl)

Endpoint: `https://marine-api.open-meteo.com/v1/marine`  
Params: `models=ncep_gfswave016`, `hourly=wave_height,wave_period,wave_direction`, `timezone=Asia/Jerusalem`, `forecast_days=3`.

| Spot | Request lat/lon | Returned grid | Null heights | Daytime median (07–18) |
|------|-----------------|---------------|--------------|------------------------|
| Poleg | 32.27, 34.83 | 32.333336, 34.833344 | **0 / 72** | **~44 cm** (Sun 13) |
| Sironit | 32.32, 34.85 | 32.333336, 34.833344 | **0 / 72** | **~44 cm** (Sun 13) |

Both coastal request points resolve to the **same NCEP GFS Wave 0.16° cell**. Heights are non-null throughout the 3-day hourly series. Range observed: **0.44–0.58 m** (~44–58 cm).

Tomorrow (Mon 14) daytime median ≈ **46 cm**; Tue 15 ≈ **50 cm**.

## 2. Cross-check vs Surf-Forecast

Sources fetched 2026-09-13:

- [Netanya (Poleg) 48h](https://www.surf-forecast.com/breaks/Netanya/forecasts/latest)
- [Sironit Beach 48h](https://www.surf-forecast.com/breaks/Sironit-Beach/forecasts/latest)

| Source | Today (13 Sep) height | Period | Direction |
|--------|----------------------|--------|-----------|
| Surf-Forecast Poleg | **0.4 m** (1.5 ft) afternoon/evening | **5 s** | WNW |
| Surf-Forecast Sironit | **0.4 m** (1.5 ft) afternoon/evening | **5 s** | WNW |
| Open-Meteo (this app) | **~0.44–0.48 m** daytime | **~5.3 s** | WNW-ish |

**Agreement:** same ballpark (~0.4 m), same short ~5 s WNW windswell, rating 0 on Surf-Forecast (not surfable). Open-Meteo sits slightly higher (~5–10 cm) than Surf-Forecast’s rounded 0.4 m — expected model / product differences. **Order-of-magnitude match: yes.**

## 3. Threshold logic unit test

```bash
python3 test_thresholds.py
```

Results:

- 10 cm → SUP  
- 40 cm → Neither  
- 70 cm → Surf  
- Boundaries: 20 → SUP, 21 → Neither, 59 → Neither, 60 → Surf  

All assertions passed.

## 4. Local serve

```bash
cd /workspace/netanya-surf-dashboard && python3 -m http.server 8765
```

`index.html` served successfully; page loads and fetches live marine data in the browser.

## Live recommendation snapshot (from API at verify time)

Using daytime median ≥60 Surf / ≤20 SUP:

- **Today (Sun 13):** ~44 cm → **Neither** — flat for softboard / too choppy for SUP  
- **Tomorrow (Mon 14):** ~46 cm → **Neither** — same vibe  

No “great surfing” or “great SUP” heads-up for these two days under Eli’s thresholds.

## 5. Screenshot

Headless Chrome mobile viewport (390×844): `screenshot-mobile.png` — live data rendered; Today/Tomorrow Neither callouts (~44 / ~46 cm); beach list with badges.
