from ValidationRule import ValidationRule


class ArrayRule(ValidationRule):
    def __init__(self, *args):
        super().__init__(*args)

    def is_valid(self):
        return isinstance(self.get_attribute_data(), (list,))

    def get_validation_default_message(self):
        return "The %s field must be an array" % self.get_attribute_name()
