from ValidationRule import ValidationRule
import re


class PhoneRule(ValidationRule):
    def __init__(self, attribute_name, attribute_data, args=[]):
        super().__init__(attribute_name, attribute_data, args)

    def is_valid(self):
        phoneRegex = re.compile(r"\+.{12}")
        return not not phoneRegex.match(self.phone_number)

    def get_validation_default_message(self):
        return "The %s field must be a number" % self.get_attribute_name()

    @property
    def phone_number(self):
        return self.get_attribute_data()
