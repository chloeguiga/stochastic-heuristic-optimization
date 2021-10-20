"""
Plot the distribution of the algorithms run in snp.py for evaluation
"""
import get_evaluation
import evaluation_representation


if __name__ == "__main__":
    N_RUNS = 10
    METHOD_NAME = "num_annealing"
    RESOLUTION = 50
    DELTA = 600

    # get_evaluation.create_evaluation(N_RUNS, METHOD_NAME)
    runs = get_evaluation.get_data(METHOD_NAME)
    evaluation_representation.plot_runs(runs, title=METHOD_NAME)

    eah = evaluation_representation.create_eah(runs, RESOLUTION, RESOLUTION)
    evaluation_representation.plot_eah(eah, title=METHOD_NAME + "_eah")

    ert = evaluation_representation.create_ert(runs, DELTA)
    evaluation_representation.plot_ert(ert, title=METHOD_NAME + "_ert" + ", delta = " + str(DELTA), x_label="Budget", y_label="Probability (x > {})".format(str(DELTA)))


