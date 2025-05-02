/*
 * Compute the disk-only rotation speeds at each radius.
 * @param {number[]} radii - array of r values
 * @param {number} Sigma0 - central surface density
 * @param {number} Rd - scale length
 * @returns {number[]} diskSpeeds - placeholder array (same length as radii)
 */

export function rotationCurveDisk(radii, Sigma0, Rd) {
  // TODO: replace placeholder with numeric integration
  let length = radii.length;
  const diskSpeeds = new Array(length).fill(0);
  for (let i = 0; i < radii.length; i++) {
    let radius = radii[i];
    let N = 100;
    let midpoint = radius / N;
    let sum = 0;
    const eulerNumber = Math.E;
    const pi = Math.PI;
    const G = 4.3009e-6;
    for (let i = 0; i < N; i++) {
      let r_k = (i + 1/2) * midpoint;
      sum += ((2 * pi) * Sigma0 * Math.pow(eulerNumber, (-r_k / Rd)) * (r_k * midpoint));
    }
    let disk = Math.sqrt((G * sum) / radius);
    diskSpeeds[i] = disk;
  }
  return diskSpeeds;
}