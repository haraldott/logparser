#!/usr/bin/env python

import sys
sys.path.append('../')
from logparser import LogSig

long_file = True

if not long_file:
    input_dir  = '../logs/HDFS/'  # The input directory of log file
    log_file = 'HDFS_2k.log'  # The input log file name
else:
    input_dir  = '/Users/haraldott/Development/thesis/anomaly_detection_main/data/hdfs/sosp/'  # The input directory of log file
    log_file = 'sorted_half.log'  # The input log file name
output_dir   = 'LogSig_result/' # The output directory of parsing results
log_format   = '<Date> <Time> <Pid> <Level> <Component>: <Content>' # HDFS log format
regex        = []  # Regular expression list for optional preprocessing (default: [])
group_number = 14 # The number of message groups to partition

parser = LogSig.LogParser(input_dir, output_dir, group_number, log_format, rex=regex)
parser.parse(log_file)
