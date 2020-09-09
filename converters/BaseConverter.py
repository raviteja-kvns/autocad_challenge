class BaseConverter:

    def __init__(self, to_types):
        """

        :param to_type: The type to which we would like to convert the file
        :param from_type: The type of the source file. eg. .csv etc.
        """

        self.to_types = to_types

    def is_type_supported(self, file_type):

        return file_type in self.to_types

    def convert(self, csv_file_obj, selected_to_type):
        raise NotImplementedError
