import os
import re
import json

print("Current working directory:", os.getcwd());

dash_re = re.compile(r'^-+$')
records = [];

with open("/home/johnny/projects/galactic-rotation-curves/galactic-rotation-curves/tmp-sparc/data/MassModels_Lelli2016c.mrt", 'r') as f:
    # -- 1) Skip up until the first dash
    for line in f:
        if dash_re.match(line.strip()):
            break;
    # -- 2) Skip up until the second dash
    for line in f:
        if dash_re.match(line.strip()):
            break;
    for line in f:
        if dash_re.match(line.strip()):
            break;
    for line in f:
        if dash_re.match(line.strip()):
            break;

    data = line.rstrip('\n');
    
    # Parses each line into an array. 
    for line in f:
        clean = line.strip();
        if not clean:
            continue;
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
        records.append(record)
        print(cols)
print("Successfully read.")

with open("all_galaxies.json", "w", encoding="utf-8") as out:
    json.dump(records, out, indent=2)

print(f"Wrote {len(records)} records to all_galaxies.json")