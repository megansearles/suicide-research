import glob
import os

file_number = 0
file_name = "file-" + str(file_number) + ".txt"
carmen_name = 'carmen-' + str(file_number) + '.txt'
file_count = len(glob.glob("file-*.txt"))

for n in range(file_count):
    os.system('python -m carmen.cli ' + file_name + ' ' + carmen_name)
    f = open('file_number','w')
    f.write(str(file_number))
    f.close()
    file_number += 1
    file_name = 'file-' + str(file_number) + '.txt'
    carmen_name = 'carmen-' + str(file_number) + '.txt'
