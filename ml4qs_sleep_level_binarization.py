
import csv
from pprint import pprint
from preprocessor.select_column import select_column
from preprocessor.append_column import append_column

data = list(csv.reader(open("C://Code//DMT//data//ml4qs_preprocessed//dataset2_sequential_imped.csv", encoding="UTF8"), delimiter=","))

#pprint(data[0:5])

sleep_stage_column =  select_column("sleep_stage", data)
print(set(sleep_stage_column))

sleep_stage_0_column = []
for each_row in sleep_stage_column:
    if each_row == '0':
        sleep_stage_0_column.append('1')
    else:
        sleep_stage_0_column.append('0')


sleep_stage_1_column = []
for each_row in sleep_stage_column:
    if each_row == '1':
        sleep_stage_1_column.append('1')
    else:
        sleep_stage_1_column.append('0')

sleep_stage_2_column = []
for each_row in sleep_stage_column:
    if each_row == '2':
        sleep_stage_2_column.append('1')
    else:
        sleep_stage_2_column.append('0')

sleep_stage_3_column = []
for each_row in sleep_stage_column:
    if each_row == '3':
        sleep_stage_3_column.append('1')
    else:
        sleep_stage_3_column.append('0')

sleep_stage_nan_column = []
for each_row in sleep_stage_column:
    if each_row == 'nan':
        sleep_stage_nan_column.append('1')
    else:
        sleep_stage_nan_column.append('0')

append_column(sleep_stage_0_column,"sleep_stage_0", data)
append_column(sleep_stage_1_column,"sleep_stage_1", data)
append_column(sleep_stage_2_column,"sleep_stage_2", data)
append_column(sleep_stage_3_column,"sleep_stage_3", data)
append_column(sleep_stage_nan_column,"sleep_stage_nan", data)

pprint(data)


output_file_location_and_name = "data//ml4qs_preprocessed//binarized_dataset2_sequential_imped.csv"
file = open(output_file_location_and_name, 'w', newline='')
writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
for row in data[0:len(data)]:
    writer.writerow(row)
file.close()

print("Binarized ataset written to:", output_file_location_and_name)
