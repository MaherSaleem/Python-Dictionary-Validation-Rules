from ValidationRule import ValidationRule


class NumberRule(ValidationRule):
    def __init__(self, attributeName, attributeData, args=[]):
        super().__init__(attributeName, attributeData, args)

    def isValid(self):
        return isinstance(self.get_attributeData(), (int, float, complex))

    def getValidationDefaultMessage(self):
        return "The %s field must be a number" % self.get_attributeName()
