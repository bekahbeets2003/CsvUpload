import json
import csv


def convert_csv_to_json(csv_file):
    with open(csv_file, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        data = []
        for row in reader:
            dict_row = {'model_number': row[0], "unit_price": row[1], "quantity": row[2]}
            data.append(dict_row)

    json_data = json.dumps(data)

    return json_data


def write_json_to_dir(output_file_path, json_data):
    with open(output_file_path, "w") as f:
        f.write(json_data)


'''def convert_csv_to_json_file(csv_file_path, json_file_path):
    with open(csv_file_path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        data = []
        for row in reader:
            data.append({key: value for key, value in zip(reader.fieldnames, row)})

    with open(json_file_path, "w") as jsonfile:
        json.dump(data, jsonfile)'''
