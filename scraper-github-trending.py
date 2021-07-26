import requests
from bs4 import BeautifulSoup
# Collect the github page
page = requests.get('https://github.com/trending')
#print(page)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)

# get the box list
box = soup.find(class_='')
# print (box)

# find all instances of that class 
box_row = box.find_all(class_="Box-row")
print(len(box_row))

import csv
# Open writer with name
file_name = "github_trending_today.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))
# write a new row as a header
f.writerow(['Developer', 'Box Name', 'Number of Stars'])

for box in box_row:
    # find the first <a> tag and get the text. Split the text using '/' to get an array with developer name and box name
    full_box_name = box.find('h1').text.split('/')
    
    # extract the developer name at index 0
    developer = full_box_name[0].strip()

    # extract the box name at index 1
    box_name = full_box_name[1].strip()

    # find the first occurance of class octicon octicon-star and get the text from the parent (which is the number of stars)
    stars = box.find(class_='octicon octicon-star').parent.text.strip()
    # strip() all to remove leading and traling white spaces
    print('developer', developer)
    print('name', box_name)
    print('stars', stars)
    # add the information as a row into the csv table
    f.writerow([developer, box_name, stars])
