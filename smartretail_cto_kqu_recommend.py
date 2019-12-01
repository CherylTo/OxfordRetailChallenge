import numpy as np
import pandas as pd
import json
import re
from apyori import apriori
import glob


all_files = pd.DataFrame()
for f in glob.glob('dailypaths/*.json'):
    tmp = pd.read_json(f)
    all_files = pd.concat([all_files, tmp], axis = 1, ignore_index=True)

#getting associations
whatever=[]
width = all_files.shape[1]
for i in range(len(all_files)): #len(all_files)
    for j in range(width):
        if str(all_files.iloc[i][j]) != 'nan':
            whatever.append(all_files.iloc[i][j][0])

path = []
for i in whatever:
    p = []
    for j in i:
        if j[1] != 'OTHER':
            p.append(j)
            for k in range(len(j)):
                if j[1] != 'OTHER':
                    pass
    path.append(p)

#Association rules
journey = []
singles=[]
for i in range(len(path)):
    p = []
    if len(path[i]) == 1:
        p.append(path[i][0][0])
    elif len(path[i]) >= 2:
        #print(path[i], len(path[i]))
        try:
            for j in range(len(path[i])):
                p.append(path[i][j][0])
        except:
            pass
    else:
        pass
    journey.append(p)

#2 or more stores visited
##for Edges
edges=[]
for i in path:
    if len(i) >=2:
        try:
            for j in range(len(i)):
                edges.append((i[j][0], i[j+1][0]))
        except:
            pass

journey2= list(filter(None, journey))

rules = apriori(journey2, min_support = 0.001, min_confidence=0.10, min_lift = 3, min_length=2)
results = list(rules)

lift = []
association = []
confidence = []

for i in range(1, len(results)):
    lift.append(results[:len(results)][i][2][0][3])
    association.append(list(results[:len(results)][i][0]))
    confidence.append(results[:len(results)][i][2][0][2])

rank = pd.DataFrame([association, lift, confidence]).T
rank.dropna(inplace=True)
rank.columns = ['Association', 'Lift', 'confidence']

values = rank.sort_values('Lift', ascending = False)
values.reset_index(drop=True, inplace=True)


# input ordered list of stores and association list

def ap_rec (path=[], *args, values):
    length = len(path)

    rec = []

    if length == 0:
        print ("Can't recommend with nothing...")
        return None

    elif length == 1:
        rec = get_one(path=path, values=values)
        return list(set(trim(rec, path)))

    elif length == 2:
        rec = get_two(path=path, values=values)
        return list(set(trim(rec, path)))

    elif length > 2:
        rec = get_two(path=path[-2:], values=values)
        return list(set(trim(rec, path)))

    else:
        return None

def trim(rec, path):
    newrec = []
    print (path)
    for r in rec:
        for p in path:
            if r not in path:
                newrec.append(r)
    return newrec

def get_one(path=[], *args, values):
    rec = []
    for i in range(len(values)):
        if values.iloc[i]['Association'][0] == path[-1]:
            #print(values.iloc[i]['Association'])
            try:
                rec.append(values.iloc[i]['Association'][1])
            except:
                pass
    return rec

def get_two(path=[], *args, values):
    rec = []
    for i in range(len(values)):
        if (values.iloc[i]['Association'][0] == path[0]) and (values.iloc[i]['Association'][1] == path[1]):
            #print(values.iloc[i]['Association'])
            try:
                rec.append(values.iloc[i]['Association'][2])
            except:
                pass
    if len(rec) == 0:
        rec = get_one(path=path, values=values)
    return rec

path = [s.strip() for s in input().split(',')]

ap_rec(path,values=values)
