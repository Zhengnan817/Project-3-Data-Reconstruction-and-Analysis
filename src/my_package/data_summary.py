import pandas as pd


class Data_process:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(filepath)

    def view_data(self):
        """
        Display the first few rows of the dataframe.

        Returns:
        pandas.DataFrame: The first few rows of the dataframe.
        """
        return self.df

    def check_data(self):
        """
        Print information about the file and display the first row of the dataframe.
        """
        return self.df.isna().sum()

    def remove_null(self):
        """
        Remove rows with null values from the dataframe.

        Returns:
        pandas.DataFrame: The dataframe with null values removed.
        """
        return self.df.dropna()
