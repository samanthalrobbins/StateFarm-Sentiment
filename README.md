# StateFarm-Sentiment

Remove-Unnecessary branch holds the files to remove data that was deemed unnecessary for the sentiment analysis. 

File removerows.py is the python file that removes the data. Includes, State Farm account, employees, and spam accounts. 
As well as unwanted data, such as User_ID, links, and tweets not in English. 

It runs the data_full.csv which is all the mined Twitter data for 2019. 

File base_data.csv is the new removed dataset. 
