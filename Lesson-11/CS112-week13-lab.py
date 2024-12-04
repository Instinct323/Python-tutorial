import pandas as pd


def Q1():
    df = pd.read_csv(r"sales_data.csv")

    # Group by region, calculate total sales and revenue, and sort by total sales
    result = df.groupby("region").agg(
        total_sales=("sales", "sum"),
        total_revenue=("revenue", "sum")
    ).sort_values(by="total_sales", ascending=False)

    print("Q1:\n", result, "\n")
    return result


def Q2():
    df = pd.read_csv(r"marketing_data.csv")

    # Merge the sales summary with marketing data
    result = Q1().merge(df, on="region")
    print("Q2:\n", result, "\n")


def Q3():
    # Provided DataFrame
    df = pd.DataFrame({"price": [200, 300, 400, 500, 300, 600, 700, 900],
                       "brand": ["apple", "google", "apple", "apple", "google", "apple", "google", "google"],
                       "device": ["phone", "phone", "computer", "phone", "computer", "computer", "phone", "computer"]})

    # Group by brand and device, and calculate mean price
    result = df.groupby(["brand", "device"]).mean()
    # Rename the "price" column for clarity (optional)
    result.rename(columns={"price": "mean_price"}, inplace=True)
    print("Q3:\n", result, "\n")


def Q4():
    df = pd.read_csv(r"stocks_data.csv")

    # Pivot the table
    result = df.pivot(index="date", columns="symbol", values="close")
    print("Q4:\n", result, "\n")


def Q5():
    df1 = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c'], 'col3': ['a1', 'b2', 'c3']})
    df2 = pd.DataFrame({'col1': [4, 5, 6], 'col2': ['d', 'e', 'f'], 'col3': ['d4', 'e5', 'f6']})
    df3 = pd.DataFrame({'col1': [7, 8, 9], 'col2': ['g', 'h', 'i'], 'col3': ['g7', 'h2', 'i3']})

    # Concatenate the DataFrames
    result = pd.concat([df1, df2, df3], ignore_index=True)
    print("Q5:\n", result, "\n")


if __name__ == '__main__':
    Q3()
