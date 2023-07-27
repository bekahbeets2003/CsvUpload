import asyncio
import random
import pyodbc

# connect to sql server on localhost with windows auth
# this would normally go in a secrets file for security
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    r'SERVER={server name}};'
    'DATABASE=csv_upload;'
    'TrustedConnection=yes'
)
conn.autocommit = True
cursor = conn.cursor()


async def get_user():
    # loop = asyncio.get_event_loop()
    # result = loop.run_in_executor(None, cursor.execute('select * from csv_users'))
    # loop.run_until_complete(result)
    # loop.close()
    mock_user_id = random.randint(1000, 1002)
    data = []
    # sql = 'exec usp_csv_get_user'
    sql = 'select * from csv_users where user_id = {0}'.format(mock_user_id)
    cursor.execute(sql)
    if cursor.description is not None:
        data = list(cursor.fetchone())

    return data


async def get_vendors():
    data = []
    sql = 'exec usp_csv_get_vendors'
    cursor.execute(sql)
    if cursor.description is not None:
        data = cursor.fetchall()

    return data


def insert_file(user_id, vendor_id, upload_date, network_json_file_location):
    sql = 'exec usp_csv_insert_file @p_user_id=?, @p_vendor_id=?, @p_upload_date=?, @p_network_file_location=?'
    params = (user_id, vendor_id, upload_date, network_json_file_location)
    cursor.execute(sql, params)
    ret_val = cursor.fetchall()

    return ret_val


# convert Rows to lists
def convert_rows_to_list(list_of_rows):
    desired_list = []
    for row in list_of_rows:
        desired_list.append(list(row))

    return desired_list

# x = asyncio.run(get_user())
# print(x)
