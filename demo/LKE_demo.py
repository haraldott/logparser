#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import LKE

long_file = True

if not long_file:
    input_dir  = '../logs/HDFS/'  # The input directory of log file
    log_file = 'HDFS_2k.log'  # The input log file name
else:
    input_dir  = '/Users/haraldott/Development/thesis/anomaly_detection_main/data/hdfs/sosp/'  # The input directory of log file
    log_file = 'sorted_half.log'  # The input log file name
output_dir      = 'LKE_result/' # The output directory of parsing results
log_format      = '<Date> <Time> <Pid> <Level> <Component>: <Content>' # HDFS log format
regex           = [r'blk_-?\d+', r'(\d+\.){3}\d+(:\d+)?'] # Regular expression list for optional preprocessing (default: [])
split_threshold = 3 # The threshold used to determine group splitting (default: 4)

parser = LKE.LogParser(log_format=log_format, indir=input_dir, outdir=output_dir,
                       rex=regex, split_threshold=split_threshold)        
parser.parse(log_file)

