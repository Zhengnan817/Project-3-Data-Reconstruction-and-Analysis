import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas import DataFrame, Series
from src.my_package.data_summary import Data_process


class EDA:
    def __init__(self, df):
        self.df = df

    def type_vendor(self):
        # Create a barplot for 'Type' and 'Vendor' in one picture
        plt.figure(figsize=(12, 6))
        sns.catplot(
            data=self.df,
            x="Type",
            hue="Vendor",
            kind="count",
            palette="Set3",
            height=6,
            aspect=2,
        )

        # Set labels and title
        plt.xlabel("Type")
        plt.ylabel("Count")
        plt.title("Barplot of Type and Vendor")

        # Show the plot
        plt.show()

    def process_size(self):
        plt.figure(figsize=(15, 10))
        sns.boxplot(data=self.df["Process Size"], orient="h")
        plt.title("Boxplot of chip process size")
        plt.xlabel("Values")
        plt.show()

    def vendor_distribute(self):
        plt.figure(figsize=(12, 6))
        sns.countplot(x=self.df["Vendor"], palette="husl")
        plt.title("Distribution of Vendors")
        plt.xlabel("Vendor")
        plt.ylabel("Count")
        plt.show()

    def release_date(self):
        plt.figure(figsize=(12, 8))
        sns.boxplot(x="Vendor", y="TDP", data=self.df, palette="Set3")
        plt.title("TDP distribute in different vemdors")
        plt.show()
