import argparse
from converters.AutoCADConverter import AutoCADConverter
from converters.RevitConverter import RevitConverter
import pandas as pd


def parse_input_arguments():

    parser = argparse.ArgumentParser(description='drawing creator')
    parser.add_argument('-f', '--file_path', default='./data/csv/sample_blueprint.csv', help='file path of csv file')
    parser.add_argument('-cs', '--convert_to_software', default='autocad', help="The software to be covnerted into. Supported softwares:autocad, revit")
    parser.add_argument('-cf', '--convert_to_fmt', default='dwg', help='The specific format to be converted in the selected software')

    return parser.parse_args()

def convert_selected_file(preferences):

    converter_instance = None

    # Instantiating Relevant File Converter
    if preferences.convert_to_software == "autocad":
        converter_instance = AutoCADConverter()
    elif preferences.convert_to_software == "revit":
        converter_instance = RevitConverter()

    # Checking if the selected format is supported
    if not converter_instance.is_type_supported(preferences.convert_to_fmt):
        print("The selected file format is not suppported")
        return False

    # Reading the CSV File
    csv_file_obj = pd.read_csv(preferences.file_path)

    # Trigger Conversion Process
    converter_instance.convert(csv_file_obj=csv_file_obj,
                               selected_to_type=preferences.convert_to_fmt,
                               file_name=preferences.file_path.split('/')[-1].split('.')[0])

if __name__ == '__main__':

    preferences = parse_input_arguments()
    convert_selected_file(preferences)

    print("The End")