import random
import time
import csv

# initialise initial data of x_value, y1 and y2
x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ['x_value', 'total_1', 'total_2']
file_path = r'C:\Users\santo\Scientific_Python\Data Analysis with Python\random.csv'

with open(file_path, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


while True: 

    with open(file_path, 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        info = {
            'x_value': x_value,
            'total_1': total_1,
            'total_2': total_2
        }
        
        csv_writer.writerow(info)

        # print the new set of values
        print(f"{info['x_value']}, {info['total_1']}, {info['total_2']}")
        
        # update the values
        x_value += 1
        total_1 += random.randint(-2, 5)
        total_2 += random.randint(-3, 7)
    
    # delay a sec 
    time.sleep(1)
