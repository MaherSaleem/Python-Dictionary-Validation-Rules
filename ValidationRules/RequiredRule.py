from ValidationRule import ValidationRule


class RequiredRule(ValidationRule):
    def __init__(self, attribute_name, attribute_data, args=[]):
        super().__init__(attribute_name, attribute_data, args)

    def is_valid(self):
        return self.get_attribute_data() is not None and self.get_attribute_data() != ""

    def get_validation_default_message(self):
        return "The %s field is required" % self.get_attribute_name()
