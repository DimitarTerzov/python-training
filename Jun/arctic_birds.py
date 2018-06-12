observations_file = open('observations.txt')

birds_observed = set()

for line in observations_file:
    bird = line.strip()
    birds_observed.add(bird)
    
for species in birds_observed:
    print(species)