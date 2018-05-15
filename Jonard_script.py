#This imports all the
import sys
import csv
import os.path
import xml.dom.minidom
document = xml.dom.minidom.parse(sys.argv[1])
mainElements = document.getElementsByTagName('main')
data = []
state = sys.argv[2]
city = sys.argv[3]
data.append(state)
data.append(city)

# # Gets the State
# for h4 in mainElements[0].getElementsByTagName('h4'):
#     for a in h4.getElementsByTagName('a'):
#         for node in a.childNodes:
#             if node.nodeType == node.TEXT_NODE:
#                 myString = node.nodeType
#                 data.append(node.nodeValue)
#                 myString = (data[0][-2:])
#                 data.append(myString)
#                 data.pop(0)
#         break
# #print(data[0])


# # Gets the City
# for h2 in mainElements[0].getElementsByTagName('h2'):
#     for node in h2.childNodes:
#         if node.nodeType == node.TEXT_NODE:
#             data.append(node.nodeValue)
#             myString = data[1][0:13]
#             data.append(myString)
#             data.pop(1)
# #    print(','.join(data))
#     break

temperature = document.getElementsByTagName("h1") #gets all the elements that have h1 as tag name
temperature = temperature[1].firstChild.nodeValue # goes to 2nd element in h1 (which is 94)
data.append(temperature[0:2])


weather = document.getElementsByTagName("h4")
weather = weather[2].firstChild.nodeValue
data.append(weather)


humidity = document.getElementsByTagName("td")
humidity = humidity[1].firstChild.nodeValue.strip().split("%")[0]
data.append(humidity)


pressure = document.getElementsByTagName("td")
pressure = pressure[5].firstChild.nodeValue.strip().split(" ")[0].strip()[:-5]
data.append(pressure)

#This prints all the elements in my data, and is separated by commas
print(','.join(data))

headers = ["State", "City", "Weather", "Temperature", "Humidity", "Pressure"]


with open("JonardsAwesomeData.csv", "a") as myJonardsCSV_file:
    # if not file_exists:
    #     writer.writeheader()
    # writer.writerow({'State ': data[0], 'City ': data[1], 'Weather ': data[3], 'Temperature ': data[4], 'Humidity ': data[5], 'Pressure ': data[6]})
    fileEmpty = os.stat('JonardsAwesomeData.csv').st_size == 0
    writer = csv.DictWriter(myJonardsCSV_file, delimiter=',', lineterminator='\n', fieldnames=headers)
    if fileEmpty:
        writer.writeheader()
    myWriter = csv.writer(myJonardsCSV_file)
    myWriter.writerow(data)
