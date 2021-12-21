# Python Dictionary Validation Rules

This package helps you to validate a dictionary based on some rules that you define.
Check this exmple
```bash
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
    'author.haha': 'required'
}
customAttribute = {
    'title': 'New Title',
    'author.dob': 'Date of birth'
}
customErrorMessages = {
    'pages.max': 'You shouldn\'t exceed 30 for pages'
}
x = DataValidator(data, rules, customAttribute, customErrorMessages)
print(x.getErrorMessages())
print(x.isValidData())
print(x.getFaildAttributes())
```
