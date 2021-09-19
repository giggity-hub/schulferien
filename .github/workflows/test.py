# f = open("demo.txt", "a")
# f.write("sheeeeesh\n")
import os
import csv
import json
# print(os.listdir('Schulferien'))

ferien_dict = {}

directory = 'Schulferien'
for year in os.listdir('Schulferien'):
    year_directory = os.path.join(directory, year)
    ferien_dict[year] = {}

    for bundesland_csv in os.listdir(year_directory):
        bundesland_path = os.path.join(year_directory, bundesland_csv)
        bundesland_code = bundesland_csv.split('.')[0]

        with open(bundesland_path, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, skipinitialspace=True)
            
            def addBundesland(row):
                row['bundesland'] = bundesland_code
                return row
 
            ferien_dict[year][bundesland_code] = [addBundesland(row) for row in reader]

print(json.dumps(ferien_dict, sort_keys=True, indent=4))