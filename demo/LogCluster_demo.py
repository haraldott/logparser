#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import LogCluster


long_file = True

if not long_file:
    input_dir  = '../logs/HDFS/'  # The input directory of log file
    log_file = 'HDFS_2k.log'  # The input log file name
else:
    input_dir  = '/Users/haraldott/Development/thesis/anomaly_detection_main/data/hdfs/sosp/'  # The input directory of log file
    log_file = 'sorted_half.log'  # The input log file name
output_dir = 'LogCluster_result/' # The output directory of parsing results
log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>' # HDFS log format
rsupport   = 10 # The minimum threshold of relative support, 10 denotes 10%
regex      = [] # Regular expression list for optional preprocessing (default: [])

parser = LogCluster.LogParser(input_dir, log_format, output_dir, rsupport=rsupport)
parser.parse(log_file)
