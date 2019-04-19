from ValidationRule import ValidationRule


class StringRule(ValidationRule):
    def __init__(self, attributeName, attributeData, args=[]):
        super().__init__(attributeName, attributeData, args)

    def isValid(self):
        return isinstance(self.get_attributeData(), str)

    def getValidationDefaultMessage(self):
        return "The %s field must be a valid String" % self.get_attributeName()
