
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("train.csv")

print("First 5 Rows")
display(df.head())

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nDataset Info")
df.info()

print("\nSummary Statistics")
display(df.describe(include='all'))



# Data Cleaning
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Cabin"] = df["Cabin"].fillna("Unknown")
df = df.drop_duplicates()
print("Cleaning completed.")



plots = [
("Countplot - Survived", lambda: sns.countplot(data=df,x="Survived")),
("Countplot - Passenger Class", lambda: sns.countplot(data=df,x="Pclass")),
("Countplot - Sex", lambda: sns.countplot(data=df,x="Sex")),
("Histogram - Age", lambda: sns.histplot(df["Age"],bins=30,kde=True)),
("Histogram - Fare", lambda: sns.histplot(df["Fare"],bins=30,kde=True)),
("Boxplot - Age", lambda: sns.boxplot(y=df["Age"])),
("Boxplot - Fare", lambda: sns.boxplot(y=df["Fare"])),
("Survival by Gender", lambda: sns.countplot(data=df,x="Sex",hue="Survived")),
("Survival by Passenger Class", lambda: sns.countplot(data=df,x="Pclass",hue="Survived")),
("Survival by Embarked", lambda: sns.countplot(data=df,x="Embarked",hue="Survived")),
("Scatterplot - Age vs Fare", lambda: sns.scatterplot(data=df,x="Age",y="Fare",hue="Survived")),
]

for title,func in plots:
    plt.figure(figsize=(6,4))
    func()
    plt.title(title)
    plt.tight_layout()
    plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include=np.number).corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

sns.pairplot(df[["Age","Fare","Pclass","Survived"]],hue="Survived")
plt.show()
