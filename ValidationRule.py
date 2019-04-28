class ValidationRule():

    def __init__(self, attribute_name, attribute_data, args=[], custom_error_message=None):
        self._attribute_name = attribute_name
        self._attribute_data = attribute_data
        self._args = args
        self._custom_error_message = custom_error_message

    def is_valid(self):
        raise NotImplementedError('subclasses must override validateAttributeData()!')

    def get_validation_default_message(self):
        raise NotImplementedError('subclasses must override getValidationMessage()!')

    def get_error_message(self):
        if self.get_custom_error_message() is None:
            return self.get_validation_default_message()
        else:
            return self.get_custom_error_message()

    '''
        Setters and getters
    '''

    def get_attribute_name(self):
        return self._attribute_name

    def get_attribute_data(self):
        return self._attribute_data

    def get_args(self):
        return self._args

    def get_custom_error_message(self):
        return self._custom_error_message

    def set_attribute_name(self, attribute_name):
        self._attribute_name = attribute_name

    def set_attribute_data(self, attribute_data):
        self._attribute_data = attribute_data

    def set_args(self, args):
        self._args = args

    def set_custom_error_message(self, custom_error_message):
        self._custom_error_message = custom_error_message
