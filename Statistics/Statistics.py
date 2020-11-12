from Solutions.CSPBacktracking import CSPBacktracking
from Solutions.CSPBacktrackingWithReferences import CSPBacktrackingWithReferences
from Solutions.CSPMatrix import CSPMatrix
import matplotlib.pyplot as plt
import numpy as np


def compare_solutions(n=4):
    for algo in [CSPBacktracking, CSPBacktrackingWithReferences, CSPMatrix]:

        file = "Output/Files/N" + str(n)

        all_sols = []
        g = None
        for i in range(5):
            back = algo(n)
            solutions, graph = back.back(2)
            all_sols.append(solutions)
            if g is None:
                g = graph

        sol_stats = {}
        for run_i in range(len(all_sols)):
            for sol_i in range(len(all_sols[run_i])):
                if sol_i not in sol_stats:
                    sol_stats[sol_i] = 0
                sol_stats[sol_i] += all_sols[run_i][sol_i].get_timestamp()

        for x in sol_stats:
            x /= 2

        result = ""
        output_file = file + "_time_output.txt"
        handle = open(output_file, "a+")

        result = result + algo.__name__ + ",1," + str(sol_stats[0]) + '\n'
        result = result + algo.__name__ + ",2," + str(sol_stats[1]) + '\n'
        handle.write(result)
        handle.close()

        result = ""
        output_file = file + "_graph_output.txt"
        handle = open(output_file, "a+")

        result = result + algo.__name__ + "," + str(g.number_of_nodes()) + '\n'
        handle.write(result)
        handle.close()


def plot_graph_comparisons():
    files = ["Output/Files/N3", "Output/Files/N4"]
    data = [[0 for x in range(4)] for y in range(3)]
    for fi in range(len(files)):
        f = open(files[fi] + "_graph_output.txt")
        lines = f.readlines()
        for li in range(len(lines)):
            split_line = lines[li].split(',')
            data[li][fi] = int(split_line[1])

    X = np.arange(4)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(X + 0.00, data[0], color='b', width=0.25)
    ax.bar(X + 0.25, data[1], color='g', width=0.25)
    ax.bar(X + 0.50, data[2], color='r', width=0.25)

    ax.set_ylabel('Nodes in search graph')
    ax.set_title('Search graph comparison')
    ax.set_xticks(X)
    ax.set_xticklabels(["10 nodes", "4 nodes", "6 nodes", "100 nodes"])
    plt.axis("on")

    plt.show()


def plot_time_comparisons(which):
    files = ["Output/Files/N3", "Output/Files/N4"]
    data = [[0.0 for x in range(4)] for y in range(3)]
    for fi in range(len(files)):
        f = open(files[fi] + "_time_output.txt")
        lines = f.readlines()
        lik = 0
        for li in range(len(lines)):
            if lines[li].strip() != "":
                if li % 2 == which:
                    split_line = lines[li].split(',')
                    data[lik][fi] = float(split_line[2])
                    lik += 1

    X = np.arange(4)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(X + 0.00, data[0], color='b', width=0.25)
    ax.bar(X + 0.25, data[1], color='g', width=0.25)
    ax.bar(X + 0.50, data[2], color='r', width=0.25)

    ax.set_ylabel('Nodes in search graph')
    ax.set_title('Search graph comparison')
    ax.set_xticks(X)
    ax.set_xticklabels(["10 nodes", "4 nodes", "6 nodes", "100 nodes"])
    plt.axis("on")

    plt.show()
