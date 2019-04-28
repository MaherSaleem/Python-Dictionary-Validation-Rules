import DataValidator
import helpers


class DataValidatorParser():

    def __init__(self, dataValidator: DataValidator):
        self.dataValidator = dataValidator
        self.parsedDataList = []

    def getParsedRules(self):
        rules = self.dataValidator.get_rules()
        data = self.dataValidator.get_data()
        customErrorMessages = self.dataValidator.get_customErrorMessage()
        customAttributes = self.dataValidator.get_customAttribute()
        for attributeName, validationRules in rules.items():
            shownAttributeName = self.getAttributeName(attributeName, customAttributes)
            for validationRule in validationRules.split('|'):
                rule, args = self.getRuleAndArgs(validationRule)
                customErrorMessage = self.getErrorMessage(attributeName, rule, customErrorMessages)
                self.parsedDataList.append({
                    'attributeName': shownAttributeName,
                    'attributeData': helpers.getDictValue(data, attributeName),
                    'validationRule': rule,
                    'args': args,
                    'errorMessage': customErrorMessage
                })
        return self.parsedDataList

    def getRuleAndArgs(self, validationRule: str):
        s = validationRule.split(':')
        if len(s) == 1:
            return s[0], []
        else:
            return s[0], list(s[1].split(','))

    def getAttributeName(self, attributeName, customAttributes):
        if attributeName in customAttributes:
            return customAttributes[attributeName]
        else:
            return attributeName

    def getErrorMessage(self, attributeName, ruleName, customAttributes):
        customeErrorName = "{}.{}".format(attributeName, ruleName)
        if customeErrorName in customAttributes:
            return customAttributes[customeErrorName]
        else:
            return None
