import os
import re
import json

dash_re = re.compile(r'^-+$')

with open("/home/johnny/projects/galactic-rotation-curves/galactic-rotation-curves/tmp-sparc/data/MassModels_Lelli2016c.mrt", 'r') as f:
    # Break until we get to the data, (four strips of dashes)
    for line in f:
        if dash_re.match(line.strip()):
            break;
    for line in f:
        if dash_re.match(line.strip()):
            break;
    for line in f:
        if dash_re.match(line.strip()):
            break;
    for line in f:
        if dash_re.match(line.strip()):
            break;

    # now for each line, write a tiny JSON file for each galaxy
    for i, line in enumerate(f):
        clean = line.strip()
        if not clean:
            continue

        # split the column up into categories for each galaxy...
        cols = clean.split()
        record = {
            "ID":   cols[0],
            "D":    float(cols[1]),
            "R":    float(cols[2]),
            "Vobs": float(cols[3]),
            "eVobs":float(cols[4]),
            "Vgas": float(cols[5]),
            "Vdisk":float(cols[6]),
            "Vbul": float(cols[7]),
            "SBdisk":float(cols[8]),
            "SBbul":float(cols[9]),
        }
        # set the filename to be galaxy_name.json
        fname = f"{record['ID']}.json"

        # open the file, then write the json into it.
        with open(fname, "w", encoding="utf-8") as out:
            json.dump(record, out, indent=2)
        
        # print statement to ensure successfuly name write
        print(f"Wrote {fname} successfully!")

