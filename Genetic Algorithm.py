chromosomes=['01101','11000','01000','10011']

def fitness(binary_str):
    x=int(binary_str,2)
    return x ** 2
    
fitness_values=[]

for chrom in chromosomes:
    fitness_values.append(fitness(chrom))

total_fitness=sum(fitness_values)

for i in range(len(chromosomes)):
    chrom=chromosomes[i]
    fitness_value=fitness_values[i]
    probability=fitness_value/total_fitness
    
    print(f"Chromosome c{i+1}(binary:{chrom},integer:{int(chrom,2)})-Fitness Value:{fitness_value},Probability:{probability:.2f}")
