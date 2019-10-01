#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import LogMine

long_file = True

if not long_file:
    input_dir  = '../logs/HDFS/'  # The input directory of log file
    log_file = 'HDFS_2k.log'  # The input log file name
else:
    input_dir  = '/Users/haraldott/Development/thesis/anomaly_detection_main/data/hdfs/sosp/'  # The input directory of log file
    log_file = 'sorted_half.log'  # The input log file name
output_dir = 'LogMine_result/' # The output directory of parsing results
log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>' # HDFS log format
levels     = 2 # The levels of hierarchy of patterns
max_dist   = 0.001 # The maximum distance between any log message in a cluster and the cluster representative
k          = 1 # The message distance weight (default: 1)
regex      = []  # Regular expression list for optional preprocessing (default: [])

parser = LogMine.LogParser(input_dir, output_dir, log_format, rex=regex, levels=levels, max_dist=max_dist, k=k)
parser.parse(log_file)
