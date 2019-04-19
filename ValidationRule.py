class ValidationRule():

    def __init__(self, attribute_name, attribute_data, args=[]):
        self._attribute_name = attribute_name
        self._attribute_data = attribute_data
        self._args = args

    def is_valid(self):
        raise NotImplementedError('subclasses must override validateAttributeData()!')

    def get_validation_default_message(self):
        raise NotImplementedError('subclasses must override getValidationMessage()!')

    '''
        Setters and getters
    '''

    def get_attribute_name(self):
        return self._attribute_name

    def get_attribute_data(self):
        return self._attribute_data

    def get_args(self):
        return self._args

    def set_attribute_name(self, attribute_name):
        self._attribute_name = attribute_name

    def set_attribute_data(self, attribute_data):
        self._attribute_data = attribute_data

    def set_args(self, args):
        self._args = args
