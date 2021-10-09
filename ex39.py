states = {
    'oregon': 'or',
    'florida': 'fl',
    'california': 'ca',
    'new york': 'ny',
    'michigan': 'mi'
}

cities = {
    'ca': 'san francisco',
    'mi': 'detroit',
    'fl': 'jacksonville'
}

cities['ny'] = 'new york'
cities['or'] = 'portland'

print(cities)
print(cities.items())
print(cities['ca'])
print(cities.get('ca'))