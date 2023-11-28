"""Run Chip analysis CLI for part 1 to part 4 """

from chip_analysis_package.data_summary import Data_process
from chip_analysis_package.exploratory_data_analysis import EDA
from chip_analysis_package.inferences import Inferences


def main():
    """
    Run Chip analysis as a script.
    """
    print("Project_3_Data_Reconstruction_and_Analysis")
    while True:
        print("(1)data_summary\n(2)exploratory_data_analysis\n(3)inferences")
        choice = input("Enter your choice: ")

        if choice == "1":
            data_summary()
        elif choice == "2":
            exploratory_data_analysis()
        elif choice == "3":
            exploratory_data_analysis()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def data_summary():
    my_file_path = "chip_analysis_data/data/chip_dataset.csv"
    cpu_table = Data_process(my_file_path)
    df = cpu_table.view_data()
    print(df.head())

    column_types = df.dtypes
    print(column_types)
    return cpu_table


def exploratory_data_analysis():
    cpu_table = data_summary()
    cpu_table.check_data()
    df = cpu_table.view_data
    from src.chip_analysis_package.exploratory_data_analysis import EDA

    EDA_part = EDA(df)
    type_distribution_sns = EDA_part.vendor_distribution_sns()

    type_distribution_plt = EDA_part.vendor_distribution_plt()

    product_vendor_sns = EDA_part.type_vendor_sns()

    product_vendor_plt = EDA_part.type_vendor_plt()

    process_size_sns = EDA_part.process_size_sns()

    process_size_plt = EDA_part.process_size_plt()

    process_size_vendor = EDA_part.process_size_vendor_sns()

    process_size_vendor = EDA_part.process_size_vendor_plt()

    release_date_sns = EDA_part.TDP_distribution_sns()

    release_date_plt = EDA_part.TDP_distribution_plt()


def inferences():
    cpu_table = data_summary()
    df = cpu_table.view_data
    from src.chip_analysis_package.inferences import Inferences  # noqa: E402

    inferences_analysis = Inferences(df)
    inferences_analysis.vendor_type_plt()
    inferences_analysis.vendor_type_sns()
    inferences_analysis.chip_attribute()
    inferences_analysis.ave_freq_type_ven()
    inferences_analysis.freq_and_TDP()
