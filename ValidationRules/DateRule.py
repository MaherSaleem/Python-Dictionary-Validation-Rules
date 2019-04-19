from ValidationRule import ValidationRule
import datetime


class DateRule(ValidationRule):
    def __init__(self, attribute_name, attribute_data, args=[]):
        super().__init__(attribute_name, attribute_data, args)

    def is_valid(self):
        try:
            datetime.datetime.strptime(self.get_attribute_data(), '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def get_validation_default_message(self):
        return "The %s field must a valid date" % (self.get_attribute_name())
