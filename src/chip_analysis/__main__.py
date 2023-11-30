"""Enable running `python -m chip_analysis`."""

from .data_summary import DataProcess
from .exploratory_data_analysis import EDA
from .inferences import Inferences


def main():
    """
    Run Chip analysis as a script.
    """
    print("------------------------------------------------")
    print("Project_3_Data_Reconstruction_and_Analysis")
    print("------------------------------------------------")

    data_summary()
    print("------------------------------------------------")
    exploratory_data_analysis()
    print("------------------------------------------------")
    inferences()
    print("------------------------------------------------")


def data_summary():
    my_file_path = "https://raw.githubusercontent.com/Zhengnan817/Project-3-Data-Reconstruction-and-Analysis/main/src/chip_analysis/data/chip_dataset.csv"
    cpu_table = DataProcess(my_file_path)
    df = cpu_table.view_data()
    print(df.head())

    column_types = df.dtypes
    print(column_types)

    return cpu_table


def exploratory_data_analysis():
    my_file_path = "https://raw.githubusercontent.com/Zhengnan817/Project-3-Data-Reconstruction-and-Analysis/main/src/chip_analysis/data/chip_dataset.csv"
    cpu_table = DataProcess(my_file_path)
    df = cpu_table.view_data()
    EDA_part = EDA(df)
    while True:
        EDA_part.vendor_distribution_sns()

        EDA_part.vendor_distribution_plt()

        EDA_part.type_vendor_sns()

        EDA_part.type_vendor_plt()

        EDA_part.process_size_sns()

        EDA_part.process_size_plt()

        EDA_part.process_size_vendor_sns()

        EDA_part.process_size_vendor_plt()

        EDA_part.TDP_distribution_sns()

        EDA_part.TDP_distribution_plt()


def inferences():
    my_file_path = "https://raw.githubusercontent.com/Zhengnan817/Project-3-Data-Reconstruction-and-Analysis/main/src/chip_analysis/data/chip_dataset.csv"
    cpu_table = DataProcess(my_file_path)
    df = cpu_table.view_data()
    inferences_analysis = Inferences(df)
    while True:
        inferences_analysis.vendor_type_plt()

        inferences_analysis.vendor_type_sns()

        inferences_analysis.chip_attribute()

        inferences_analysis.ave_freq_type_ven()

        inferences_analysis.freq_and_TDP()


main()
