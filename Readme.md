## Scrapping website data a persisting it in csv, json, sqlite and mysql


# Steps : 

1) Scrap data from the websites : https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html
	- download the websites in a .html file

2) Persiste the data in 
	- csv file 
	- json file 
	- sqlite embebbed database 
	- mysql database

3) Load the data into mysql database 
4) Delete the data into mysql database
5) Reload the data into a new database

To run the project : 

in the bash command :
$ scrapy crawl CveScrapping 
# then you check data in json and csv file

you can also : 
# sqlite3 vulnerabilities.db
# select * from vulnerabilities