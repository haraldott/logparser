#!/usr/bin/env python
import sys
import argparse
sys.path.append('../')
from logparser import LenMa

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', default='/Users/haraldott/Development/thesis/anomaly_detection_main/data/hdfs/sosp/', type=str)
    parser.add_argument('-file', default='sorted_half.log', type=str)
    args = parser.parse_args()

    input_dir = args.dir  # The input directory of log file
    log_file = args.file  # The input log file name
    output_dir = 'Lenma_result/' # The output directory of parsing results
    log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>' # HDFS log format
    threshold  = 0.9 # TODO description (default: 0.9)
    regex      = [] # Regular expression list for optional preprocessing (default: [])

    parser = LenMa.LogParser(input_dir, output_dir, log_format, threshold=threshold, rex=regex)
    parser.parse(log_file)
