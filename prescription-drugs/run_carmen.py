import json
import carmen

file_number = 0
file_name = "file-" + str(file_number) + ".txt"
file_count = len(glob.glob("file-*.txt"))

for n in range(file_count):
    row_number = 1
    with open(file_name) as data_file:
        for line in data_file:
            data = json.loads(line)
            resolver = carmen.get_resolver()
            resolver.load_locations
            location = resolver.resolve_tweet(tweet)

            f = open('carmenized','a')
            f.write(location + '\n')
            f.close()

            f = open('row_number','w')
            f.write(str(row_number))
            f.close()
            row_number += 1

        f = open('file_number','w')
        f.write(str(file_number))
        f.close()
        file_number += 1
        file_name = 'file' + str(file_number) + '.txt'
