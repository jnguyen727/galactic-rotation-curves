
---

### **docs/data‑dictionary.md**

```markdown
# Data Dictionary

Defines the fields in the SPARC‑derived JSON files under `data/`.

| Field   | Type   | Description                                           |
|---------|--------|-------------------------------------------------------|
| `ID`    | String | Galaxy identifier (e.g. `"NGC2403"`, `"CamB"`)        |
| `D`     | Number | Distance to galaxy (Mpc or kpc—per SPARC metadata)    |
| `R`     | Number | Radius from galactic center (kpc)                     |
| `Vobs`  | Number | Observed rotation speed at `R` (km/s)                 |
| `eVobs` | Number | Uncertainty in `Vobs` (km/s)                          |
| `Vdisk` | Number | Rotation speed contribution from stellar disk (km/s)  |
| `Vgas`  | Number | Rotation speed contribution from gas component (km/s) |
| `Vbul`  | Number | Rotation speed contribution from bulge (km/s)         |
| `SBdisk`| Number | Surface brightness of disk at `R` (mag/arcsec²)       |
| `SBbul` | Number | Surface brightness of bulge at `R` (mag/arcsec²)      |
