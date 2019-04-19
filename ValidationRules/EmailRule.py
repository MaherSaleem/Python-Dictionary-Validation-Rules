from ValidationRule import ValidationRule
import re


class EmailRule(ValidationRule):
    def __init__(self, attributeName, attributeData, args=[]):
        super().__init__(attributeName, attributeData, args)

    def isValid(self):
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return not not EMAIL_REGEX.match(self.email)

    def getValidationDefaultMessage(self):
        return "The %s field must be a valid Email" % self.get_attributeName()

    @property
    def email(self):
        return self.get_attributeData()
