import math
import random

# distance entre deux villes
def distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

# distance totale d'un chemin
def total_distance(tour, coords):
    total = 0
    for i in range(len(tour)):
        total += distance(coords[tour[i]], coords[tour[(i+1) % len(tour)]])
    return total

# créer une solution voisine (on échange 2 villes)
def voisin(tour):
    t = tour[:]
    i, j = random.sample(range(len(tour)), 2)
    t[i], t[j] = t[j], t[i]
    return t

# critère d'acceptation
def accepte(deltaE, T):
    if deltaE < 0:
        return True
    return random.random() < math.exp(-deltaE / T)

# algorithme du recuit simulé
def recuit_simule(coords):
    # solution initiale aléatoire
    current = list(range(len(coords)))
    random.shuffle(current)
    current_cost = total_distance(current, coords)

    best = current[:]
    best_cost = current_cost

    T = 1000  # température initiale

    

    for step in range(50000):
        neigh = voisin(current)
        neigh_cost = total_distance(neigh, coords)
        deltaE = neigh_cost - current_cost

        if accepte(deltaE, T):
            current = neigh
            current_cost = neigh_cost

            if current_cost < best_cost:
                best = current[:]
                best_cost = current_cost

        T *= 0.995  # refroidissement
        
        # if step % 1000 == 0: print(step, T, best_cost)

    return best, best_cost

# ----------- EXEMPLE ----------------
coords = [(0,0),(1,5),(5,2),(6,6),(8,3)]
solution, dist = recuit_simule(coords)

print("Meilleure solution :", solution)
print("Distance :", dist)
