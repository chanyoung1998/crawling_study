import json
import csv

def makejson(filename,data):
    file = open(filename, "w+")
    file.write(json.dumps(data))
    file.close()

def jsontocsv(input_file_name,output_file_name):
    with open(input_file_name, "r", encoding="utf-8", newline="") as input_file, \
            open(output_file_name, "w", encoding="utf-8", newline="") as output_file:
        data = []
        for line in input_file:
            datum = json.loads(line)
            data += datum

        csvwriter = csv.writer(output_file)
        csvwriter.writerow(data[0].keys())
        for line in data:
            csvwriter.writerow(line.values())
