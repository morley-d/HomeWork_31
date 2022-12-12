"""
Преобразование CSV файлов в JSON формат
"""

import csv
import json


def csv_to_json(csv_file_path, json_file_path):
    jsonArray = []
    # read csv file
    with open(csv_file_path, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            pk = int(row["id"])
            # model_name = "users.location"
            model_name = "users.user"
            # model_name = "ads.ads"
            # model_name = "ads.category"
            row.pop("id")
            # if row["is_published"] == "TRUE":
            #     row["is_published"] = True
            # elif row["is_published"] == "FALSE":
            #     row["is_published"] = False
            # row["price"] = int(row["price"])
            # row["author_id"] = int(row["author_id"])
            # row["category_id"] = int(row["category_id"])
            row["age"] = int(row["age"])
            row["location_id"] = int(row["location_id"])
            # row["lat"] = float(row["lat"])
            # row["lng"] = float(row["lng"])
            new_row = {
                "model": model_name,
                "pk": pk,
                "fields": row
            }
            jsonArray.append(new_row)

    # convert python jsonArray to JSON String and write to file
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)


# csv_file_path = r'datasets/location.csv'
# json_file_path = r'fixtures/location.json'

csv_file_path = r'datasets/user.csv'
json_file_path = r'fixtures/user.json'

# csv_file_path = r'datasets/ad.csv'
# json_file_path = r'fixtures/ad.json'

# csv_file_path = r'datasets/categories.csv'
# json_file_path = r'fixtures/categories.json'

csv_to_json(csv_file_path, json_file_path)
