import os
from flask import *
from flask_cors import CORS
import json
import asyncio
import mssql_da as db
import generate_json_file as file_conversion
import file_validation as file_validation

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
async def load_defaults():
    return_dict = {}
    list_user = []
    list_vendors = []

    # list report names by facility and user
    list_user_task = asyncio.create_task(db.get_user())
    list_vendors_task = asyncio.create_task(db.get_vendors())

    # get data - comes back as type Row
    list_user_rows = await list_user_task
    list_vendors_rows = await list_vendors_task

    # convert task rows to lists, as json is incompatible with type 'Row'
    list_user = list_user_rows
    list_vendors = db.convert_rows_to_list(list_vendors_rows)

    # add returned data to for conversion to json
    return_dict["user"] = list_user
    return_dict["vendors"] = list_vendors

    # list to json
    json_dump = json.dumps(return_dict)

    # return json
    return json_dump


@app.route('/upload', methods=['POST'])
async def upload():
    try:
        csv_file = request.files['file']

        # raises ValueError if not csv
        file_validation.check_file_ext(csv_file.filename)

        # set file location
        network_csv_file_location = "./uploads/" + csv_file.filename
        csv_file.save(network_csv_file_location)

        str_json_data = file_conversion.convert_csv_to_json(network_csv_file_location)

        # convert to json
        json_data = json.loads(str_json_data)

        # check for missing values
        file_validation.check_for_empty_vals(json_data)

        # convert values to correct types because they all come in as string
        file_validation.convert_val_types(json_data)

        # write json to file
        filename_without_ext = os.path.splitext(csv_file.filename)[0]
        network_json_file_location = "./uploads_json/" + filename_without_ext + '.json'
        file_conversion.write_json_to_dir(network_json_file_location, json.dumps(json_data))

        # get the other request values from form
        user_id = int(request.form["user_id"])
        upload_date = request.form["date"]
        vendor_id = int(request.form["vendor_id"])

        # send to mssql
        full_file_path = os.path.join(os.getcwd(), "uploads_json\\" + filename_without_ext + '.json')
        db.insert_file(user_id, vendor_id, upload_date, full_file_path)

        # return
        return "The files were uploaded successfully."
    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)

# do the testing...
if __name__ == '__main__':
    app.run(port=7774)
