# Jonard Bolante
# Jul 14, 2020

import bs4
import datetime
import io
import csv
from urllib.request import Request, urlopen    
from bs4 import BeautifulSoup as soup           

# SETTING UP MY URL WITH BEAUTIFULSOUP TO PARSE
myURL = 'https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?#countries'
urlClient = Request(myURL, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(urlClient).read()         
urlopen(urlClient).close()
pageSoup = soup(webpage, "html.parser") 

#I NARROWED DOWN THE HTML TO THE TABLE I NEED. NOW ALL I NEED ARE TO CAPTURE THE TABLE ROWS
bodyTable = pageSoup.find("table", id="main_table_countries_yesterday")    
tableData = bodyTable.tbody.find_all("tr")          
rowInfoList = []    
tempArray = []

# OPENING/CREATING MY CSV FILE
filename = datetime.datetime.now().strftime("Countries %B %d %Y.csv")
directory = "C:\\Users\\Master Jonard\\Documents\\JONARD - Coronavirus EXCEL Sheets\\"+filename
file = open(directory, "w+") 
writer = csv.writer(file)

# WRITING MY HEADER ROWS
writer.writerow(['   ', 'Country', 'Total Cases', 'New Cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'Active Cases', 'Serious, Critical', 'Total Cases/1M pop', 'Deaths/1M pop', 'Total Tests', 'Tests/1M pop', 'Population'])

# POPULATING MY CSV FILE ROW-BY-ROW
for i in range(len(tableData)):
    if (tableData[i].find_all("td")[0].string == None):       
        continue                                              
    tempArray.append(tableData[i].find_all("td")[0].string) if (tableData[i].find_all("td")[0].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[1].string) if (tableData[i].find_all("td")[1].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[2].string) if (tableData[i].find_all("td")[2].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[3].string) if (tableData[i].find_all("td")[3].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[4].string) if (tableData[i].find_all("td")[4].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[5].string) if (tableData[i].find_all("td")[5].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[6].string) if (tableData[i].find_all("td")[6].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[7].string) if (tableData[i].find_all("td")[7].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[8].string) if (tableData[i].find_all("td")[8].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[9].string) if (tableData[i].find_all("td")[9].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[10].string) if (tableData[i].find_all("td")[10].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[11].string) if (tableData[i].find_all("td")[11].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[12].string) if (tableData[i].find_all("td")[12].string != None) else tempArray.append(" ")
    tempArray.append(tableData[i].find_all("td")[13].string) if (tableData[i].find_all("td")[13].string != None) else tempArray.append(" ")
    writer.writerow([tempArray[0], tempArray[1], tempArray[2], tempArray[3], tempArray[4], tempArray[5], tempArray[6], tempArray[7], tempArray[8], tempArray[9], tempArray[10], tempArray[11], tempArray[12], tempArray[13]])
    rowInfoList.append(tempArray)
    tempArray = []

# PRINTING MY DATA IN CONSOLE TO CHECK IF I HAVE RECEIVED THE CORRECT INFORMATION
file.close()
for myArray in rowInfoList:
    print(myArray)
    print("\n")










# This function will get data from states within the US
def getUSAstates():
    myURL = 'https://www.worldometers.info/coronavirus/country/us/'
    urlClient = Request(myURL, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(urlClient).read()
    urlopen(urlClient).close()
    pageSoup = soup(webpage, "html.parser")    
    bodyTable = pageSoup.find("table", id="usa_table_countries_yesterday")
    tableData = bodyTable.tbody.find_all("tr")
    rowInfoList = []   
    tempArray = []

    filename = datetime.datetime.now().strftime("USA States %B %d %Y.csv")
    directory = "C:\\Users\\Master Jonard\\Documents\\JONARD - Coronavirus EXCEL Sheets\\"+filename
    file = open(directory, "w+") 
    writer = csv.writer(file)
    writer.writerow(["USA State", "Total Cases", "New Cases", "Total Deaths", "New Deaths", "Active Cases", "Total Cases/1M pop", "Deaths/1M pop", "Total Tests", "Tests/1M pop"])

    for i in range(len(tableData)):
        if (i==0):
            tempArray.append(tableData[i].find_all("td")[0].string) if (tableData[i].find_all("td")[0].string != None) else tempArray.append(" ")
        else:
            tempArray.append(tableData[i].find_all("td")[0].find_all("a")[0].string)
        tempArray.append(tableData[i].find_all("td")[1].string) if (tableData[i].find_all("td")[1].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[2].string) if (tableData[i].find_all("td")[2].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[3].string) if (tableData[i].find_all("td")[3].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[4].string) if (tableData[i].find_all("td")[4].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[5].string) if (tableData[i].find_all("td")[5].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[6].string) if (tableData[i].find_all("td")[6].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[7].string) if (tableData[i].find_all("td")[7].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[8].string) if (tableData[i].find_all("td")[8].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[9].string) if (tableData[i].find_all("td")[9].string != None) else tempArray.append(" ")
        writer.writerow([tempArray[0], tempArray[1], tempArray[2], tempArray[3], tempArray[4], tempArray[5], tempArray[6], tempArray[7], tempArray[8], tempArray[9]])
        rowInfoList.append(tempArray)
        tempArray = []

    file.close()
    for myArray in rowInfoList:
        print(myArray)
        print(" ")







# This function will get data from each County within New Jersey
def getNewJerseyCounty():
    myURL = 'https://www.worldometers.info/coronavirus/usa/new-jersey/'
    urlClient = Request(myURL, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(urlClient).read()
    urlopen(urlClient).close()
    pageSoup = soup(webpage, "html.parser")    
    bodyTable = pageSoup.find("table", id="usa_table_countries_yesterday")
    tableData = bodyTable.tbody.find_all("tr")
    rowInfoList = []   
    tempArray = []

    filename = datetime.datetime.now().strftime("New Jersey County %B %d %Y.csv")
    directory = "C:\\Users\\Master Jonard\\Documents\\JONARD - Coronavirus EXCEL Sheets\\"+filename
    file = open(directory, "w+") 
    writer = csv.writer(file)

    writer.writerow(["County", "Total Cases", "New Cases", "Total Deaths", "New Deaths", "Active Cases", "Total Tests"])

    for i in range(len(tableData)):
        if (i==0):
            tempArray.append(tableData[0].find_all("td")[0].find_all("nobr")[0].string)
        else:
            tempArray.append(tableData[i].find_all("td")[0].string) if (tableData[i].find_all("td")[1].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[1].string) if (tableData[i].find_all("td")[1].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[2].string) if (tableData[i].find_all("td")[2].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[3].string) if (tableData[i].find_all("td")[3].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[4].string) if (tableData[i].find_all("td")[4].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[5].string) if (tableData[i].find_all("td")[5].string != None) else tempArray.append(" ")
        tempArray.append(tableData[i].find_all("td")[6].string) if (tableData[i].find_all("td")[6].string != None) else tempArray.append(" ")
        writer.writerow([tempArray[0], tempArray[1], tempArray[2], tempArray[3], tempArray[4], tempArray[5], tempArray[6]])
        rowInfoList.append(tempArray)
        tempArray = []

    file.close()
    for myArray in rowInfoList:
        print(myArray)
        print(" ")




getUSAstates()
getNewJerseyCounty()

#  TO-DO
# • [DONE] Create a shell/bash script to run this python file every 24hrs   ---> I used Windows Task Scheduler
# • [DONE] Save the CSV file at a specific location 
# • [DONE] Allow Python to change the name of the CSV file to "CORONAVIRUS" followed by [the date]
# • [DONE] (This should solve the problem for creating new files with different names daily)
# • [DONE] Create 2 more excel sheets for USA states, and New Jersey County
