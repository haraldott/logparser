#!/usr/bin/env python

import sys
sys.path.append('../')
from logparser import SLCT

long_file = True

if not long_file:
    input_dir  = '../logs/HDFS/'  # The input directory of log file
    log_file = 'HDFS_2k.log'  # The input log file name
else:
    input_dir  = '/Users/haraldott/Development/thesis/anomaly_detection_main/data/hdfs/sosp/'  # The input directory of log file
    log_file = 'sorted_half.log'  # The input log file name
output_dir = 'SLCT_result/'  # The output directory of parsing results
log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'  # HDFS log format
support    = 10  # The minimum support threshold
regex      = []  # Regular expression list for optional preprocessing (default: [])

parser = SLCT.LogParser(log_format=log_format, indir=input_dir, outdir=output_dir, 
                        support=support, rex=regex)
parser.parse(log_file)
