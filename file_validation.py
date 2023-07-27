import os


# Checks if the file ext is CSV.
# Args: file_name: The name of the file.
# Raises: ValueError: If the file ext is not CSV.
def check_file_ext(file_name):
    file_ext = os.path.splitext(file_name)[1]
    if file_ext != ".csv":
        raise ValueError("File ext is not CSV.")


def check_for_empty_vals(list_of_dicts):
    for i, dict_ in enumerate(list_of_dicts):
        for key, value in dict_.items():
            if value == "":
                raise ValueError('Line ' + str(i + 1) + ' has a missing value')


def convert_val_types(list_of_dicts):
    for i, dict_ in enumerate(list_of_dicts):

        if type(dict_['model_number']) != str:
            dict_['model_number'] = str(dict_['model_number'])

        if type(dict_['unit_price']) != float:
            dict_['unit_price'] = float(dict_['unit_price'])

        if type(dict_['quantity']) != int:
            dict_['quantity'] = int(dict_['quantity'])
