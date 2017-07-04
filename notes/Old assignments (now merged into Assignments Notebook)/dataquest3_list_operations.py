datainit = open("la_weather.csv", "r")
data = datainit.read()

data

data_with_rows = data.split("\n")
data_with_rows

weather_data = []

for i in data_with_rows:
    x = i.split(',')
    weather_data.append(x)

##### Append each weather type to a separate variable
weather = []

for i in weather_data:
    weather.append(i[1])
print(weather)


# Count the number of elements in weather_data manually
count = 0
for i in weather_data:
    count = count + 1
print(count)


# Slice the weather list to remove the header
new_weather = weather[1:len(weather)]


#### IN Exercise ####

animals = ['cat', 'dog', 'rabbit', 'horse', 'giant_horrible_monster']

cat_found = "cat" in animals
space_monster_found = "space_monster" in animals


# Check whether each of the weather_types elements are in the weather_new
weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for i in new_weather:
    for j in weather_types:
        if (i == j) & (i not in weather_type_found):
            weather_type_found.append("True")
print(weather_type_found)