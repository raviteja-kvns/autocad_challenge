from converters.BaseConverter import BaseConverter
import config as cfg
import ezdxf
from ezdxf.addons import odafc
import utils.utils as utils

class AutoCADConverter(BaseConverter):

    """
        Class to convert a given file to the formats supported by AutoCAD
    """

    def __init__(self):

        super().__init__(to_types=["dxf", "dwg"])

    def convert(self, csv_file_obj, selected_to_type, file_name):

        # Creating a new document
        doc = ezdxf.new(dxfversion=cfg.autocad_settings['file_version'],
                        setup=cfg.autocad_settings['setup_standard_drawing_styles'])

        # Creating drawing with the contents of CSV filee
        msp = doc.modelspace()
        psp = doc.layout('Layout1')

        for index, row in csv_file_obj.iterrows():
            """
                This suffices for the given use case. Definitely need to expand for different shapes like say circle.
                Also such information needs to be captured in the CSV either implicitly or explicitly
            """
            msp.add_line(tuple(row.values[2:5]), tuple(row.values[5:8]), dxfattribs={'layer': 'MyLayer'})

        # Check if results dir exists
        utils.check_and_create_dir(cfg.general["results_path"])

        save_file_as = cfg.general["results_path"] + "/" + file_name
        if selected_to_type == 'dxf':
            doc.saveas(save_file_as + ".dxf")
        elif selected_to_type == 'dwg':
            odafc.export_dwg(doc, save_file_as + '.dwg', version='R2018')