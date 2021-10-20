import numpy as np
import matplotlib.pyplot as plt


def create_eah(runs, nb_steps_costs=10, nb_steps_quality=10):
    eah = np.zeros((nb_steps_costs, nb_steps_quality))

    cost_min = min([min(run[0]) for run in runs])
    cost_max = max([max(run[0]) for run in runs])
    quality_min = min([min(run[1]) for run in runs])
    quality_max = max([max(run[1]) for run in runs])

    def get_ind_cost(cost):
        """
        Computes the index of eah corresponding to the cost
        """
        step = (cost_max - cost_min) / (nb_steps_costs - 1)
        ind = (cost - cost_min) // step
        return int(ind)

    def get_ind_quality(quality):
        """
        Computes the index of eah corresponding to the quality
        """
        step = (quality_max - quality_min) / (nb_steps_costs - 1)
        ind = (quality - quality_min) // step
        return int(ind)

    for number, run in enumerate(runs):
        eah_run = np.zeros((nb_steps_costs, nb_steps_quality))
        run_points = zip(*run)
        for point in run_points:
            # Find the edge of the histogram
            cost_ind, quality_ind = (get_ind_cost(point[0]), get_ind_quality(point[1]))
            point_tab = cost_ind, quality_ind

            # Update of the run_eah
            for i in range(quality_ind):
                for j in range(cost_ind, nb_steps_costs):
                    eah_run[i, j] = 1

        eah += eah_run

    return eah


def create_ert(runs, delta):
    cost_max = max([len(run[0]) for run in runs])
    ert_tranche = np.zeros(int(cost_max))

    n = len(runs)

    for run in runs:
        costs, qualities = run
        ert_run = np.array(list(map(lambda x: x > delta, qualities)))
        if len(ert_run) < cost_max:
            ert__run = np.zeros(int(cost_max))
            ert__run[:len(ert_run)] = ert_run
            ert__run[len(ert_run):] = ert_run[-1]
            ert_run = ert__run
        ert_tranche += ert_run
    ert_tranche /= n
    return ert_tranche
