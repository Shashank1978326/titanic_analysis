import pandas as pd
from tabulate import tabulate

try:
    # Read CSV file
    df = pd.read_csv("titanic.csv")
    print("File loaded successfully")

    # First 10 Rows
    print("\nFirst 10 Rows:")
    print(tabulate(df.head(10), headers="keys", tablefmt="grid"))

    # Last 5 Rows
    print("\nLast 5 Rows:")
    print(tabulate(df.tail(5), headers="keys", tablefmt="grid"))

    # Dataset Information
    print("\nDataset Information:")
    df.info()

    # Passengers older than 60 or in First Class
    print("\nPassengers older than 60 or in First Class:")

    filtered_rows = []

    for i in range(len(df)):
        age = df.loc[i, "Age"]
        pclass = df.loc[i, "Pclass"]

        if (pd.notna(age) and age > 60) or pclass == 1:
            filtered_rows.append(df.loc[i])

    if filtered_rows:
        filtered_df = pd.DataFrame(filtered_rows)
        print(tabulate(filtered_df, headers="keys", tablefmt="grid"))
    else:
        print("No matching passengers found")

    # Fill missing Age values with median
    median_age = df["Age"].median()
    df["Age"] = df["Age"].fillna(median_age)

    print("\nMissing Age values filled with median age:", median_age)

    # Create new columns
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["FarePerPerson"] = df["Fare"] / df["FamilySize"]
    df["IsChild"] = df["Age"] < 12

    # Show new columns
    print("\nNew Columns Created:")
    print(
        tabulate(
            df[["FamilySize", "FarePerPerson", "IsChild"]].head(10),
            headers="keys",
            tablefmt="grid"
        )
    )

    # Statistics Table
    stats = df[["Age", "Fare", "FamilySize", "FarePerPerson"]].describe()

    print("\nStatistics:")
    print(tabulate(stats, headers="keys", tablefmt="grid"))

    # Survival Count
    print("\nSurvival Count:")
    survival_table = df["Survived"].value_counts().reset_index()
    survival_table.columns = ["Survived", "Count"]

    print(tabulate(survival_table, headers="keys", tablefmt="grid"))

    # Women and Children
    women_children = df[(df["Sex"] == "female") | (df["Age"] < 12)]

    print("\nWomen and Children:")
    print(tabulate(women_children.head(10), headers="keys", tablefmt="grid"))

    # Save all results to a text file
    with open("titanic_report.txt", "w", encoding="utf-8") as file:

        file.write("Titanic Dataset Analysis\n")
        file.write("=" * 60 + "\n\n")

        file.write("First 10 Rows:\n")
        file.write(tabulate(df.head(10), headers="keys", tablefmt="grid"))
        file.write("\n\n")

        file.write("Last 5 Rows:\n")
        file.write(tabulate(df.tail(5), headers="keys", tablefmt="grid"))
        file.write("\n\n")

        file.write("Passengers older than 60 or in First Class:\n")
        if filtered_rows:
            file.write(tabulate(filtered_df, headers="keys", tablefmt="grid"))
        else:
            file.write("No matching passengers found")
        file.write("\n\n")

        file.write("Statistics:\n")
        file.write(tabulate(stats, headers="keys", tablefmt="grid"))
        file.write("\n\n")

        file.write("New Columns:\n")
        file.write(
            tabulate(
                df[["FamilySize", "FarePerPerson", "IsChild"]].head(10),
                headers="keys",
                tablefmt="grid"
            )
        )
        file.write("\n\n")

        file.write("Survival Count:\n")
        file.write(tabulate(survival_table, headers="keys", tablefmt="grid"))
        file.write("\n\n")

        file.write("Women and Children:\n")
        file.write(tabulate(women_children.head(10), headers="keys", tablefmt="grid"))

    print("\nReport saved successfully as titanic_report.txt")

except FileNotFoundError:
    print("titanic.csv file not found")

except Exception as e:
    print("An error occurred:", e)