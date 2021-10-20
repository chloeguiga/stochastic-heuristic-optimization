
def evaluation_run(times, qualities, method_name):
    """
    Register the results of cost and quality over one run
    """
    n = len(times)
    if n != len(qualities):
        raise Exception("times and quality don't have matching lengths")
    file_txt = to_file(method_name)
    file = open(file_txt, "a")
    for i in range(n):
        time, quality = times[i], qualities[i]
        file.write("{} {} ".format(time, quality))

    file.write("\n")
    file.close()
    return None


def clear_method(method_name):
    file_txt = to_file(method_name)
    file = open(file_txt, 'w')
    file.truncate(0)
    file.close()


def get_data(method_name):
    file_txt = to_file(method_name)
    file = open(file_txt, 'r')
    data = []
    run_i = file.readline()

    while run_i != "":
        run_i = run_i.split(" ")
        run_i = list(map(eval, run_i[:-1]))

        costs = [cost for k, cost in enumerate(run_i) if k % 2 == 0]
        qualities = [quality for k, quality in enumerate(run_i) if k % 2 == 1]
        data.append((costs, qualities))

        run_i = file.readline()

    return data


def to_file(method_name):
    return "".join([method_name, ".txt"])



def create_evaluation(n_runs, method_name="num_annealing"):
    clear_method(method_name)
    for k in range(n_runs):
        exec(open('snp.py').read())
    return None

