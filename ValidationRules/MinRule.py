from ValidationRule import ValidationRule


class MinRule(ValidationRule):
    def __init__(self, attributeName, attributeData, args=[]):
        super().__init__(attributeName, attributeData, args)
        self._args = list(map(int, self._args))

    def isValid(self):
        return self.get_attributeData() >= self.minValue

    def getValidationDefaultMessage(self):
        return "The %s field must at least %s" % (self.get_attributeName(), self.minValue)

    @property
    def minValue(self):
        return self.get_args()[0]
