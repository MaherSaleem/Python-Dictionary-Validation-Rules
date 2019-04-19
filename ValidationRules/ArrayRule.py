from ValidationRule import ValidationRule


class ArrayRule(ValidationRule):
    def __init__(self, attribute_name, attribute_data, args=[]):
        super().__init__(attribute_name, attribute_data, args)

    def is_valid(self):
        return isinstance(self.get_attribute_data(), (list,))

    def get_validation_default_message(self):
        return "The %s field must be an array" % self.get_attribute_name()
