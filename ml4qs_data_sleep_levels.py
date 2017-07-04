import json
from pprint import pprint
input_file_location_and_name = "data//ml4qs_raw//june sleep levels 2.txt"
with open(input_file_location_and_name) as data_file:
    data = json.load(data_file)

#pprint(data)
#print("the length is", len(data["sleep"][0]["levels"]))
#print(data["sleep"][0]["levels"][0])

dataset_interday_sleep_records = []
for each_instance in data["sleep"]:
    dataset_interday_sleep_records.extend(each_instance["levels"]["data"])

#pprint(dataset_interday_sleep_records)


id = 17
vector_interday_sleep_dates            = []
vector_interday_sleep_levels           = []
vector_interday_sleep_level_durations  = []


for each_row in dataset_interday_sleep_records:
 vector_interday_sleep_dates.append(each_row["dateTime"])
 vector_interday_sleep_levels.append(each_row["level"])
 vector_interday_sleep_level_durations.append(each_row["seconds"])

#print(vector_interday_sleep_dates)
#print(vector_interday_sleep_levels)
#print(vector_interday_sleep_level_durations)
#
#
#

from datetime import datetime
vector_interday_sleep_level_datetimes = []
for each_date in vector_interday_sleep_dates:
    #vector_interday_sleep_level_datetimes.append(datetime.datetime.strptime(each_date, "%Y-%m-%dT%H:%M:%S.%f")) #This full version is omitted
    current_datetime = datetime.strptime(each_date, "%Y-%m-%dT%H:%M:%S.000") # Convert string to datetime for flexible manipulation
    current_datetime = current_datetime.replace(second=00)
    current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] # Convert datetime back to string format that is compatible with Mark's code.
    vector_interday_sleep_level_datetimes.append(current_datetime)

#print(vector_interday_sleep_level_datetimes)

#print(len(vector_interday_sleep_level_datetimes), vector_interday_sleep_level_datetimes)
#print(len(vector_interday_sleep_levels), vector_interday_sleep_levels)
#print(len(vector_interday_sleep_level_durations), vector_interday_sleep_level_durations)
#
#print(set(vector_interday_sleep_levels))
