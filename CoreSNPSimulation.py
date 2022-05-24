#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-
# @author lvmin
# @time 2021/8/26 14:49
import re, glob, sys, random, linecache
try:
    file_marker = sys.argv[1]  #the candidate marker information in geno file format
    cau_list = sys.argv[2]  # the core sample list for testing
    marker_num = int(sys.argv[3])  #the number of core SNPs
    times = int(sys.argv[4]) # the simulation times
    # fot_file = sys.argv[5]
except IndexError:
    print("random select 20 marker to ditingush 820 cauliflower. \n"
          "python3 /home/lmj/tmp/pycharm_project_503/random_test_markers.py filein \n")

def ranks(sample):
    """
    Return the ranks of each element in an integer sample.
    """
    indices = sorted(range(len(sample)), key=lambda i: sample[i])
    return sorted(indices, key=lambda i: indices[i])

def sample_with_minimum_distance(total, select, distance):
    """
    Sample of k elements from range(n), with a minimum distance d.
    """
    sample = random.sample(range(total-(select-1)*(distance-1)), select)
    return [s + (distance-1)*r + 1 for s, r in zip(sample, ranks(sample))]

fot_file = "random_"+str(marker_num)+"_"+str(times)+"_core.xls"

fot = open(fot_file, 'w')
fot.write("Random_id\tNumber_types\tMarker_list\n")

core_list = []
core_file = "/aglab200T/aglab/lmj/2_projects/project_01/5_DNA_fingerprint/Sample_list_Core_153"
core_fin = open(core_file, 'r')
for line in core_fin:
    core = line.strip("\n")
    core_list.append(core)

fin_cau_list = open(cau_list, 'r')
index_num = {}
num = 0
for line in fin_cau_list:
    # if re.match(r'C0_|PN|YC|SB|SN|SC.+', line):
    if line.strip("\n") in core_list:
        index_num[num] = 1
    num += 1

tag = 0
while tag < times:
    # print(len(index_num.keys()))

    fin_marker = open(file_marker, 'r')
    line_num = 0
    for line in fin_marker:
        line_num += 1

    fin_marker.seek(0,0)
    rdms = sample_with_minimum_distance(line_num, int(marker_num), int(line_num/int(marker_num)*0.6))
    # print(rdms)
    rdms.sort()
    dic = {}
    marker_list = []
    for i in rdms:
        line = linecache.getline(file_marker, i)
        line = line.strip("\n")
        _line = line.split("\t")
        try:
            id = _line[0]+"_"+_line[1]
        except IndexError:
            print(i)
        marker_list.append(id)
        try:
            nts = _line[3].split(" ")
        except IndexError:
            print(line)
        nts_825 = []
        # print(len(nts))
        num = 0
        for nt in nts:
            if num in index_num.keys():
                # print(nts.index(nt))
                # print(index_num)
                nts_825.append(nt)
            num += 1
        dic[id] = nts_825
        # print(len(nts_825))

    dic1 = {}
    for id in dic:
        for sample in range(len(dic[id])):
            if sample not in dic1:
                dic1[sample] = [dic[id][sample]]
            else:
                dic1[sample].append(dic[id][sample])

    codes = []
    type = 0
    for sample in dic1:
        string = "".join(dic1[sample])
        if string not in codes:
            codes.append(string)
            type += 1
    fot.write(str(tag)+"\t"+str(type)+"\t"+";".join(marker_list)+"\n")
    tag += 1
fot.close()

