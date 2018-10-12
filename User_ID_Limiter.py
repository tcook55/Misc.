import csv
import os
from fnmatch import fnmatch
import ntpath
import time
from datetime import datetime

#Puts all csv file names in a list
data = []
pattern = "*.csv"
for path, subdirs, files in os.walk('data_directory_path'):
    for name in files:
        if fnmatch(name, pattern):
            data.append(os.path.join(path, name))

print (data)
users = []
user_dict = {}
other_users = 0
iteration = 1

#enumerate through file names in the list for multiple csv looping
with open('new_csv_path', mode='w', newline = '') as test_file:
    test_writer = csv.writer(test_file, delimiter = ',')
    for idx, file in enumerate(data):
        print ("Iteration Number " + str(iteration))
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter='|')
            #print current number of data points found for users
            for key in user_dict:
                print("{}: {}".format(key, user_dict[key]))
            #Check if user id is new or already in user list
            #length of users says how many user ids you want to collect data points for
            #Convert epoch to datetime
            for row in readCSV:
                if row[0] not in users and len(users) < 50:
                    x = int(row[1])
                    x /= 1000
                    dt = datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S')
                    users.append(row[0])
                    user_dict[row[0]] = 1
                    test_writer.writerow([row[0], dt, row[2], row[3]])
                elif row[0] in users:
                    x = int(row[1])
                    x /= 1000
                    dt = datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S')
                    test_writer.writerow([row[0], dt, row[2], row[3]])
                    user_dict[row[0]] += 1
                elif row[0] not in users:
                    other_users += 1
            iteration += 1
 
#Print shows number of data points ignored by the script because they didn't have a matching user id
print ('Number of data points not collected: ' + str(other_users))
for key in user_dict:
    print("{}: {}".format(key, user_dict[key]))


