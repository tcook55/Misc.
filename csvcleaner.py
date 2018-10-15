#Used in conjunction with user_ID_limiter.py. Removes duplicate points.

import csv

class Point:
    def __init__(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
user_dict = {}
old_ctr = 0
new_ctr = 0
seen = set()
with open('location of file to be cleaned', mode='r') as unclean_f:
    parser = csv.reader(unclean_f, delimiter = ',')
    with open('cleaned file output location', mode='w', newline = '') as clean_f:
        writeCSV = csv.writer(clean_f, delimiter = ',')
        for row in parser:
            old_ctr += 1
            point_check = Point(row[3], row[2])
            if (point_check.x, point_check.y) not in seen:
                seen.add((point_check.x, point_check.y))
                writeCSV.writerow([row[0], row[1], row[2], row[3]])
                if row[0] in user_dict:
                    user_dict[row[0]] += 1
                else:
                    user_dict[row[0]] = 1
                new_ctr += 1


print('Old number of data points: ' + str(old_ctr))
print('New number of data points: ' + str(new_ctr))
print('================================')
for key in user_dict:
    print("{}: {}".format(key, user_dict[key]))
