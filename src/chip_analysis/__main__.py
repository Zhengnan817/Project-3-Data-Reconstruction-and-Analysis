"""Enable running `python -m chip_analysis`."""

from src.chip_analysis.data_summary import DataProcess
from src.chip_analysis.exploratory_data_analysis import EDA
from src.chip_analysis.inferences import Inferences


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


def exploratory_data_analysis():
    cpu_table = data_summary()
    cpu_table.check_data()
    df = cpu_table.view_data

    EDA_part = EDA(df)
    type_distribution_sns = EDA_part.vendor_distribution_sns()
    print(type_distribution_sns)

    type_distribution_plt = EDA_part.vendor_distribution_plt()
    print(type_distribution_plt)

    product_vendor_sns = EDA_part.type_vendor_sns()
    print(product_vendor_sns)

    product_vendor_plt = EDA_part.type_vendor_plt()
    print(product_vendor_plt)

    process_size_sns = EDA_part.process_size_sns()
    print(process_size_sns)

    process_size_plt = EDA_part.process_size_plt()
    print(process_size_plt)

    process_size_vendor = EDA_part.process_size_vendor_sns()
    print(process_size_vendor)

    process_size_vendor = EDA_part.process_size_vendor_plt()
    print(process_size_vendor)

    release_date_sns = EDA_part.TDP_distribution_sns()
    print(release_date_sns)

    release_date_plt = EDA_part.TDP_distribution_plt()
    print(release_date_plt)


def inferences():
    cpu_table = data_summary()
    df = cpu_table.view_data

    inferences_analysis = Inferences(df)

    vendor_and_type = inferences_analysis.vendor_type_plt()
    print(vendor_and_type)

    vendor_and_type_sns = inferences_analysis.vendor_type_sns()
    print(vendor_and_type_sns)

    chip_attri = inferences_analysis.chip_attribute()
    print(chip_attri)

    average_freq = inferences_analysis.ave_freq_type_ven()
    print(average_freq)

    freq_TDP = inferences_analysis.freq_and_TDP()
    print(freq_TDP)


main()
