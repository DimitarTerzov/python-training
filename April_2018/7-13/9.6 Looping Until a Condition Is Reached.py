time = 0
population = 1000   # 4000 bacteria to start with
growth_rate = 0.21  # 21% growth per minute
while population < 2000:
    population = population + growth_rate * population
    print(population)
    time = time + 1
    
print("It took", time, "minutes for the bacteria to double.")
print("The final population is", round(population), "bacteria.")
