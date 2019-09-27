import csv

with open('jairbolsonaro.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('jairbolsonaro.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)