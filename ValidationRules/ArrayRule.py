from ValidationRule import ValidationRule


class ArrayRule(ValidationRule):
    def __init__(self, attributeName, attributeData, args=[]):
        super().__init__(attributeName, attributeData, args)

    def isValid(self):
        return isinstance(self.get_attributeData(), (list,))

    def getValidationDefaultMessage(self):
        return "The %s field must be an array" % self.get_attributeName()
