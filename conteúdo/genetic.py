import random

# Parâmetros do problema
item_weights = [2, 3, 4, 5]  # Pesos dos itens
item_values = [3, 4, 5, 6]   # Valores dos itens
capacity = 5                # Capacidade máxima da mochila
num_items = len(item_weights)
population_size = 500
num_generations = 50
mutation_rate = 0.1

def generate_individual():
    """Gera um indivíduo (solução candidata) aleatório."""
    return [random.randint(0, 1) for _ in range(num_items)]

def calculate_fitness(individual):
    """Calcula a adequação (fitness) de um indivíduo."""
    total_weight = sum(individual[i] * item_weights[i] for i in range(num_items))
    total_value = sum(individual[i] * item_values[i] for i in range(num_items))
    if total_weight > capacity:
        return 0  # Penaliza soluções que excedem a capacidade
    return total_value

def select_population(population):
    """Seleciona indivíduos para a próxima geração usando roleta."""
    fitness_values = [calculate_fitness(ind) for ind in population]
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return random.choices(population, probabilities, k=population_size)

def crossover(parent1, parent2):
    """Realiza o cruzamento (crossover) entre dois pais."""
    point = random.randint(1, num_items - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual):
    """Aplica mutação em um indivíduo."""
    for i in range(num_items):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]

def genetic_algorithm():
    """Executa o algoritmo genético para o problema da mochila."""
    population = [generate_individual() for _ in range(population_size)]

    for generation in range(num_generations):
        population = select_population(population)
        new_population = []

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population[:population_size]

        best_individual = max(population, key=calculate_fitness)
        best_fitness = calculate_fitness(best_individual)
        print(f"Generation {generation}: Best fitness = {best_fitness}, Best individual = {best_individual}")

    best_solution = max(population, key=calculate_fitness)
    return best_solution, calculate_fitness(best_solution)

# Executa o algoritmo genético
best_solution, best_value = genetic_algorithm()
print(f"Melhor solução: {best_solution}")
print(f"Valor total dos itens na mochila: {best_value}")
