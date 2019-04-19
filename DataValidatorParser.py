import DataValidator


class DataValidatorParser():

    def __init__(self, dataValidator: DataValidator):
        self.dataValidator = dataValidator
        self.parsedDataList = []

    def getParsedRules(self):
        rules = self.dataValidator.get_rules()
        data = self.dataValidator.get_data()
        customAttributes = self.dataValidator.get_customAttribute()
        for attributeName, validationRules in rules.items():
            shownAttributeName = self.getAttributeName(attributeName, customAttributes)
            for validationRule in validationRules.split('|'):
                rule, args = self.getRuleAndArgs(validationRule)
                self.parsedDataList.append({
                    'attributeName': shownAttributeName,
                    'attributeData': data[attributeName],
                    'validationRule': rule,
                    'args': args
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
