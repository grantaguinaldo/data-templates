import pandas as pd
import datetime
from sys import argv

def app(file_name):
		
	'''
	This script takes data in wide format and reshapes the file into
	long format.

	Input file must be the following format:
		GNN_ID
		BA_ID
		READ_BUSINESS_DT in YYYY-MM-DD	
		READ_VALUE_THM_0000 ... READ_VALUE_THM_2300 

	When running this app from CLI, enter "python app.py <file name of input file including extension>"

	As an example, for a file name of "export_2019_01_01.csv" enter the following in command line:
		python app.py export_2019_01_01.csv 

	Be sure that export_2019_01_01.csv and app.py are in the same directory. 

	'''

	df1 = pd.read_csv(file_name)

	print('File received sucessfully.')

	df1['READ_BUSINESS_DT'] = pd.to_datetime(df1['READ_BUSINESS_DT'], format='%Y/%m/%d')

	df_melt = pd.melt(df1, id_vars=df1.columns.tolist()[:3], value_vars=df1. \
			  columns.tolist()[3:]).sort_values(by=['GNN_ID', 'READ_BUSINESS_DT'])

	df_melt.rename(columns={'variable': 'TIME_', 'value': 'USAGE_VALUE', 'GNN_ID': \
			  'SERVICE_POINT_ID', 'BA_ID': 'ACCOUNT_ID'}, inplace=True)

	print('Working.')

	df_melt['TIME'] = df_melt['TIME_'].str.split('_').apply(lambda x: x[-1])

	df_melt['IS_ESTIMATE'] = 'E'
	df_melt['UNITS'] = 'THERMS'
	df_melt['DAYLIGHT_SAVINGS'] = 'PST'

	df_melt['DATE'] = df_melt['READ_BUSINESS_DT'].apply(lambda x: x.strftime('%Y%m%d'))

	df_final_list = ['SERVICE_POINT_ID','ACCOUNT_ID',
	                 'USAGE_VALUE', 'DATE', 'TIME',
	                 'UNITS', 'IS_ESTIMATE', 'DAYLIGHT_SAVINGS',]

	df_final = df_melt[df_final_list].sort_values(by=['SERVICE_POINT_ID', 'DATE', \
			 'TIME']).reset_index(drop=True)

	customer_list = df_final.ACCOUNT_ID.unique().tolist()

	print('Working.')

	for each in customer_list:
	    df_final[df_final['ACCOUNT_ID'] == each].sort_values(by=['ACCOUNT_ID', \
	                'DATE', 'TIME']).reset_index(drop=True).to_csv('account_id_' + \
	                str(each) + '_export.csv', index=False)

	print('Done with reshaping data file.')

if __name__ == '__main__':
	app(argv[1])