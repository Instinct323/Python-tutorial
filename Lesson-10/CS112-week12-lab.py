import numpy as np
import pandas as pd


def Q1():
    genes = np.array(['ERAP1', 'IL10', 'JAK2', 'TP53', 'EST1'])
    ctrl = pd.Series([120, 52, 100, 90, 20], index=genes)
    treated = pd.Series([120, 20, 90, 120, 25], index=genes)

    mask = np.abs(ctrl - treated) > 20
    print("Mask:\n", mask)
    print("\nResult:", genes[mask])


def Q2():
    genes = ['ERAP1', 'IL10', 'JAK2', 'TP53', 'EST1']
    ctrl = [120, 52, 100, 90, 20]
    treated = [120, 20, 90, 120, 25]

    df = pd.DataFrame({"ctrl": ctrl, "treated": treated}, index=genes)
    print(df)
    print(df.T)


def Q3():
    records = {'Name': ['Mary', 'Maria', 'Anna', 'John', 'Jake', 'Joe'],
               'Gender': ['Female', 'Female', 'Female', 'Male', 'Male', 'Male'],
               'Score': [88, 92, 56, 70, 55, 48]}
    df = pd.DataFrame(records)
    print(df)

    mask = (df["Gender"] == "Male") * (df["Score"] < 60)
    print("\nMask:\n", mask)
    # Convert boolean mask to list
    print("\nResult:", df["Name"][mask].tolist())


def Q4():
    df = pd.read_csv("codon_table.txt", sep=" ",
                     names=["codon", "single", "triple"], index_col=0)
    print(df)
    df.to_csv("codon_table.csv", index=False)


def Q5():
    df = pd.read_csv("codon_table.txt", sep=" ",
                     names=["codon", "single", "triple"], index_col=0)
    print(df)

    print("--- 1 ---")
    for q in ["ATT", "ATG", "TGC", "GTT"]:
        v = df.loc[q].tolist()
        print(f"The single and triple letters for {q} are {v[0]} and {v[1]}.")

    print("--- 2 ---")
    for q in "LMTI":
        v = df[df["single"] == q]
        print(f"The codons for the single letter {q} are {v.index.tolist()}.")


def Q6():
    data = pd.read_csv("Titanic.csv")

    # 1. Survival rates for male and female passengers
    print("--- 1 ---")
    print("Male:", data["Survived"][data["Sex"] == "male"].mean())
    print("Female:", data["Survived"][data["Sex"] == "female"].mean())

    # 2. Normalize the fare data by dividing it by the mean fare
    print("--- 2 ---")
    data["tmp"] = data["Fare"] / data["Fare"].mean()
    print(data["tmp"])

    # 3. Sort the data by age
    print("--- 3 ---")
    data = data.sort_values("Age")
    print(data)


if __name__ == '__main__':
    Q5()
