import csv
import pprint
import re

# fall2022
class_list = ['PHIL370', 'PHIL170', 'ENGL393', 'CMSC421', 'CMSC320']
class_dict = {'PHIL370': [], 'PHIL170': [], 'ENGL393': [], 'CMSC421': [],\
 'CMSC320': []}

# open TODO
with open('TODO.csv', 'r+') as f:
  csvreader = csv.reader(f)
  csvwriter = csv.writer(f)

  # extract class specific info
  lines = []
  x = 0
  curr_class = class_list[x]
  for line in csvreader:

    # non class lines
    if not line[0] in class_list and not x == 0:
      class_dict[curr_class].append(line)
    else:
      #class lines
      curr_class = line[0]

    x+=1
  pprint.pprint(class_dict)