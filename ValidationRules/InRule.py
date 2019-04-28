from ValidationRule import ValidationRule


class InRule(ValidationRule):
    def __init__(self, *args):
        super().__init__(*args)

    def is_valid(self):
        return self.get_attribute_data() in self.given_list

    def get_validation_default_message(self):
        return "The %s field must be one of these %s" % (self.get_attribute_name(), ','.join(self.given_list))

    @property
    def given_list(self):
        return self.get_args()
