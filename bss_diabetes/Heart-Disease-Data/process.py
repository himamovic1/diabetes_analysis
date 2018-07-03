import glob
import os


class Entry:
    def __init__(self, row):
        self.data = [row[2], row[3], row[9], row[12], row[13], row[14], row[15], row[16], row[57]]


# Get file names ending with .data in cwd
saved_dir = os.getcwd()
os.chdir('./Heart-Disease-Data/')
files = glob.glob('*.data')

for file in files:
    with open(file, 'r') as f:
        rows = f.read().replace('\n', ' ').replace('-9', 'None').split('name')

    data_set = [r.lstrip().rstrip().strip('\n').split(' ') for r in rows[:-1]]
    processed = [Entry(r).data for r in data_set]

    with open('./processed2/processed-' + file, 'w', encoding='utf-8') as phd:
        for r in processed:
            phd.write(','.join(r) + '\n')
