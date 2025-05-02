import { rotationCurveDisk } from "./rotationCurve";

// 1. Group tests under a named suite:
describe('rotationCurveDisk stub', () => {
    // 2. One test case, described in English
    it('returns an array of the same length as its input', () => {
        const radii = [1,2,3];
        // 3. Call the function under test:
        const result = rotationCurveDisk(radii, /*Sigma0*/ 1, /*Rd*/ 1);
        // 4. Assert expectations about the result.
        expect(Array.isArray(result)).toBe(true);
        expect(result).toHaveLength(radii.length);
    });
 //   it('initially returns all zeros', () => {
 //       const radii = [0.5, 1.0, 2.0];
 //       const result = rotationCurveDisk(radii, 10, 5);
 //       // until i replace this stub guarantee me that i have zeroes
 //       expect(result).toEqual([0, 0, 0]);
 //   });
    it('matches analytic constant-density speeds within 1%', () => {
        const radii = [1, 2, 3];
        const Sigma0 = 1;
        const Rd = 1e6;
        const result = rotationCurveDisk(radii, Sigma0, Rd);

        const expected = [0.00366, 0.00518, 0.00634];
        expected.forEach((vExp, i) => {
            const vComp = result[i];
            const relError = Math.abs((vComp - vExp) / vExp);
            expect(relError).toBeLessThan(0.01);
        });
    });
});