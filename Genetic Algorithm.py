import random

chromosomes=['01101','11000','01000','10011']

def fitness(binary_str):
    x=int(binary_str,2)
    return x ** 2
    
fitness_values=[]

for chrom in chromosomes:
    fitness_values.append(fitness(chrom))

total_fitness=sum(fitness_values)

start=0.0

bins=[]

for i in range(len(chromosomes)):
    chrom=chromosomes[i]
    fitness_value=fitness_values[i]
    probability=fitness_value/total_fitness
    
    end=start+probability
    bins.append((start,end,chrom))
    
    print(f"Chromosome c{i+1}(binary:{chrom},integer:{int(chrom,2)})-Fitness Value:{fitness_value},Probability:{probability:.3f}, Bin Range:{start:.3f}-{end:.3f}")
    start=end
    
random_value=random.random()

for start,end,chrom in bins:
    if start<=random_value<end:
        print(f"Random Value:{random_value:.2f} falls in Bin Range:{start:.3f}-{end:.3f} for Chromosome:{chrom}")
        break

