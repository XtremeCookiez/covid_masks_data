from datetime import datetime
from collections import defaultdict
from statistics import mean

import argparse
import csv

def average(args):
    start_date = datetime.fromisoformat(args.start)
    data = defaultdict(list)
    with open(args.file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            if datetime.fromisoformat(row[3]) >= start_date:
                data[row[1]].append(float(row[7]))

        with open(args.output, 'w') as export:
            avg = {}
            for i in data:
                avg[i] = mean(data[i])
                export.write(f'{i},{avg[i]}\n')
            print(avg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Average the data into one value per location')
    parser.add_argument('start', help='Start date in format of YYYY-MM-DD')
    parser.add_argument('file', help='File to average')
    parser.add_argument('--output', help='Output file, default is "export.csv"', default='export.csv')
    parser.add_argument('--end', default=None)
    args = parser.parse_args()
    average(args)
