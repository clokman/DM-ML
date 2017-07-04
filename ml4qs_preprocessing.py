# TODO

from math import isnan


ids_list = list(range(170608, 170629))

# these are initial headers, and some will be removed dynamically, while some others will be added in the code later.
headers = ["instance_code", "date", "total_steps_day", "time_of_day", "steps_this_minute", "heartrate_this_minute"]
dataset_global = [headers]

no_of_imputed_values = 0

for each_id in ids_list:

    ###################################################################
    #                       STEPS DATA                                #
    ###################################################################

    #----------------------------------------------------
    # Read json into variable
    #----------------------------------------------------

    import json
    from pprint import pprint

    input_file_location_and_name = "data//ml4qs_raw//" + str(each_id) + " activity.txt"
    with open(input_file_location_and_name) as data_file:
        data = json.load(data_file)

    #pprint(data)


    #-----------------------------------------------------------------
    # Parse date and total number of steps
    #-----------------------------------------------------------------

    string_day_date = data["activities-steps"][0]["dateTime"]
    count_total_steps_day = data["activities-steps"][0]["value"]

    #-----------------------------------------------------------------
    # Parse number of steps within a day, and their times (per minute)
    #-----------------------------------------------------------------

    data_intraday_steps = data["activities-steps-intraday"]["dataset"]

    # Iterate over data_intraday_steps and create two vectors for steps and their times
    vector_intraday_steps_counts       = []
    vector_intraday_steps_times = []
    for each_row in data_intraday_steps:
        vector_intraday_steps_counts.append(each_row["value"])
        vector_intraday_steps_times.append(each_row["time"])

    ###################################################################
    #                          HR DATA                                #
    ###################################################################

    #-----------------------------------------------------------------
    # Import file to variable
    #-----------------------------------------------------------------

    input_file_location_and_name = "data//ml4qs_raw//" + str(each_id) + " bpm.txt"
    with open(input_file_location_and_name) as data_file:
        data = json.load(data_file)

    #pprint(data)
    dataset_hr_intraday = data["activities-heart-intraday"]["dataset"]

    #-----------------------------------------------------------------
    # Parse heartrate to a variable
    #-----------------------------------------------------------------

    vector_intraday_hr_values       = []
    vector_intraday_hr_values_times = []
    for each_row in dataset_hr_intraday:
        vector_intraday_hr_values.append(each_row["value"])
        vector_intraday_hr_values_times.append(each_row["time"])

    #-----------------------------------------------------------------
    # Missing values
    #-----------------------------------------------------------------

    #--------- Build a list that has all minutes of the day -----------#
    hours_int = list(range(0,24))
    hours_str = []
    for each_hour in hours_int:
        each_hour_str = str(each_hour)
        if len(each_hour_str) == 1:
            each_hour_str = "0" + each_hour_str
        hours_str.append(each_hour_str)

    minutes_int = list(range(0,60))
    minutes_str = []
    for each_minute in minutes_int:
        each_minute_str= str(each_minute)
        if len(each_minute_str) == 1:
            each_minute_str= "0" + each_minute_str
        minutes_str.append(each_minute_str)

    vector_all_day_minutes= []
    for each_hour in hours_str:
        for each_minute in minutes_str:
            vector_all_day_minutes.append(each_hour + ":" + each_minute + ":00")

    #------------ Add missing values and minutes when a minute is missing from HR ----------#
    for i, each_minute in enumerate(vector_all_day_minutes):
        try:
            if vector_all_day_minutes[i] != vector_intraday_hr_values_times[i]:
                vector_intraday_hr_values_times.insert(i, vector_all_day_minutes[i])
                vector_intraday_hr_values.insert(i, float("NaN"))
        except IndexError: #If index out of range, hr minutes do not go till the end of day. Add these missing values.
            vector_intraday_hr_values_times.append(vector_all_day_minutes[i])
            vector_intraday_hr_values.append(float("NaN"))

    #------------------ Impute missing values with interpolation ---------------------------#
    for i, each_value in enumerate(vector_intraday_hr_values):
        if isnan(each_value): # if value is a NaN value.
            try:
                # if previous and next values are also not a NaN, impute.
                if not isnan(vector_intraday_hr_values[i-1]) and not isnan(vector_intraday_hr_values[i+1]):
                    vector_intraday_hr_values[i] = (vector_intraday_hr_values[i-1] + vector_intraday_hr_values[i+1]) / 2
                    no_of_imputed_values += 1
            except IndexError:
                pass # in case the previous or next value does not exist, then just pass

    # Prevent steps data to have unhandled missing data (it was left alone due to the assumption that it is always complete)
    if len(vector_intraday_hr_values_times) < len(vector_all_day_minutes):
        raise Exception("Unhandled missing data exists in vector_steps. Because steps data is assumed to be have no missing time steps, it is not processed for missing data. Please process.")


    ###################################################################
    #                       CREATE THE DATASET                        #
    ###################################################################

    #-----------------------------------------------------------------
    # Create local dataset (based on only one file)
    #-----------------------------------------------------------------

    dataset_local_combined = [] # this variable is refreshed with each iteration of the main for loop
    for i, each_row in enumerate(data_intraday_steps):
        dataset_local_combined.append([str(each_id), string_day_date, count_total_steps_day, vector_intraday_steps_times[i], vector_intraday_steps_counts[i], vector_intraday_hr_values[i]])


    # ---------------------------------------------------------------------------------
    # Aggregate data files as rows to create global dataset (all files entered as rows)
    # ---------------------------------------------------------------------------------
    for each_row in dataset_local_combined:  # this updates the global dataset that is outside the main loop
        dataset_global.append(each_row)


##############################################################################
#     COMBINE DATE and TIME_OF_DAY VARIABLES INTO A DATETIME COLUMN          #
##############################################################################
# Note: From this point on, values will be adressed with database functions (e.g., select_column)
# ... rather than rather than calling vector variables defined as before.

import datetime
from preprocessor.select_column import select_column
from preprocessor.append_column import append_column
from preprocessor.remove_columns import remove_columns

dates_column        = select_column("date", dataset_global)
time_of_day_column  = select_column("time_of_day", dataset_global)

datetimes_string_vector = []
for each_date, each_time in zip(dates_column,time_of_day_column):
    datetimes_string_vector.append(each_date + "T" + each_time)

# Convert to datetime type
datetimes_vector = []
for each_string_datetime in datetimes_string_vector:
    current_datetime_object = datetime.datetime.strptime(each_string_datetime, "%Y-%m-%dT%H:%M:%S")
    # Convert back from datetime type into a string format compatible with Mark's libraries
    # Format that must be adhered: <2017-06-14 11:20:40.121>
    current_compatible_string_datetime = current_datetime_object.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    datetimes_vector.append(current_compatible_string_datetime)

#print("datetime", datetimes_vector)

append_column(datetimes_vector,"datetime", dataset_global)
remove_columns(["date", "time_of_day"], dataset_global)

#pprint(dataset_global)

###################################################################
#                        SLEEP DATA                               #
###################################################################

from ml4qs_data_sleep_levels import vector_interday_sleep_level_datetimes
from ml4qs_data_sleep_levels import vector_interday_sleep_levels
from ml4qs_data_sleep_levels import vector_interday_sleep_level_durations

#print("sleep datetimes", vector_interday_sleep_level_datetimes)
#print("sleep levels", vector_interday_sleep_levels)

datetime_column                         = select_column("datetime", dataset_global)
sleep_levels_column                     = []
sleep_level_durations_column_in_minutes = []

# Create a placeholder vector for later inserting sleep levels at approproate rows that correspond to sleep level dates
for each_item in datetime_column:
    sleep_levels_column.append("NA")
    sleep_level_durations_column_in_minutes.append(float("NaN"))

# Insert sleep levels at appropriate rows based on their match with dates and times in datetime column
bad_values = []
for i, each_sleep_level_datetime in enumerate(vector_interday_sleep_level_datetimes):
    try:
        current_index = datetime_column.index(each_sleep_level_datetime) # Find at what index position the date from the new dataset occurs in the main dataset
    except:
        import warnings
        warnings.warn("Operation finished but datetime below are not found. Two datasets end at different dates (or ids_list variable stops at an earlier id)?")
        print("Warning: Value not found: ", each_sleep_level_datetime)
    sleep_levels_column[current_index] = vector_interday_sleep_levels[i] # Place the sleep level value at the index position that corresponds to it's date in the main dataset
    sleep_level_durations_column_in_minutes[current_index] = round(int(vector_interday_sleep_level_durations[i] / 60), 0)
#print(sleep_levels_column)


# Extrapolate values

for i, each_sleep_level in enumerate(sleep_levels_column):
    if each_sleep_level in set(vector_interday_sleep_levels):
        try:
            current_target_index = i  # assignment not needed, but done for clarity of code below
            current_window_size = sleep_level_durations_column_in_minutes[current_target_index]  # Calculate how many seconds the sleep level's duration covers
            for current_step in range(1, current_window_size):  # Assign the same sleep level value to x rows that follow it, x being duration of the sleep level.
                if sleep_levels_column[current_target_index + current_step] not in set(vector_interday_sleep_levels): # Stop the filling operation if a row already has value!
                    sleep_levels_column[current_target_index + current_step] = each_sleep_level  # Otherwise, just extrapolate the previous sleep level value for its duration
                    sleep_level_durations_column_in_minutes[current_target_index + current_step] = current_window_size - current_step
        except:
            print("Skipped sleep value extrapolation at index (probably a NA value, and that's OK):", i)


append_column(sleep_levels_column, "sleep_level_labeled", dataset_global)

from preprocessor.transform_column_values import transform_column_values
sleep_level_numerical_temp = select_column("sleep_level_labeled", dataset_global)
append_column(sleep_level_numerical_temp, "sleep_level_numerical", dataset_global)
conversion_dictionary = {
    'rem'       :0,
    'deep'      :1,
    'light'     :2,
    'asleep'    :3,
    'wake'      :4,
    'awake'     :5,
    'restless'  :6,
    "NA"        :7, # The old NaN values are now 7 to reflect "non-sleeping"
}

transform_column_values(conversion_dictionary, "sleep_level_numerical", dataset_global)

append_column(sleep_level_durations_column_in_minutes, "sleep_level_duration_remaining", dataset_global)

print("Data Preview")
pprint(dataset_global[0:50])
print("Number of imputed missing values:", no_of_imputed_values)

#print(type(select_column("steps_this_minute", dataset_global)[2]))

#-----------------------------------------------------------------
# Output to .csv
#-----------------------------------------------------------------
import csv
from preprocessor.select_column import select_column

output_file_location_and_name = "data//ml4qs_preprocessed//dataset_global.csv"
file = open(output_file_location_and_name, 'w', newline='')
writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
for row in dataset_global[0:len(dataset_global)]:
    writer.writerow(row)
file.close()

print("Final dataset written to:", output_file_location_and_name)
## Check if the written dataset is the same with the one in the memory:
#test_data = list(csv.reader(open(output_file_location_and_name, encoding="utf8"), delimiter=";"))
#
#print(len(dataset_global) == len(test_data))
#print(select_column("steps_this_minute", dataset_local_combined) == select_column("steps_this_minute", test_data))
