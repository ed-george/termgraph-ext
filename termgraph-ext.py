#!/usr/bin/env python
# coding=utf-8

# termgraph.py - draw basic graphs on terminal
# https://github.com/mkaz/termgraph

# Marcus Kazmierczak
# http://mkaz.com/

from __future__ import print_function

import argparse
import sys
import termcolor
from datetime import datetime

#TODO: change tick character
tick = '▇'
sm_tick = '|'
index = 0
labels =[]
data = []
# sample bar chart data
#labels = ['2007', '2008', '2009', '2010', '2011']
#data = [183.32, 231.23, 16.43, 50.21, 508.97]

try:
    range = xrange
except NameError:
    pass

def main():

    global index
    global labels
    global data

    # determine type of graph
    
    # read data
    if (args['filename']):
        labels, data = read_data(args['filename'])
    else:
        # shouldn't happen since argparse covers empty case
        print(">> Error: No data file specified")
        sys.exit(1)

    # verify data
    m = len(labels)
    if m != len(data):
        print(">> Error: Label and data array sizes don't match")
        sys.exit(1)

    # massage data
    ## normalize for graph
    max = 0
    for i in range(m):
        if data[i] > max:
            max = data[i]
            index = i

    step = max / args['width']
    # display graph
    for i in range(m):
        isMax = data[i] == data[index]
        print_blocks(i, labels[i], data[i], step, isMax)

    print()


def print_blocks(index, label, count, step, isMax):
    #TODO: add flag to hide data labels
    blocks = int(count / step)
    print("{}: ".format(label), end="")
    if count < step:
        sys.stdout.write(sm_tick)
    else:
        bar = ""
        for i in range(blocks):
                bar += tick

        if args['color']:
            if isMax:
                termcolor.cprint(bar, "green", end="")
            else:
                termcolor.cprint(bar, "cyan", end="")
        else:
            sys.stdout.write(bar)

    print("{:>7.2f}".format(count), end="")

    if args['diff'] and index != 0:
        formatDifference(count, data[index - 1])

    if args['parse']:
        parseDate(index)
    
    print()    

def parseDate(i):
    if i > 0:
        try:
            curr = datetime.strptime(labels[i], args['format'])
            prev = datetime.strptime(labels[i - 1], args['format'])
        except Exception, e:
            print(" **Error parsing date**", end="")
            return

        duration = curr - prev
        days, seconds = duration.days, duration.seconds
        hours = days * 24 + seconds // 3600

        print(" " + str(hours) + "hrs", end="")
       
        avg = float((data[i] - data[i-1]) / hours)

        if args['color']:
            termcolor.cprint(" (Avg: %.2f p/hr)" % avg, "yellow", end="")
        else:
            print(" (Avg: %.2f p/hr)" % avg, end="")

        if(i == (len(data) - 1)):
            first = datetime.strptime(labels[0], args['format'])
            f_duration = curr - first
            f_days, f_seconds = f_duration.days, f_duration.seconds
            f_hours = f_days * 24 + f_seconds // 3600
            f_avg = float((data[i] - data[0]) / f_hours)
            if args['color']:
                termcolor.cprint("\n\nOverall average of %.4f p/hr over %d hours" % (f_avg, f_hours), "yellow", end="")
            else:
                print("\n\nOverall average of %.4f p/hr over %d hours" % (f_avg, f_hours), end="")

    else:
        return


def formatDifference(current, prev):

    formatted = current - prev
    pos = formatted >= 0
    symbol = "+" if pos else ""

    if args['color']:
        termcolor.cprint(" (" + symbol + str(formatted) + ")", "green" if pos else "red", end="")
    else:
        print (" (" + symbol + str(formatted) + ")", end="")

    return

def init():
    parser = argparse.ArgumentParser(description='draw basic graphs on terminal')
    parser.add_argument('filename', nargs=1, help='data file name (comma or space separated)')
    parser.add_argument('-c', '--color', action='store_true',  help='print graph using ANSI color')
    parser.add_argument('-d', '--diff', action='store_true', help='show numerical difference between adjacent plots')
    parser.add_argument('-f', '--format', type=str,default="%d/%m/%Y-%H:%M", help='specify date format used in data labels')
    parser.add_argument('-p', '--parse', action='store_true', help='parse date format used in data labels')
    parser.add_argument('-w', '--width', type=int, default=50, help='width of graph in characters default:50')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = vars(parser.parse_args())
    args['filename'] = args['filename'][0]  # returns as list, we dont want that
    return args


def read_data(filename):
    print("------------------------------------")
    print("Reading data from", filename)
    print("------------------------------------\n")

    labels = []
    data = []

    f = open(filename, "r")

    verbose = args['verbose']
    lines = 0
    for line in f:
        line = line.strip()
        lines += 1
        if verbose:
            print("R: " + line)
        if line:
            if not line.startswith('#'):
                if line.find(",") > 0:
                    cols = line.split(',')
                else:
                    cols = line.split()
                labels.append(cols[0].strip())
                data_point = cols[1].strip()
                data.append(float(data_point))

    f.close()

    if verbose:
        print("------------------------------------")
        print ("Closed file - read %d lines" % lines)
        print("------------------------------------\n")

    return labels, data


if __name__ == "__main__":
    args = init()
    main()


