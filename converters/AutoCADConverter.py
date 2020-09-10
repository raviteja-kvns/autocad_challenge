from converters.BaseConverter import BaseConverter
import config as cfg
import ezdxf
from ezdxf.addons import odafc
import utils.utils as utils
import math


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
            # Line object 1: Wall one - True measurements
            p1 = row.values[2:5]
            p2 = row.values[5:8]
            aa = msp.add_line(tuple(p1), tuple(p2), dxfattribs={'layer': 'MyLayer'})

            # Parallel Line Object 2: With thickness
            delta = self._get_detla_for_wall_thickness(p1, p2)
            msp.add_line(tuple(p1 - delta), tuple(p2 - delta), dxfattribs={'layer': 'MyLayer'})

            # Short segments to close the figure wall
            msp.add_line(tuple(p1), tuple(p1 - delta), dxfattribs={'layer': 'MyLayer'})
            msp.add_line(tuple(p2), tuple(p2 - delta), dxfattribs={'layer': 'MyLayer'})


        # Check if results dir exists
        utils.check_and_create_dir(cfg.general["results_path"])

        save_file_as = cfg.general["results_path"] + "/" + file_name
        if selected_to_type == 'dxf':
            doc.saveas(save_file_as + ".dxf")
        elif selected_to_type == 'dwg':
            odafc.export_dwg(doc, save_file_as + '.dwg', version='R2018')

    def _get_detla_for_wall_thickness(self, p1, p2):

        """
            Compute Delta for Wall thickness
            as the offset would be only along x,y jointly or either just x or y
        :return:
        """
        thickness = cfg.model_preferences["default_wall_thickness"]
        delta = None
        if p1[0] == p2[0]:
            # Line along Y axis -> offset x
            delta = [thickness, 0, 0]
        elif p1[1] == p2[1]:
            # Line along X axis -> offset y
            delta = [0, thickness, 0]
        else:
            # Spread the thickness along x and y proportionately
            slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
            slope_of_perpendicular = -1/slope
            theta = math.atan(slope_of_perpendicular)

            delta = [math.cos(theta) * thickness, math.sin(theta) * thickness, 0]

        return delta