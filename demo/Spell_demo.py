#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import Spell

long_file = True

if not long_file:
    input_dir  = '../logs/HDFS/'  # The input directory of log file
    log_file = 'HDFS_2k.log'  # The input log file name
else:
    input_dir  = '/Users/haraldott/Development/thesis/anomaly_detection_main/data/hdfs/sosp/'  # The input directory of log file
    log_file = 'sorted_half.log'  # The input log file name
output_dir = 'Spell_result/'  # The output directory of parsing results
log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'  # HDFS log format
tau        = 0.5  # Message type threshold (default: 0.5)
regex      = []  # Regular expression list for optional preprocessing (default: [])

parser = Spell.LogParser(indir=input_dir, outdir=output_dir, log_format=log_format, tau=tau, rex=regex)
parser.parse(log_file)