# Galactic Rotation Curves Simulator

An interactive 3D web app for exploring galactic rotation curves and the evidence for dark matter.  
Built with React‑Three‑Fiber, D3, and KaTeX.
Current work in progress.

---

## Demo

WIP

---

## Table of Contents

- [Installation](#installation)  
- [Usage](#usage)  
- [Data Sources](#data-sources)  
- [Roadmap](#roadmap)  
- [Contributing](#contributing)  
- [License](#license)

---

## Installation

```bash
git clone https://github.com/your-username/galactic-rotation-curves.git
cd galactic-rotation-curves
npm install
npm start

The app will be available at http://localhost:3000.
```
## Usage

    Select a galaxy from the dropdown to load its observed rotation‑curve data.

    Adjust disk mass and halo parameters via the control panel.

    View synchronized 3D orbits and 2D D3 rotation‑curve plots.

    Toggle “Visible‑only” vs. “+ Dark Halo” modes to see how dark matter flattens the curve.

    Open “Scholar Mode” for live KaTeX derivations and code snippets.

## Data Sources

All observational data come from the SPARC (Spitzer Photometry & Accurate Rotation Curves) mass‑model release (Lelli et al. 2016).
Parsed JSON lives in data/:

    all_galaxies.json — combined dataset for all supported galaxies

    NGC2403.json, UGC05721.json, etc. — per‑galaxy arrays of radius & velocity measurements

See docs/data‑dictionary.md for field definitions.
## Roadmap

A full 20‑week plan lives in ROADMAP.md (or link to your LaTeX/PDF).
Weekly notebooks are in /notebook.

## Contributing

See CONTRIBUTING.md.

## License

This project is licensed under the MIT License — see LICENSE.md for details.
