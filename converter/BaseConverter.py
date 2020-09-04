class BaseConverter:

    def __init__(self, to_types):
        """

        :param to_type: The type to which we would like to convert the file
        :param from_type: The type of the source file. eg. .csv etc.
        """

        self.to_types = to_types

    def _is_type_supported(self, file_type):

        return file_type in self.to_types

    def _build_standardized_representation(self):

        """
            Builds standardized representation from CSV or the file inputted
            to be used as input to library
        :return: representation
        """

        raise NotImplementedError

    def convert(self, file_obj):
        raise NotImplementedError
