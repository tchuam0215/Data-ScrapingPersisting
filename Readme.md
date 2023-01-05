# Scraping data from https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html  and persist them in csv, json format and sqlite, mysql database

## Steps : 

1) Scrap data from the websites : https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html
	- download the websites in a .html file

2) Persists the data in 
	- csv file format 
	- json file format
	- sqlite embebbed database 
	- mysql database

3) Load the data into mysql database 
4) Delete the data into mysql database
5) Reload the data into a new database

## To run the project in the bash command :
- $ scrapy crawl CveScrapping 
- then you check data in json and csv file

you can also do : 
- sqlite3 vulnerabilities.db
- select * from vulnerabilities

to check the data are correctly added to sqlite embebbed vulnerabilities.db database 
