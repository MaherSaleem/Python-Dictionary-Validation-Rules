

class ValidationRule():

    def __init__(self, attributeName, attributeData, args=[]):
        self._attributeName = attributeName
        self._attributeData = attributeData
        self._args = args


    def isValid(self):
        raise NotImplementedError('subclasses must override validateAttributeData()!')

    def getValidationDefaultMessage(self):
        raise NotImplementedError('subclasses must override getValidationMessage()!')

    '''
        Setters and getters
    '''

    def get_attributeName(self):
        return self._attributeName

    def get_attributeData(self):
        return self._attributeData

    def get_args(self):
        return self._args

    def set_attributeName(self, attributeName):
        self._attributeName = attributeName

    def set_attributeData(self, attributeData):
        self._attributeData = attributeData

    def set_args(self, args):
        self._args = args
