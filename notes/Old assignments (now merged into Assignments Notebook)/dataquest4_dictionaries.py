weather = ['Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Sunny', 'Fog', 'Rain', 'Sunny', 'Sunny',
           'Sunny', 'Sunny', 'Sunny', 'Fog', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Rain', 'Fog-Rain',
           'Rain', 'Fog-Rain', 'Rain', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Fog', 'Fog',
           'Sunny', 'Sunny', 'Rain', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Sunny', 'Sunny', 'Fog',
           'Sunny', 'Rain', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny',
           'Sunny', 'Rain', 'Fog', 'Fog', 'Sunny', 'Rain', 'Rain', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Fog', 'Fog',
           'Fog', 'Fog', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Sunny', 'Sunny', 'Fog', 'Sunny', 'Fog',
           'Fog', 'Fog', 'Fog', 'Rain', 'Sunny', 'Fog', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog',
           'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Fog', 'Fog',
           'Sunny', 'Rain', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Fog', 'Sunny', 'Sunny', 'Rain',
           'Rain', 'Rain', 'Sunny', 'Thunderstorm', 'Fog', 'Sunny', 'Fog', 'Sunny', 'Fog', 'Fog', 'Sunny', 'Sunny',
           'Sunny', 'Sunny', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Fog',
           'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Sunny', 'Sunny',
           'Fog', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Fog', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny',
           'Fog', 'Fog', 'Fog', 'Fog', 'Fog', 'Sunny', 'Fog', 'Fog', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Sunny', 'Sunny',
           'Fog', 'Sunny', 'Fog-Rain', 'Fog', 'Fog', 'Sunny', 'Fog', 'Sunny', 'Fog', 'Fog', 'Fog', 'Sunny', 'Rain',
           'Fog', 'Fog', 'Fog', 'Fog', 'Fog-Rain', 'Sunny', 'Sunny', 'Fog', 'Sunny', 'Sunny', 'Fog', 'Fog', 'Sunny',
           'Sunny', 'Fog', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Fog', 'Fog', 'Fog', 'Fog', 'Fog',
           'Fog', 'Fog', 'Fog', 'Fog', 'Sunny', 'Fog', 'Fog', 'Fog', 'Fog', 'Sunny', 'Fog', 'Fog', 'Fog', 'Sunny',
           'Sunny', 'Fog', 'Sunny', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Fog', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Fog', 'Fog',
           'Sunny', 'Fog', 'Fog', 'Fog', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Sunny', 'Sunny', 'Sunny',
           'Sunny', 'Sunny', 'Sunny', 'Fog', 'Sunny', 'Fog', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Rain', 'Sunny',
           'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Fog', 'Fog', 'Fog', 'Sunny',
           'Sunny', 'Fog', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog',
           'Sunny', 'Sunny', 'Fog', 'Fog', 'Sunny', 'Fog', 'Fog', 'Sunny', 'Sunny', 'Fog', 'Sunny', 'Sunny', 'Fog',
           'Sunny', 'Rain', 'Rain', 'Rain', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Rain', 'Sunny',
           'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog',
           'Fog', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Sunny',
           'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Fog', 'Fog', 'Fog']

print(weather[0])
print(weather[len(weather) - 1])

# Dictionary Practice
dict1 = {}
dict1["one"] = 1
dict1["two"] = 2
print(dict1)

dict2 = {"one": 1, "two": 2, "three": 3}
print(dict2)

# Practice
superhero_ranks = {}
superhero_ranks["Aquaman"] = 1
superhero_ranks["Superman"] = 2
print(superhero_ranks)

# Look up in dictionary
president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3

fdr_rank = president_ranks["FDR"]
aquaman_rank = president_ranks["Aquaman"]
lincoln_rank = president_ranks["Lincoln"]

print(fdr_rank, aquaman_rank, lincoln_rank)

# Adding multiple values to dictionaries
random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}
print(random_values)

animals = {
    7: "raven",  # 7 is the KEY, "raven" is the VALUE
    8: "goose",
    9: "duck"
}

times = {
    "morning": 9,
    "afternoon": 14,
    "evening": 19,
    "night": 23
}

# Modifying dictionary values
students = {
    "Tom": 60,
    "Jim": 70
}
students["Ann"] = 85
students["Tom"] = 80
students["Jim"] = students["Jim"] + 5

print(students)

# Using 'in' in dictionaries
planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}

jupiter_found = "jupiter" in planet_numbers
print(jupiter_found)

earth_found = "earth" in planet_numbers
print(earth_found)

# Else statement
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]

short_names = []  # shorter than 5 characters
long_names = []  # longer than 5 characters

for i in planet_names:
    if len(i) <= 5:
        short_names.append(i)
    else:
        long_names.append(i)

print(short_names + [" are the short names"])
print(long_names + [" are the long names"])

# Counting
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]

pantry_counts = {}

for i in pantry:
    if i not in pantry_counts:
        pantry_counts[i] = 1  # initialize
    else:
        pantry_counts[i] = pantry_counts[i] + 1

print(pantry_counts)

# Counting 2

weather = [
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Rain',
    'Sunny',
    'Sunny',
    'Fog',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Rain',
    'Fog-Rain',
    'Rain',
    'Fog-Rain',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Rain',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Rain',
    'Fog',
    'Fog',
    'Sunny',
    'Rain',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Rain',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Sunny',
    'Rain',
    'Rain',
    'Rain',
    'Sunny',
    'Thunderstorm',
    'Fog',
    'Sunny',
    'Fog',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Fog-Rain',
    'Fog',
    'Fog',
    'Sunny',
    'Fog',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Rain',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Fog-Rain',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Rain',
    'Rain',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Rain',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Sunny',
    'Fog',
    'Fog',
    'Fog'
]
weather_counts = {}

for i in weather:
    if i not in weather_counts:
        weather_counts[i] = 1
    else:
        weather_counts[i] = weather_counts[i] + 1

print(weather_counts)

