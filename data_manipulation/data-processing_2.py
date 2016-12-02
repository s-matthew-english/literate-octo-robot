tally = {}

with open('phase_ii_output.txt', 'r') as infile, open('off_to_the_map.txt', 'w') as outfile:
    for line in infile:
        data = line.strip('\n')
        tag1, code, tag2, num = data.split()
        tally[code] = tally.get(code, 0) + int(num)
    for key, value in tally.items():
        outfile.write(' '.join(map(str, [key, value, '\n'])))