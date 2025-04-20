# Project Charter

## Goals
- Build a research‑grade Dark‑Matter Rotation‑Curve simulator in the browser.
- Derive all key formulas from first principles (Kepler’s laws, exponential disk, NFW halo).
- Implement and validate high‑precision integrators (RK4, RKF45, leapfrog).
- Visualize orbits and rotation curves in 3D (React‑Three‑Fiber) and 2D (D3 charts).
- Embed interactive math proofs and documentation via KaTeX.

## Core Deliverables
- `rotationCurve.js` (disk and halo modules) with unit tests.
- Custom React‑Three‑Fiber app with PBR materials, glow effects, and UI controls.
- D3 overlay of observed vs. modeled rotation curves.
- Downloadable PDF of derivations and a technical report/blog series.
- NPM packages for your integrator and orbit‑geometry libraries.

## 4‑Week Sprint Timeline
- **Week 1–2:** Math derivations & core integration code  
- **Week 3:** Disk rotation‑curve implementation & testing  
- **Week 4:** NFW halo module, data integration, and comparative plotting  

*(Weeks 5+ will build on this for 3D viz, docs, outreach, etc.)*

## Key References
- Goldstein, _Classical Mechanics_, Chapter 3 (Kepler’s Laws & Conics)  
- SPARC database or Vera Rubin’s original rotation‑curve data  
- Navarro–Frenk–White, 1996, “The Structure of Cold Dark Matter Halos”  
- Numerical Recipes, Chapter 16 (RK4) & relevant ODE/Num‑Meth texts  
- React‑Three‑Fiber, Drei, and D3 documentation

## Week 1 Goals
- Derive the exponential‑disk rotation formula in KaTeX.  
- Sketch out your numeric integration approach in pseudocode.  
- Fetch and convert a small rotation‑curve dataset into `data/`. 
- Stub out your disk‐curve function file for later implementation.
