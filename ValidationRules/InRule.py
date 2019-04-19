from ValidationRule import ValidationRule


class InRule(ValidationRule):
    def __init__(self, attributeName, attributeData, args=[]):
        super().__init__(attributeName, attributeData, args)

    def isValid(self):
        return self.get_attributeData() in self.given_list

    def getValidationDefaultMessage(self):
        return "The %s field must be one of these %s" % (self.get_attributeName(), ','.join(self.given_list))

    @property
    def given_list(self):
        return self.get_args()
