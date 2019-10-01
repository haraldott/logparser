#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import SHISO
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', default='/Users/haraldott/Development/thesis/anomaly_detection_main/data/hdfs/sosp/', type=str)
    parser.add_argument('-file', default='sorted_half.log', type=str)
    args = parser.parse_args()

    input_dir = args.dir  # The input directory of log file
    log_file = args.file  # The input log file name
    output_dir  = 'SHISO_result/' # The output directory of parsing results
    log_format  = '<Date> <Time> <Pid> <Level> <Component>: <Content>' # HDFS log format
    regex       = [r'blk_-?\d+', r'(\d+\.){3}\d+(:\d+)?'] # Regular expression list for optional preprocessing (default: [])
    maxChildNum = 4 # The maximum number of children for each internal node
    mergeThreshold = 0.1 # Threshold for searching the most similar template in the children
    formatLookupThreshold = 0.3 # Lowerbound to find the most similar node to adjust
    superFormatThreshold  = 0.85 # Threshold of average LCS length, determing whether or not to create a super format

    parser = SHISO.LogParser(log_format,indir=input_dir,outdir=output_dir, rex=regex, maxChildNum=maxChildNum,
                             mergeThreshold=mergeThreshold, formatLookupThreshold=formatLookupThreshold,
                             superFormatThreshold=superFormatThreshold)
    parser.parse(log_file)
