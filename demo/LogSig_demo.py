#!/usr/bin/env python

import sys
sys.path.append('../')
from logparser import LogSig
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', default='/Users/haraldott/Development/thesis/anomaly_detection_main/data/hdfs/sosp/', type=str)
    parser.add_argument('-file', default='sorted_half.log', type=str)
    args = parser.parse_args()

    input_dir = args.dir  # The input directory of log file
    log_file = args.file  # The input log file name
    output_dir   = 'LogSig_result/' # The output directory of parsing results
    log_format   = '<Date> <Time> <Pid> <Level> <Component>: <Content>' # HDFS log format
    regex        = []  # Regular expression list for optional preprocessing (default: [])
    group_number = 14 # The number of message groups to partition

    parser = LogSig.LogParser(input_dir, output_dir, group_number, log_format, rex=regex)
    parser.parse(log_file)
