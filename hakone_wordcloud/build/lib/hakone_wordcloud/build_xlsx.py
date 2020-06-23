import glob
import re
import sys
import pandas as pd

# `$1/topic#_#_freq.txt` を集めて data/topics.xlsx にまとめる

def main():
    if len(sys.argv) <= 1:
        print(f'Usage: {sys.argv[0]} [datadir]')
        sys.exit(1)
    datadir = sys.argv[1]

    sheets = {}
    re_fname = re.compile(datadir + r'/topic(\d+)_(\d+)_freq.txt')
    for fname in glob.glob(datadir + '/*.txt'):
        m = re_fname.match(fname)
        if m:
            sheet_name = f'{int(m[1]):02}-{int(m[2]):02}'
            sheets[sheet_name] = pd.read_csv(fname, sep='\t', header=None, names=['term', 'value'])

    writer = pd.ExcelWriter('topics.xlsx', engine='xlsxwriter')
    for sheet_name in sorted(sheets.keys()):
        sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
    writer.save()

if __name__ == '__main__':
    main()
