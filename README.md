# Data Cleaning : USDA- NASS


<B> About data:</B> <br>
This project involves  data cleaning and munging of the dataset from <B> United States Department of Agriculture </B> -National Agriculture Statistics Service.<br> 

Data is available for download [here](https://quickstats.nass.usda.gov) <br>
Glossary is available to view [here](https://quickstats.nass.usda.gov/src/glossary.pdf) <br>

### <b><u>Methodology and Approach:</b></u> <br>

The data cleaning process begins with: <br>
1. Understanding how big the dataset is (the downloaded file is 6.5 GB), so we would have to process it by in chunks and then  cleaning it further.<br>
2. Project requirement includes the following:<br>
a. the data is to be included from 1990 till current year <br>
b. the essential crops to be included are  Corn, Wheat, Rice, Soy and Cotton<br>
c. include county level data <br>

<b>About the project structure: </b> <br>
 There are 2 files in the project:<br>
 1. Jupyter Notebook: NASS QuickStats data .ipynb - for step by step representation of the cleaning process with the output <br>
 2. Python file: Nass_data.py <br> - replication of jupyter notebook for compact code with compact and cleaner code<br>


<b>Steps involved:</b><br>

1. <b>Data Chunking</b> : <br> 
a. This process involves processing the data in smaller chunks of a large file. One chunk with a specific size is processed and then appened to the masterdata set. <br>
b. In this step of my code, I have divided the data into multiple chunks with each of size 1000 and iterating over it till it reaches the end chunk and the process is complete. <br>
c. Additionally, I am filtering the dataset for only years <b>1990-present</b> so that operation is faster and the master dataset becomes smaller.<br>
d. The output of this process is a masterdata set with the data filtered out of years before 1990.<br>

2. <b>Data Profiling:</b><br> 
a. This step is very crucial for understanding nature the variables in the dataset by collecting statistics or informative, such as count of uniques, number of nulls in a categorical variable.<br>
b. Functions involved in the profiling are: unique(), describe(), info() to understand the structure of the dataset.<br>

3. <b> Data Filtering: </b><br>
a. Filtering out the data based on identification the categories of a column that we would like to filter; crops, geographic level etc.<br>
b. <i> Important point to note here is that filtering involves in the reduction of row count but the columns count remains intact.</i><br>
 
4. <b> Data Restructuring and Data Munging</b><br>
a. This is the last step of the data cleaning process which involves the selection of columns for the cleaned dataset.<br>
b. The columns can be dropped if :<br>
- the columns have one category <br>
- if 70% of the data in the column is Null, Not Available,or Not Applicable, Not Recorded <br>
- the entire column is NaN <br>
c. After the <b>selection</b> of columns that are to be included in the dataset, the remaining columns can be dropped.<br>
d. Once I have the final set of columns to be included, we can <b>restructure</b> the dataset based on the hierarchy if any,
eg: Geographic level (State, county, ASD etc).<br>
e. Once I have the dataset ready I then <b>sort</b> the data based on year just before the final export.<br>
f. Lastly, I have exported the cleaned dataset to the desired location in a .csv file. (~480 MB) <br>
  
<b><i>Note: In all the above steps, I have used df.shape() to ensure changes in the data structure are consistent.</b></i><br>
