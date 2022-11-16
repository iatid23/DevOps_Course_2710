# import datetime
#
#
# print(datetime.datetime.now().month)
#
# import requests
#
# response = requests.get('https://google.com')
#
# if 200 <= response.status_code < 300:
#     print('The Web Is Online')
# else:
#     print('The Web Is Down')
#
# exit(30)

names = open('names.txt')
## opned the file read all lines and then stay at the end so if read more then one time it will stay there
# so you can eather open it again or
#
#print(names)
#print(names.readlines())
first_position = names.tell()
print(first_position)
for x in names:
    print(x, end='')
    ## end=''  -  will twll him to end without getting one more line again
## same :
# for x in names.readlines():
#     print(x)
print('\n\n################################################\n')
names.seek(first_position)
for x in names:
    #print(x)
    print(x, end='')
print('\n\n*************************************************\n')
names.seek(0, 0)
for x in names:
    #print(x)
    print(x, end='')