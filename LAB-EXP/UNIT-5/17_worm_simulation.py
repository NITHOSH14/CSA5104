import random

nodes = 10
infected = {0}

for step in range(1, 6):
    new_infected = set()
    for node in range(nodes):
        if node in infected:
            for target in range(nodes):
                if target not in infected and random.random() < 0.3:
                    new_infected.add(target)
    infected |= new_infected
    print(f'Step {step}: infected nodes = {sorted(infected)}')
