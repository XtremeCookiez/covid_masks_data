from datetime import datetime
from collections import defaultdict
from statistics import mean

import argparse
import csv

def average(args):
    start_date = datetime.fromisoformat(args.start)
    cases = defaultdict(list)
    hospitalizations = defaultdict(list)
    with open(args.file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            # if datetime.strptime(row[0], '%m/%d/%Y') >= start_time:
                # print(row)
            if datetime.fromisoformat(row[0]) >= start_date:
                state = row[1].lower()
                c = int(row[23])
                cases[state].append(int(row[23]))
                hospitalizations[state].append(int(row[10]))
                # print(f'{state},{cases}')
                # data[row[1]].append(float(row[7]))
            # print(data)
        with open(args.output, 'w') as export:
            avg = {}
            for i in cases:
                avg[i] = mean(cases[i])
                export.write(f'{i},{avg[i]},{mean(hospitalizations[i])}\n')
            print(avg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Average the data into one value per location')
    parser.add_argument('start', help='Start date in format of YYYY-MM-DD')
    parser.add_argument('file', help='File to average')
    parser.add_argument('--output', help='Output file, default is "export.csv"', default='export.csv')
    parser.add_argument('--end', default=None)
    args = parser.parse_args()
    average(args)
