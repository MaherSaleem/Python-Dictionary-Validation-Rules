from ValidationRule import ValidationRule
import datetime


class DateRule(ValidationRule):
    def __init__(self, attributeName, attributeData, args=[]):
        super().__init__(attributeName, attributeData, args)

    def isValid(self):
        try:
            datetime.datetime.strptime(self.get_attributeData(), '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def getValidationDefaultMessage(self):
        return "The %s field must a valid date" % (self.get_attributeName())
