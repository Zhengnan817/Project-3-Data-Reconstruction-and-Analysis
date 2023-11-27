import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


class EDA:
    def __init__(self, df):
        """
        Initialize the Inferences class with a DataFrame.

        Parameters:
        - df (pd.DataFrame): The input DataFrame for analysis.
        """
        self.df = df

    def vendor_type():
        crosstab = pd.crosstab(index=self.df["Vendor"], columns=self.df["Process Size"])
        crosstab.plot.bar(figsize=(7, 4), rot=0).set(
            ylabel="Process Size", title="Vendor"
        )
