import { rotationCurveDisk } from "./rotationCurve";

describe('rotationCurveDisk stub', () => {
    it('returns an array of the same length as its input', () => {
        const radii = [1,2,3];
        const result = rotationCurveDisk(radii, /*Sigma0*/ 1, /*Rd*/ 1);
        expect(Array.isArray(result)).toBe(true);
        expect(result).toHaveLength(radii.length);
    });
});