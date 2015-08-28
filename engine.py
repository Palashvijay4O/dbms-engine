import sys
import re
import csv
#input
query = sys.argv[1:]

select_cases = ['Select', 'select', 'SELECT']
from_cases = ['FROM', 'From', 'from']
where_cases = ['WHERE', 'where', 'Where']
#print query

query_split = query[0].split(' ')

#print query_split


def query_case1(query_split):
  flag = 0
  target = open('metadata.txt')
  target_split = target.read().splitlines()
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


def get_column_index(column_name,query_split):

  table_name = query_split[3]
  flag = 0
  target = open('metadata.txt')
  target_split = target.read().splitlines()
  index = target_split.index(table_name)
  output = ""
  columns = []
  index = index + 1
  k = 0
  while target_split[index] != column_name:
    k = k + 1
    index = index + 1
  return k


def query_case2_max(query_split):
	a = query_split[1]
	column_name = a[a.index("(") + 1:a.rindex(")")]
	f = open(query_split[3] + ".csv", 'rt')
	reader = csv.reader(f)
	row_list = []
	for row in reader:
		row_list.append(row)
	#print row_list
	temp = get_column_index(column_name,query_split)
	i = 1
	row_list = [ map(int,x) for x in row_list ]
	maximum = row_list[0][temp]
	length = len(row_list)
	while i < length:
		if maximum < row_list[i][temp]:
			maximum = row_list[i][temp]
		i = i + 1
	print query_split[3] + "." + column_name
	print maximum


def query_case2_min(query_split):
	a = query_split[1]
	column_name = a[a.index("(") + 1:a.rindex(")")]
	f = open(query_split[3] + ".csv", 'rt')
	reader = csv.reader(f)
	row_list = []
	for row in reader:
		row_list.append(row)
	#print row_list
	temp = get_column_index(column_name,query_split)
	i = 1
	row_list = [ map(int,x) for x in row_list ]
	minimum = row_list[0][temp]
	length = len(row_list)
	while i < length:
		if minimum > row_list[i][temp]:
			minimum = row_list[i][temp]
		i = i + 1
	print query_split[3] + "." + column_name
	print minimum



def query_case2_sum(query_split):
	a = query_split[1]
	column_name = a[a.index("(") + 1:a.rindex(")")]
	f = open(query_split[3] + ".csv", 'rt')
	reader = csv.reader(f)
	row_list = []
	for row in reader:
		row_list.append(row)
	#print row_list
	temp = get_column_index(column_name,query_split)
	i = 1
	row_list = [ map(int,x) for x in row_list ]
	sum_up = 0
	length = len(row_list)
	while i < length:
		sum_up = sum_up + row_list[i][temp]
		i = i + 1
	print query_split[3] + "." + column_name
	print sum_up
	return float(sum_up/length)



def query_case2_average(query_split):
	a = query_split[1]
	column_name = a[a.index("(") + 1:a.rindex(")")]
	f = open(query_split[3] + ".csv", 'rt')
	reader = csv.reader(f)
	row_list = []
	for row in reader:
		row_list.append(row)
	#print row_list
	temp = get_column_index(column_name,query_split)
	i = 1
	row_list = [ map(int,x) for x in row_list ]
	sum_up = 0
	length = len(row_list)
	while i < length:
		sum_up = sum_up + row_list[i][temp]
		i = i + 1
	print query_split[3] + "." + column_name
	average = sum_up/float(length)
	print average


def parser(query):
    if query_split[0] not in select_cases:
        print "Wrong Query"

    else:
        if query_split[1] is '*' :
          if query_split[2] in from_cases:
            if len(query_split) == 4:
              query_case1(query_split)

        elif query_split[1].startswith("max"):
					query_case2_max(query_split)

        elif query_split[1].startswith("min"):
          query_case2_min(query_split)

        elif query_split[1].startswith("average"):
          query_case2_average(query_split)

        elif query_split[1].startswith("sum"):
          query_case2_sum(query_split)


parser(query)
