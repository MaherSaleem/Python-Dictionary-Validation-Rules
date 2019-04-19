from ValidationRule import ValidationRule


class StringRule(ValidationRule):
    def __init__(self, attribute_name, attribute_data, args=[]):
        super().__init__(attribute_name, attribute_data, args)

    def is_valid(self):
        return isinstance(self.get_attribute_data(), str)

    def get_validation_default_message(self):
        return "The %s field must be a valid String" % self.get_attribute_name()
