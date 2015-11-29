import os

outfile = open('../combined.txt', 'w')
for root, dir, files in os.walk("."):
    for file in files:
        if file.endswith('.txt'):
            path = os.path.join(root, file)
            with open(path) as infile:
                for line in infile:
                    outfile.write(line)

outfile.close()
 
