from DataValidator import DataValidator


data = {
    "title": 121,
    "author": {
        "name": "Maher",
        "dob": "11/01/1996",
        "email": "maher@birzeit.edu",
        "friends": ["Chandler", "Monica", "Joey"],
    },
    "pages": 50,
    "creation_date": "15-12-2015"
}

rules = {
    "pages": "number|min:20|max:30",
    "title": "string",
    "creation_date": "date",
    'author.friends': 'array',
    'author.dob': 'date',
}
customAttribute = {
    'title': 'New Title',
    'author.dob': 'Date of birth'
}
x = DataValidator(data, rules, customAttribute)
print(x.getErrorMessages())
print(x.isValidData())
print(x.getFaildAttributes())
