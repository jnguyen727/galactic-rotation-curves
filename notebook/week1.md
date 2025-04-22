# Week 1: Exponential-Disk Rotation Curve

$$ 
v_{\rm disk}(r)
= \sqrt{\frac{G}{r}
    \int_{0}^{r} 2\pi\,\Sigma_{0}\,e^{-r'/R_{d}}\,r'\,dr'
  }.
$$

**Notation:**
- \(G\): Gravitational constant  
- \(r\): Radius from galactic center (kpc)  
- \(\Sigma_{0}\): Central surface density of the stellar disk (M☉/pc²)  
- \(R_{d}\): Scale length of the exponential disk (kpc)  

## Pseudocode for Numeric Integration

1. Input: array of radii \([r_1, r_2, …]\), constants \(\Sigma_0, R_d\).  
2. For each \(r_i\):  
   - Divide \([0, r_i]\) into \(N\) small steps \(\Delta r\).  
   - Compute sum = \(\sum_{k=0}^{N-1} 2\pi \Sigma_0 e^{-r_k/R_d}\,r_k\,\Delta r\).  
   - Set \(v_{\rm disk}(r_i) = \sqrt{G \cdot (\text{sum})/r_i}\).  
3. Return array \([v_{\rm disk}(r_1), v_{\rm disk}(r_2), …]\).

## Textbook Exercises

- **Arfken & Weber** §1–3, Problem 2: Verify the dot‑product identity for rotated vectors.  
- **Goldstein** Ch 3, Problem 4: Derive the specific energy for an elliptical orbit.  
- **Optional:** Kleppner & Kolenkow App A, Problem 1: Solve \(d^2u/d\theta^2 + u = GM/h^2\).
