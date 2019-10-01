#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import Spell
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', default='/Users/haraldott/Development/thesis/anomaly_detection_main/data/hdfs/sosp/', type=str)
    parser.add_argument('-file', default='sorted_half.log', type=str)
    args = parser.parse_args()

    input_dir = args.dir  # The input directory of log file
    log_file = args.file  # The input log file name
    output_dir = 'Spell_result/'  # The output directory of parsing results
    log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'  # HDFS log format
    tau        = 0.5  # Message type threshold (default: 0.5)
    regex      = []  # Regular expression list for optional preprocessing (default: [])

    parser = Spell.LogParser(indir=input_dir, outdir=output_dir, log_format=log_format, tau=tau, rex=regex)
    parser.parse(log_file)