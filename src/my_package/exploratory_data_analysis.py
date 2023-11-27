import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class EDA:
    def __init__(self, df):
        """
        Initialize the EDA (Exploratory Data Analysis) class with a DataFrame.

        Parameters:
        - df (pd.DataFrame): The input DataFrame for analysis.
        """
        self.df = df

    def type_vendor_sns(self):
        """
        Create a barplot for 'Type' and 'Vendor' in one picture using Seaborn.

        Returns:
        - None
        """
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
        return plt.show()

    def type_vendor_plt(self):
        """
        Create a barplot for 'Type' and 'Vendor' in one picture using Matplotlib.

        Returns:
        - None
        """

        # Create a barplot for 'Type' and 'Vendor' in one picture
        plt.figure(figsize=(12, 6))

        # Assuming self.df is your DataFrame
        grouped_data = self.df.groupby(["Type", "Vendor"]).size().unstack()

        # Plotting
        grouped_data.plot(kind="bar", stacked=True, colormap="Set3", figsize=(12, 6))

        # Set labels and title
        plt.xlabel("Type")
        plt.ylabel("Count")
        plt.title("Barplot of Type and Vendor")

        # Show the plot
        return plt.show()

    def process_size_sns(self):
        """
        Create a boxplot of chip process size using Seaborn.

        Returns:
        - None
        """
        plt.figure(figsize=(15, 10))
        sns.boxplot(data=self.df["Process Size"], orient="h")
        plt.title("Boxplot of chip process size")
        plt.xlabel("Values")
        return plt.show()

    def process_size_plt(self):
        """
        Create a boxplot of chip process size using Matplotlib.

        Returns:
        - None
        """
        plt.figure(figsize=(15, 10))
        plt.boxplot(self.df["Process Size"], vert=False)
        plt.title("Boxplot of chip process size")
        plt.xlabel("Values")
        return plt.show()

    def vendor_distribution_sns(self):
        """
        Create a countplot for the distribution of vendors using Seaborn.

        Returns:
        - None
        """
        plt.figure(figsize=(12, 6))
        sns.countplot(x=self.df["Vendor"], palette="husl")
        plt.title("Distribution of Vendors")
        plt.xlabel("Vendor")
        plt.ylabel("Count")
        return plt.show()

    def vendor_distribution_plt(self):
        """
        Create a barplot for the distribution of vendors using Matplotlib.

        Returns:
        - None
        """
        plt.figure(figsize=(12, 6))

        # Assuming self.df["Vendor"] contains the vendor data
        unique_vendors, vendor_counts = np.unique(self.df["Vendor"], return_counts=True)

        plt.bar(unique_vendors, vendor_counts, color="mediumseagreen")

        plt.title("Distribution of Vendors")
        plt.xlabel("Vendor")
        plt.ylabel("Count")
        plt.xticks(
            rotation=45, ha="right"
        )  # Rotate x-axis labels for better readability
        return plt.show()

    def TDP_distribution_sns(self):
        """
        Create a boxplot for the distribution of TDP in different vendors using Seaborn.

        Returns:
        - None
        """
        plt.figure(figsize=(12, 8))
        sns.boxplot(x="Vendor", y="TDP", data=self.df, palette="Set3")
        plt.title("TDP distribute in different vendors")
        return plt.show()

    def TDP_distribution_plt(self):
        """
        Create a boxplot for the distribution of TDP in different vendors using Matplotlib.

        Returns:
        - None
        """
        plt.figure(figsize=(8, 6))

        # Boxplot for TDP distribution in different vendors
        plt.boxplot(
            [
                self.df[self.df["Vendor"] == vendor]["TDP"]
                for vendor in self.df["Vendor"].unique()
            ],
            labels=self.df["Vendor"].unique(),
            showfliers=False,
            patch_artist=True,
        )

        plt.xlabel("Vendor")
        plt.ylabel("TDP")
        plt.title("TDP distribution in different vendors")
        return plt.show()
