import os
import csv
class Output:
    
    def get_equal_output(file_1, file_2, path):
        with open('./output/equal.csv','r+') as file:
            n = file.read()
            writer = csv.writer(file)
            writer.writerow([path + file_1,path + file_2])

    def get_inequal_output(file_1, file_2, path):
        with open('./output/inequal.csv','r+') as file:
            n = file.read()
            writer = csv.writer(file)
            writer.writerow([path + file_1,path + file_2])

    def init_output():
        #s.mkdir(r'output')
        with open('./output/equal.csv','w') as file:
            writer = csv.writer(file)
            writer.writerow(["file1","file2"])
        with open('./output/inequal.csv','w') as file:
            writer = csv.writer(file)
            writer.writerow(["file1","file2"])