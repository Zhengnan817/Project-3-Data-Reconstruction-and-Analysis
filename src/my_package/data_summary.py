import pandas as pd


class Data_process:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(filepath)

    def load_data(self):
        try:
            # Load data into a DataFrame
            data = pd.read_csv(self.file_path)
            return data
        except FileNotFoundError:
            print(f"File not found at path: {self.file_path}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

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
