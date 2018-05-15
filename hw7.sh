#!bin/bash/sh

NY=`date '+%Y-%m-%d-%H:%M:%S-NY'`
CA=`date '+%Y-%m-%d-%H:%M:%S-CA'`
IL=`date '+%Y-%m-%d-%H:%M:%S-IL'`
TX=`date '+%Y-%m-%d-%H:%M:%S-TX'`
AZ=`date '+%Y-%m-%d-%H:%M:%S-AZ'`
PA=`date '+%Y-%m-%d-%H:%M:%S-PA'`
FL=`date '+%Y-%m-%d-%H:%M:%S-FL'`

#curl $NY.html https://forecast-v3.weather.gov/point/40.78,-73.97?view=plain
wget https://forecast-v3.weather.gov/point/40.78,-73.97?view=plain -O $NY.html
wget https://forecast-v3.weather.gov/point/34.02,-118.45?view=plain -O $CA.html
wget https://forecast-v3.weather.gov/point/41.78,-87.76?view=plain -O $IL.html
wget https://forecast-v3.weather.gov/point/29.64,-95.28?view=plain -O $TX.html
wget https://forecast-v3.weather.gov/point/33.69,-112.07?view=plain -O $AZ.html
wget https://forecast-v3.weather.gov/point/40.08,-75.01?view=plain -O $PA.html
wget https://forecast-v3.weather.gov/point/30.23,-81.67?view=plain -O $FL.html

java -jar tagsoup-1.2.1.jar --files $NY.html
java -jar tagsoup-1.2.1.jar --files $CA.html
java -jar tagsoup-1.2.1.jar --files $IL.html
java -jar tagsoup-1.2.1.jar --files $TX.html
java -jar tagsoup-1.2.1.jar --files $AZ.html
java -jar tagsoup-1.2.1.jar --files $PA.html
java -jar tagsoup-1.2.1.jar --files $FL.html


#Why do my for loops for my python script only work SOMETIMES and not all the time? if I'm looping
# through all the divs, h4's, and header's, it should work...Also, it only works when i dont have too many
# files. That's weird.

python3 Jonard_script.py $NY.xhtml 'NY' 'New York'
python3 Jonard_script.py $CA.xhtml 'CA' 'Los Angeles'
python3 Jonard_script.py $IL.xhtml 'IL' 'Chicago'
python3 Jonard_script.py $TX.xhtml 'TX' 'Houston'
python3 Jonard_script.py $AZ.xhtml 'AZ' 'Phoenix'
python3 Jonard_script.py $PA.xhtml 'PA' 'Philadelphia'
python3 Jonard_script.py $FL.xhtml 'FL' 'Jacksonville'








#breadth-first-search
#A* algorithm
#best-first-search
#Deptth-first-search
