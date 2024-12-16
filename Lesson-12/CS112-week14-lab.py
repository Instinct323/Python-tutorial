import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

drug_conc = [0, 0.5, 1, 2, 3, 4]
response1 = [0, 0.2, 0.5, 0.8, 0.9, 0.95]
response2 = [0, 0.1, 0.2, 0.4, 0.8, 0.9]


def Q1():
    plt.title("title")

    # labels
    plt.xlabel("drug concentration")
    plt.ylabel("response")

    # ticks
    plt.grid(True)
    plt.xticks(drug_conc)
    plt.yticks(response2)

    # :param color: red, orange, yellow, green, cyan, blue, purple, pink
    # :param marker: o, d, p, *, h, s
    # :param linestyle: -, --, -., :
    plt.plot(drug_conc, response1, color="red", label="response1", marker="s", linestyle=":")
    plt.plot(drug_conc, response2, color="orange", label="response2", marker="d", linestyle="--")

    # legend
    plt.legend()

    # save must before show
    plt.savefig("Q1.png", dpi=300)
    plt.show()


def Q2():
    fig = plt.figure()
    res = [response1, response2]

    for i in range(2):
        fig.add_subplot(1, 2, i + 1)
        plt.plot(drug_conc, res[i])

        # title and labels
        plt.title(f"animal {i + 1}")
        plt.xlabel("drug concentration")
        if i == 0: plt.ylabel("response")

    plt.show()


def Q4():
    df = pd.read_csv("codon_usage.csv")

    plt.title("codon frequency for T")

    plt.bar(df["codon"], df["relative_frequency"])
    plt.show()


def Q5():
    df = pd.read_csv("Titanic.csv")

    # labels
    plt.xlabel("Age")
    plt.ylabel("Fare")

    colors = np.array(["red", "yellow", "blue"])
    plt.scatter(df["Age"], df["Fare"], alpha=0.5, c=colors[df["Pclass"].to_numpy() - 1])

    plt.show()


if __name__ == '__main__':
    Q5()
