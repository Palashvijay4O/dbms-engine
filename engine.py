import sys

#input
query = sys.argv[1:]

select_cases = ['Select', 'select', 'SELECT']
from_cases = ['FROM', 'From', 'from']

#print query

query_split = query[0].split(' ')

#print query_split


def query_case1(query_split):
  flag = 0
  target = open('metadata.txt')
  target_split = target.read().splitlines()
#  print target_split
  index = target_split.index(query_split[3])
  output = ""
  columns = []
  index = index + 1
  while target_split[index] != '<end_table>':
    if target_split[index+1] == '<end_table>':
      output += query_split[3] + "." +target_split[index]
    else:
      output += query_split[3] + "." +target_split[index] + ","
    columns.append(target_split[index])
    index = index + 1
  print output
#  print columns
  filename = query_split[3] + ".csv"
  fileopend = open(filename)
  print fileopend.read()



def parser(query):
    if query_split[0] not in select_cases:
        print "Wrong Query"

    else:
        if query_split[1] is '*' :
          if query_split[2] in from_cases:
            if len(query_split) == 4:
              query_case1(query_split)



parser(query)
