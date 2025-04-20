import os
import re
import json

print("Current working directory:", os.getcwd());

# create our regex (dashed lines) for scanning dashes
dash_re = re.compile(r'^-+$')

# store our records to convert to json
records = [];

# loop to iterate over the file and parse each line into json type
with open("/home/johnny/projects/galactic-rotation-curves/galactic-rotation-curves/tmp-sparc/data/MassModels_Lelli2016c.mrt", 'r') as f:
    # -- 1) Skip up until the first dash
    for line in f:
        if dash_re.match(line.strip()):
            break;
    # -- 2) Skip up until the second dash
    for line in f:
        if dash_re.match(line.strip()):
            break;
    # -- 3) Skip up until the third dash
    for line in f:
        if dash_re.match(line.strip()):
            break;
    # -- 4) Skip up until the fourth dash
    for line in f:
        if dash_re.match(line.strip()):
            break;

    # remove trailing space
    data = line.rstrip('\n');
    
    # Parses each line into an array. 
    for line in f:
        # clean now stores the strip of line
        clean = line.strip();
        if not clean:
            continue;
        # splits the line into columns
        cols = clean.split()
        # assign each column a specifier
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
        records.append(record)
print("Successfully read.")

# populates the all_galaxies.json with each galaxy
with open("all_galaxies.json", "w", encoding="utf-8") as out:
    json.dump(records, out, indent=2)

print(f"Wrote {len(records)} records to all_galaxies.json")