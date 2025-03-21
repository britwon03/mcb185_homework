import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q): # using taxi - cab distance to find the distance
    d = 0
    for p, q in zip(P, Q):
        d += abs(p - q)
    return d

min_distance = float('inf') # set initial 
closest_color = None

with open(colorfile, 'rt') as fp:
    for line in fp:
        if line.startswith('#') or not line.strip():
            continue

        fields = line.strip().split('\t')
        name = fields[0]
        rgb_values = fields[2].split(',') # takes the rgb values from the tsv file 
        
        r = int(rgb_values[0])
        g = int(rgb_values[1])
        b = int(rgb_values[2])
        # computes the distance between the values 
        distance = dtc([R, G, B], [r, g, b])

        if distance < min_distance:
            min_distance = distance
            closest_color = name

print(closest_color)