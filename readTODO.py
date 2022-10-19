import csv
import pprint
import re
# open TODOcsv, extract and return info

# fall2022
def getclasslist():
  return ['PHIL370', 'PHIL170', 'ENGL393', 'CMSC421', 'CMSC320']

class_dict = {'PHIL370': [], 'PHIL170': [], 'ENGL393': [], 'CMSC421': [],\
 'CMSC320': []}

def readtodo():
  with open('TODO.csv', 'r+') as f:
    csvreader = csv.reader(f)
    csvwriter = csv.writer(f)

    lines = []
    x = 0
    curr_class = getclasslist()[x]
    for line in csvreader:
      if not line[0] in getclasslist() and not x == 0:
        class_dict[curr_class].append(line)
      else:
        curr_class = line[0]
      x+=1
    # omit classes with nothing todo
    for line in getclasslist():
      if class_dict[line] == []:
        class_dict.pop(line)
  return class_dict