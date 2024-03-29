# writing dictionaries to a file

import json

some_large_arbitrary_json = {
    'foo': 'bar',
    'year': 1996,
    'meaning': 'nothing',
    'subject': 'philosophy',
    'website': 'Yahoo Answers',
    'intent': 'good',
    'age': 67,
    'template_engine': 'hugo',
    'racecar': 'racecar',
    'frames': 60,
    'watch': 'titan',
    'climate': 'humid',
    'temperature': '30C',
    'character': 'Red Riding Hood',
    'fruit': 'apple',
    'colour': 'yellow',
    'location': 'Somewhere in the World',
    'editor': 'VS Code',
    'story': "The Hitchhiker's Guide to the Galaxy",
    'author': 'John',
    'with_list': ['1st item', '2nd item', '3rd item', '4th item', '5th item', '6th item']
}

fp = open('3.example.json', 'w')

json.dump(some_large_arbitrary_json, fp)

fp.close()

fp1 = open('3.example.pretty.json', 'w')

json.dump(some_large_arbitrary_json, fp1, indent=4)

fp1.close()