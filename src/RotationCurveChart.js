import { rotationCurveDisk } from "./rotationCurve";
import allData from '../data/all_galaxies/all_galaxies.json';

const galaxy = 'NGC2403';
const points = allData.filter(p => p.ID === galaxy);
const radii = points.map(p => p.R);
const obsSpeeds = points.map(p => p.Vobs);