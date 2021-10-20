########################################################################
# Algorithms
########################################################################
import numpy as np
from sho import num


def random(func, init, again):
    """Iterative random search template."""
    best_sol = init()
    best_val = func(best_sol)
    val, sol = best_val, best_sol
    i = 0
    while again(i, best_val, best_sol):
        sol = init()
        val = func(sol)
        if val >= best_val:
            best_val = val
            best_sol = sol
        i += 1
    return best_val, best_sol


def greedy(func, init, neighb, again):
    """Iterative randomized greedy heuristic template."""
    best_sol = init()
    best_val = func(best_sol)
    val, sol = best_val, best_sol
    i = 1
    while again(i, best_val, best_sol):
        sol = neighb(best_sol)
        val = func(sol)
        # Use >= and not >, so as to avoid random walk on plateus.
        if val >= best_val:
            best_val = val
            best_sol = sol
        i += 1
    return best_val, best_sol


def simu_annealing(func, init, neighb, again, T_init=2, alpha=0.5, beta=2, evaluation=True):
    """Iterative randomized greedy heuristic template."""
    best_sol = init()
    best_val = func(best_sol)
    val, sol = best_val, best_sol
    T = T_init
    i = 1
    if evaluation:
        L_val = []

    # Fonction de recui simule
    def test_recui(f0, f1, t_instant):
        return np.exp(-(f1 - f0) / t_instant) < alpha

    while again(i, best_val, best_sol):
        # Mise a jour de la bonne solution
        sol = neighb(best_sol)
        val = func(sol)
        # Use >= and not >, so as to avoid random walk on plateus.
        if val >= best_val:
            best_val = val
            best_sol = sol

        elif test_recui(best_val, val, T):
            best_val, best_sol = val, sol

        if evaluation:
            L_val.append(best_val)

        i += 1
        T /= beta

    if evaluation:
        return L_val, best_sol

    return best_val, best_sol


# TODO add a population-based stochastic heuristic template.
def stochastic_heuristic(func, init, neighb, again, pop_size=15, selection_size=5):
    """Population-based stochastic heuristic template"""
    population = [init() for k in range(pop_size)]
    pop_val = [func(individual) for individual in population]
    idx = np.argmax(np.array(pop_val))
    best_val, best_sol = pop_val[idx], population[idx]
    val,sol = best_val,best_sol
    i = 1
    while again(i, best_val, best_sol):

        ## SELECTION ##
        """
        Below, I randomly select k individuals among the population (where k is the selection size).
        """
        total_val = np.sum(pop_val)
        indices = np.random.choice(len(population), selection_size, replace=False, p=[(pop_val[j]/total_val) for j in range(len(pop_val))])
        selected_population = np.array(population)[indices]
        selected_population = list(selected_population)

        ## MUTATION ##
        """
        Here, I choose a close neighboor of each selected individuals.
        I have decided to do only a mutation (so no crossover) as I have good results and that the execution is already pretty long (30s to 1min, depending on chosen parameters).
        """
        mutation_population = [neighb(individual) for individual in selected_population]

        ## REPLACEMENT AND FITNESS ##
        population += mutation_population                                       #I add the mutated population to the population
        pop_val = [func(individual) for individual in population]               #I apply the function to each of them and then sort them.
        index_order = sorted(range(len(pop_val)), key = lambda k:pop_val[k])
        population = [population[i] for i in index_order]
        pop_val = [pop_val[i] for i in index_order]
        population = population[selection_size:]                                #I remove the k less good individuals (where k is the selection size) to keep the same population size.
        pop_val = pop_val[selection_size:]


        idx = np.argmax(np.array(pop_val))
        val, sol = pop_val[idx], population[idx]
        if val > best_val :
            best_val, best_sol = val, sol
        i += 1
    return best_val, best_sol

########################################################################
# Additional functions
########################################################################


def argmax_k(list_iter, k):
    """
    Compute the indices of the k highest elements of the list l.
    :param list_iter: list
    :param k: int
    :return: bests_ind: list
    """
    list_sorted = list_iter.copy()
    sorted(list_sorted)
    goods = list_sorted[-k:]
    bests_ind = []
    for ind, elem in enumerate(list_iter):
        if elem in goods:
            bests_ind.append(ind)
    return bests_ind


def argmax_k_old(list_iter, k):
    """
    Compute the indices of the k highest elements of the list l.
    :param list_iter: list
    :param k: int
    :return: bests_ind: list
    """
    l_ = list_iter.copy()
    bests_ind = []
    mini = min(l_) - 1
    for i in range(k):
        if i >= len(l_):
            return bests_ind
        ind = np.argmax(l_)
        bests_ind.append(ind)
        l_[ind] = mini
    return bests_ind
