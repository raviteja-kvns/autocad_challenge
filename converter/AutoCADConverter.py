from converter.BaseConverter import BaseConverter
from pyautocad import Autocad, APoint

class AutoCADConverter(BaseConverter):

    """
        Class to convert a given file to the formats supported by AutoCAD
    """

    def __init__(self):

        super(AutoCADConverter).__init__(to_types=["rvt", "rfa"])

    def convert(self, file_obj):

        pass

    def _build_standardized_representation(self, file_obj):

        a_cad = Autocad()