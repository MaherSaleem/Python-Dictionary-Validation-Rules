from ValidationRule import ValidationRule


class NumberRule(ValidationRule):
    def __init__(self, *args):
        super().__init__(*args)

    def is_valid(self):
        return isinstance(self.get_attribute_data(), (int, float, complex))

    def get_validation_default_message(self):
        return "The %s field must be a number" % self.get_attribute_name()
