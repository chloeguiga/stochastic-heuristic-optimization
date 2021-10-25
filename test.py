"""
Plot the distribution of the algorithms run in snp.py for evaluation
"""
import get_evaluation
import evaluation_representation
import plot_representation
import algo_comparison

if __name__ == "__main__":
    N_RUNS = 100
    METHOD_NAME = "num_annealing"
    RESOLUTION = 50
    DELTA = 600
    DELTAS = (600, 660, 675)
    METHOD_NAMES = ["num_annealing", "bit_annealing"]


    # get_evaluation.create_evaluation(N_RUNS, METHOD_NAME)
    runs = get_evaluation.get_data(METHOD_NAME)
    plot_representation.plot_runs(runs, title=METHOD_NAME)

    eah = evaluation_representation.create_eah(runs, RESOLUTION, RESOLUTION)
    plot_representation.plot_eah(eah, title=METHOD_NAME + "_eah")

    ert = evaluation_representation.create_ert(runs, DELTA)
    plot_representation.plot_ert(ert, title=METHOD_NAME + "_ert" + ", delta = " + str(DELTA), x_label="Budget",
                                 y_label="Probability (x > {})".format(str(DELTA)))

    #algo_comparison.compare_ert(METHOD_NAMES, deltas=DELTAS, nb_runs=N_RUNS)

    costs, qualities, eaf = evaluation_representation.create_eaf(runs)
    plot_representation.plot_eaf(costs, qualities, eaf, title=METHOD_NAME+"_eaf")


