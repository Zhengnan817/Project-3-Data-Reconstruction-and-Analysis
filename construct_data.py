import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class reconstruct_data:
    def __init__(self, df):
        """
        Initialize the EDA (Exploratory Data Analysis) class with a DataFrame.

        Parameters:
        - df (pd.DataFrame): The input DataFrame for analysis.
        """
        self.df = df

    # def compare_CPU_and_GPU(self.df)
