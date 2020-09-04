from converter.BaseConverter import BaseConverter

class RevitConverter(BaseConverter):

    """
        Class to convert a given file to the formats supported by Revit
    """

    def __init__(self):

        super(RevitConverter).__init__(to_types=["dxf", "dwg"])