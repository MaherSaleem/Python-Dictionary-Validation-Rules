from ValidationRule import ValidationRule
import re


class PhoneRule(ValidationRule):
    def __init__(self, attributeName, attributeData, args=[]):
        super().__init__(attributeName, attributeData, args)

    def isValid(self):
        phoneRegex = re.compile(r"\+.{12}")
        return not not phoneRegex.match(self.phoneNumber)

    def getValidationDefaultMessage(self):
        return "The %s field must be a number" % self.get_attributeName()

    @property
    def phoneNumber(self):
        return self.get_attributeData()
