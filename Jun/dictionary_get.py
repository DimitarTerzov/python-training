observations_file = open('observations.txt')

bird_to_count = {}

for line in observations_file:
    bird = line.strip()
    # Find a bird, i'f there is bird with the same name, add to first one.
    bird_to_count[bird] = bird_to_count.get(bird, 0) + 1
    
observations_file.close()

alphabet_names = sorted(bird_to_count.keys())

for bird in alphabet_names:
    print(bird, bird_to_count[bird])