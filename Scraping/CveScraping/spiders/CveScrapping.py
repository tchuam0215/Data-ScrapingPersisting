import scrapy
import csv
import json 
import os
import sqlite3

path = os.getcwd()
parent_dir = os.path.abspath(os.path.join(path, os.pardir))
current_dir = os.path.dirname(__file__)
url = os.path.join(parent_dir, "source-EXPLOIT-DB.html")

print(os.path.join(current_dir, "source-EXPLOIT-DB.html"))

print(url)
print("Current directory -->", current_dir)
print("Parent directory -->", parent_dir)
print("Start url -->", [f"file:///{url}"])

# persisting data in csv format
# persisting data in json format
# persisting data in mysql format

class CvescrappingSpider(scrapy.Spider):
    name = 'CveScrapping'
    allowed_domains = ['cve.mitre.org']
    # start_urls = ['https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html']
    start_urls = [f"file:///{url}"]

    def parse(self, response):
        for table in response.xpath("//table"):
            if len(table.xpath("//tr")) > 100:
                tbRow=table
                break
        # csv 
        count = 0
        csv_file = open("vulnerabilities.csv", "w", newline="")
        json_file = open("vulnerabilities.json", "w")
        
        writer = csv.writer(csv_file)
        writer.writerow(["EXPLOIT-ID", "CVE-ID"])

        #json 
        data = {}

        #json
        connection = sqlite3.connect("vulnerabilities.db")
        table = "CREATE TABLE vuln(exploit TEXT, cve TEXT)"
        cursor = connection.cursor()
        cursor.execute(table)
        connection.commit()

        for tbColumn in tbRow.xpath("//tr"):
            if count > 100 :
                break
            try:
                exploit_id =  tbColumn.xpath("td//text()")[0].extract()
                print(exploit_id)
                cve_id = tbColumn.xpath("td//text()")[2].extract()
                print(cve_id)
                data[exploit_id] = cve_id
                json.dump(data, json_file)

                cursor.execute('INSERT INTO vuln(exploit, cve) VALUES(?, ?)', (exploit_id, cve_id))
                connection.commit()

                writer.writerow([exploit_id, cve_id])
                count +=1
            except IndexError:
                pass
        csv_file.close()
        json_file.close()
