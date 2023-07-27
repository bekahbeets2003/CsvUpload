# CsvUpload
Allow a user to upload a csv file, parse contents, and store in mysql db

# Setup
This project pushes and pulls to a mysql db as a rdbms.  <br />
	- You will need to edit the connection string in db_data file <br />
	- In the directory 'Sql', I have included the scripts to create the tables, sprocs, and seed data. These will need created before running the program 


# Tables
Vendors <br />
Users <br />
User_File_Uploads <br />

# Csv expectations
Id (string) <br />
Cost (float) <br />
Quantity (int) <br />

# Process
A basic form allows the users to upload a file, with the vendor name. Field validation is added. <br />
An Ajax command checks the file for the right ext type and then calls the api command <br />
The api is written in python with flask and asyncio packages/modules <br />
The api converts the csv to json, validates the 'values' in the kvp's and then pushes to the database by calling the sproc for an insert <br />
The form shows results of the file upload or an error as returned to it by python <br />