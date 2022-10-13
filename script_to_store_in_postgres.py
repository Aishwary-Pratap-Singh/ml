# Python program to demonstrate
# Conversion of JSON data to
# dictionary


# importing the module
import json

def open_json():
	table = dict()
	table['id'] = []
	table['ques'] = []
	# Opening JSON file
	with open('question.json') as json_file:
		data = json.load(json_file)

		# Print the type of data variable
		print("Type:", type(data))

		# Print the data of dictionary
		cnt = 1
		for title in data["items"]:
			# print(title["title"])
			table['ques'].append(title["title"])

			table['id'].append(cnt)
			cnt += 1

		return table

import pandas as pd
def dict_to_df(data):

	df = pd.DataFrame.from_dict(data)
	print(df)
	return df

from sqlalchemy import create_engine

def insert_df_into_postgres(df):


	import sqlalchemy as sa

	db_name = "dna1"
	db_user = "postgres"
	db_pwd = "Password@123"
	db_host = "localhost"
	db_client = "postgresql"

	connection_url = sa.engine.URL.create(
		drivername=db_client,
		username=db_user,
		password=db_pwd,
		host=db_host,
		database=db_name
	)


	db = create_engine(connection_url)
	conn = db.connect()

	df.to_sql('question', con=conn, if_exists='replace',
			  index=False)


data_dict = open_json()
df = dict_to_df(data_dict)
insert_df_into_postgres(df)