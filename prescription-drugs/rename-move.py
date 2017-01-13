import glob
import os

old_len = len(glob.glob("oldData/file-*.txt"))
new_len = len(glob.glob("file-*.txt"))

new_index = old_len
old_index = 0

for n in range(new_len):
    old_name = "file-" + str(old_index) + ".txt"
    new_name = "oldData/file-" + str(new_index) + ".txt"
    os.rename(old_name, new_name)
    new_index += 1
    old_index += 1
