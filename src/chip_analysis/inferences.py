import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class Inferences:
    """
    A class for generating various visualizations and inferences from Chips of GPU and CPU.

    This class provides methods to visualize and analyze data, specifically tailored for a DataFrame
    containing information about vendors, types, process sizes, release dates, and attributes of chips.

    Attributes:
    - df (pd.DataFrame): The input DataFrame for analysis.

    Methods:
    - __init__(self, df): Initialize the Inferences class with a DataFrame.
    - vendor_type_sns(self): Generate a Seaborn bar plot to visualize the distribution of Vendor types.
    - vendor_type_plt(self): Generate a Matplotlib bar plot to visualize the distribution of Vendor types.
    - ave_freq_type_ven(self): Generate a Seaborn bar plot to visualize the average frequency for each product and vendor.
    - chip_attribute(self): Generate a Seaborn box plot to visualize chip attributes across vendors.
    - freq_and_TDP(self): Generate a Matplotlib bar plot to visualize the average TDP by vendor.
    """

    def __init__(self, df):
        """
        Initialize the Inferences class with a DataFrame.

        Parameters:
        - df (pd.DataFrame): The input DataFrame for analysis.
        """
        self.df = df

    def vendor_type_sns(self):
        """
        Generate a Seaborn bar plot to visualize the distribution of Vendor types.

        The plot shows the count of each type for each vendor.

        Returns:
        None
        """
        crosstab = pd.crosstab(index=self.df["Vendor"], columns=self.df["Type"])
        crosstab.plot.bar(figsize=(7, 4), rot=0).set(ylabel="Type", title="Vendor")

    def vendor_type_plt(self):
        """
        Generate a Matplotlib bar plot to visualize the distribution of Vendor types.

        The plot shows the count of each type for each vendor.

        Returns:
        None
        """
        crosstab = pd.crosstab(index=self.df["Vendor"], columns=self.df["Type"])

        # Using Matplotlib for a bar plot
        plt.figure(figsize=(7, 4))
        for col in crosstab.columns:
            plt.bar(crosstab.index, crosstab[col], label=col)

        plt.xlabel("Vendor")
        plt.ylabel("Type")
        plt.title("Vendor Type Distribution")
        plt.legend()
        plt.show()

    def ave_freq_type_ven(self):
        """
        Generate a Seaborn bar plot to visualize the average frequency for each product and vendor.

        Returns:
        None
        """
        pivot_data = self.df.pivot_table(
            index=["Type", "Vendor"], values="Process Size", aggfunc="mean"
        ).reset_index()

        # Perform exploratory data analysis (EDA)

        # Example: Bar plot for average frequency for each product and vendor
        plt.figure(figsize=(12, 6))
        sns.barplot(
            x="Type",
            y="Process Size",
            hue="Vendor",
            data=pivot_data,
            palette="viridis",
        )
        plt.title("Average Frequency for Each Vendor and Vendor")
        plt.xlabel("Type")
        plt.ylabel("Average Frequency")
        plt.xticks(rotation=45, ha="right")
        plt.legend(title="Vendor", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.show()

    def chip_attribute(self):
        """
        Generate a Seaborn box plot to visualize chip attributes across vendors.

        The plot shows the distribution of attributes (excluding Transistors and Freq) for each vendor.

        Returns:
        None
        """
        re_release_vendor = pd.melt(
            self.df.drop(["Transistors", "Freq"], axis=1),
            id_vars=["Product", "Type", "Release Date", "Vendor"],
            var_name="Attribute",
            value_name="Value",
        )
        plt.figure(figsize=(8, 8))
        sns.boxplot(x="Attribute", y="Value", data=re_release_vendor, hue="Vendor")
        plt.title("Attribute View")
        plt.show()

    def freq_and_TDP(self):
        """
        Generate a Matplotlib bar plot to visualize the average TDP by vendor.

        Returns:
        None
        """
        grouped_data = self.df.groupby("Vendor").agg({"Die Size": "mean"}).reset_index()
        grouped_data.plot(kind="bar", y="Die Size", x="Vendor", legend=False)
        plt.title("Average Die Size by Vendor")
        plt.xlabel("Vendor")
        plt.ylabel("Average Die Size")
        plt.show()
