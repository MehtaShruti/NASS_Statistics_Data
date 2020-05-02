#-----author: Shruti Mehta 04-30-2020---#
#-----Cleaning and preprocessing of NASSQuick Stats data---#


#package imports
import pandas as pd
import csv
from datetime import date 
from datetime import datetime


#-------------------------------------------------------------#
#----function helps to clean and preprocess the source file---#
#----to generate cleaner dataset as output file---------------#
#-------------------------------------------------------------#

def cleansing_prep():
	
	# source file path  
	file_path = 'data/qs.crops_20200429.txt'
	chunksize = 1000 
	df_chunks = []

	#iterate over the file and process with limited chunk at a time and repeat the process
	for df in pd.read_csv(file_path, chunksize=chunksize, iterator=True, sep='\t',low_memory=False):
	    
	    # taking year >=1990 from the dataset
	    df_f = df.loc[(df['YEAR']>=1990)]
	    
	    # append the processed chunk with the list of chunks 
	    df_chunks.append(df_f)

	    #concatenating the processed chunk into master dataframe
	master_df = pd.concat(df_chunks)

	#list of crops 
	crops = ['WHEAT', 'RICE','COTTON','CORN','SOYBEANS']

	# to check the list of crops against the data in the dataset
	master_df.COMMODITY_DESC.isin(crops)

	#filtering the rows with the crops in the master dataframe
	filter_crops= master_df[master_df.COMMODITY_DESC.isin(crops)]

	# list of statistic categories
	category = ['AREA PLANTED','AREA HARVESTED','PRODUCTION','YIELD']

	# to check the list of statistic categories against the data in the dataset
	filter_crops.STATISTICCAT_DESC.isin(category)
	
	#filtering the rows with the statistic categories in the master dataframe
	filter_category= filter_crops[filter_crops.STATISTICCAT_DESC.isin(category)]


	#only county level data
	region = ['COUNTY']
	
	# to filter the dataset with the county level data
	filter_category.AGG_LEVEL_DESC.isin(region)

	#filtering the rows with the region county  in the master dataframe
	filter_region= filter_category[filter_category.AGG_LEVEL_DESC.isin(region)]


	# column selection to reduce the size of the dataset
	# other columns were filtered out based on the 
	# 1. missing data (more than 90%), 2. unnecessary columns  
	filter_region=filter_region.drop(columns=['SECTOR_DESC','GROUP_DESC','DOMAINCAT_DESC','STATE_ANSI',
                              'STATE_FIPS_CODE','STATE_ALPHA','CONGR_DISTRICT_CODE','WATERSHED_DESC',
                              'WATERSHED_CODE','COUNTRY_CODE','BEGIN_CODE','END_CODE','LOAD_TIME','REFERENCE_PERIOD_DESC',
                            'WEEK_ENDING','SOURCE_DESC','ASD_CODE','ZIP_5'])

    #column renaming for readability                            
	filter_region.rename(columns={'COMMODITY_DESC': 'FIELD_CROPS',
                                'CLASS_DESC': 'CROP_TYPE',
                                'PRODN_PRACTICE_DESC':'PRODN_PRACTICE',
                                'UTIL_PRACTICE_DESC':'UTILIZATION',
                                'STATISTICCAT_DESC':'CATEGORY',
                                'UNIT_DESC':'UNIT',
                                'SHORT_DESC':'ACTIVITY',
                                'DOMAIN_DESC':'DOMAIN',
                                'AGG_LEVEL_DESC':'GEOGRAPHIC_LEVEL',
                                'ASD_DESC':'AGRICULTURAL_DISTT',
                                'FREQ_DESC':'FREQUENCY',
                                'VALUE':'UNIT_VALUE',
                                'CV_%':'CV%'
                                },inplace=True)

	#resturcture the dataframe in the order of columns of heirarchy
	filter_region=filter_region[['YEAR','GEOGRAPHIC_LEVEL','COUNTRY_NAME','STATE_NAME','AGRICULTURAL_DISTT','REGION_DESC','LOCATION_DESC',
                            'COUNTY_ANSI', 'COUNTY_CODE','COUNTY_NAME', 'FIELD_CROPS', 'CROP_TYPE', 'PRODN_PRACTICE', 'UTILIZATION', 'CATEGORY',
                            'ACTIVITY', 'DOMAIN', 'FREQUENCY','UNIT','UNIT_VALUE', 'CV%']]


	
	#sort values based year
	sorted_data=filter_category.sort_values(['YEAR'])
	
	#return the processed dataframe
	return sorted_data



if __name__== "__main__":

	print('------------Cleaning data set-----------')

	#call the function for cleaning and preprocessing
	sorted_data=cleansing_prep()

	print('------------Exporting the processed dataset in file-------')
	
	#get current time
	now = datetime.now()

	#convert it to string to append to the filename
	current_time=now.strftime("%m-%d-%Y,%H-%M-%S")

	# export the file to the desired location
	sorted_data.to_csv('data_exports/cleaned_data'+current_time+'.csv')
	




