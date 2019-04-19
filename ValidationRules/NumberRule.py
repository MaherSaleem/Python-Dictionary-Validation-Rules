from ValidationRule import ValidationRule


class NumberRule(ValidationRule):
    def __init__(self, attribute_name, attribute_data, args=[]):
        super().__init__(attribute_name, attribute_data, args)

    def is_valid(self):
        return isinstance(self.get_attribute_data(), (int, float, complex))

    def get_validation_default_message(self):
        return "The %s field must be a number" % self.get_attribute_name()
