import matplotlib.pyplot as plt  # noqa: F401
import numpy as np  # noqa: F401
import pandas as pd
import seaborn as sn  # noqa: F401
from pandas import Series, DataFrame  # noqa: F401


class Data_process:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(filepath)

    def view_data(self):
        return self.df.head()

    def say(self):
        print("The file is", self.filepath)
        print(self.project.head(1))
