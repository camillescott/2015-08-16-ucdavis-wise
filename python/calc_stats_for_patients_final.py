import numpy
import glob
import sys

def main(file_list, action):
    for f in file_list:
        data = numpy.loadtxt(fname = f, delimiter = ',')
        if action == 'min':
            values = data.min(axis = 1)
        elif action == 'max':
            values = data.max(axis = 1)
        elif action == 'mean':
            values = data.mean(axis = 1)
        for m in values:
            print m

if __name__ == "__main__":
    script_name = sys.argv[0]
    action = sys.argv[1]
    file_list = sys.argv[2:]
    main(file_list, action)
