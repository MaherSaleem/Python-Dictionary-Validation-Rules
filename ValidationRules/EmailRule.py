from ValidationRule import ValidationRule
import re


class EmailRule(ValidationRule):
    def __init__(self, *args):
        super().__init__(*args)

    def is_valid(self):
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return not not EMAIL_REGEX.match(self.email)

    def get_validation_default_message(self):
        return "The %s field must be a valid Email" % self.get_attribute_name()

    @property
    def email(self):
        return self.get_attribute_data()
