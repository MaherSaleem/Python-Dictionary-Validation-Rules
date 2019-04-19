from DataValidator import DataValidator

data = {
    "title": 121,
    "author": {
        "name": "Maher",
        "dob": "11/01/1996",
        "email": "maher@birzeit.edu",
        "friends": ["Chandler", "Monica", "Joey"]
    },
    "pages": 50,
    "creation_date": "15/12/2015"
}

rules = {
    "pages": "max:70",
    "title": "string",
}
customAttribute = {
    'title': 'New Title'
}
x = DataValidator(data, rules, customAttribute)
print(x.getErrorMessages())
print(x.isValidData())
print(x.getFaildAttributes())
