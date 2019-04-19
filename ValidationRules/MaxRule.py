from ValidationRule import ValidationRule


class MaxRule(ValidationRule):
    def __init__(self, attributeName, attributeData, args):
        super().__init__(attributeName, attributeData, args)
        self._args = list(map(int, self._args))

    def isValid(self):
        return self.get_attributeData() <= self.get_attributeData()

    def getValidationDefaultMessage(self):
        return "The %s field must at max %s" % (self.get_attributeName(), self.maxValue)

    @property
    def maxValue(self):
        return self.get_args()[0]
