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


# a02 = pd.read_json('dailypaths/11-02.json')
# a03 = pd.read_json('dailypaths/11-03.json')
# a04 = pd.read_json('dailypaths/11-04.json')
# a05 = pd.read_json('dailypaths/11-05.json')
# a06 = pd.read_json('dailypaths/11-06.json')
# a07 = pd.read_json('dailypaths/11-07.json')
# a08 = pd.read_json('dailypaths/11-08.json')
# a09 = pd.read_json('dailypaths/11-09.json')
# a10 = pd.read_json('dailypaths/11-10.json')
# a11 = pd.read_json('dailypaths/11-11.json')
# a12 = pd.read_json('dailypaths/11-12.json')
# a13 = pd.read_json('dailypaths/11-13.json')
# a14 = pd.read_json('dailypaths/11-14.json')
# a15 = pd.read_json('dailypaths/11-15.json')
# a16 = pd.read_json('dailypaths/11-16.json')
# a17 = pd.read_json('dailypaths/11-17.json')
# a18 = pd.read_json('dailypaths/11-18.json')
# a19 = pd.read_json('dailypaths/11-19.json')
# a20 = pd.read_json('dailypaths/11-20.json')
# a21 = pd.read_json('dailypaths/11-21.json')
# a22 = pd.read_json('dailypaths/11-22.json')
# a23 = pd.read_json('dailypaths/11-23.json')
# a24 = pd.read_json('dailypaths/11-24.json')
# a25 = pd.read_json('dailypaths/11-25.json')
# a26 = pd.read_json('dailypaths/11-26.json')
# a27 = pd.read_json('dailypaths/11-27.json')
# a28 = pd.read_json('dailypaths/11-28.json')
# a29 = pd.read_json('dailypaths/11-29.json')
# a30 = pd.read_json('dailypaths/11-30.json')
# a31 = pd.read_json('dailypaths/12-01.json')
# a32 = pd.read_json('dailypaths/12-02.json')
# a33 = pd.read_json('dailypaths/12-03.json')
# a34 = pd.read_json('dailypaths/12-04.json')
# a35 = pd.read_json('dailypaths/12-05.json')
# a36 = pd.read_json('dailypaths/12-06.json')
# a37 = pd.read_json('dailypaths/12-07.json')
# a38 = pd.read_json('dailypaths/12-08.json')
# a39 = pd.read_json('dailypaths/12-09.json')
# a40 = pd.read_json('dailypaths/12-10.json')
# a41 = pd.read_json('dailypaths/12-11.json')
# a42 = pd.read_json('dailypaths/12-12.json')
# a43 = pd.read_json('dailypaths/12-13.json')
# a44 = pd.read_json('dailypaths/12-14.json')
# a45 = pd.read_json('dailypaths/12-15.json')
# a46 = pd.read_json('dailypaths/12-16.json')
# a47 = pd.read_json('dailypaths/12-17.json')
# a48 = pd.read_json('dailypaths/12-18.json')
# a49 = pd.read_json('dailypaths/12-19.json')
# a50 = pd.read_json('dailypaths/12-20.json')
# a51 = pd.read_json('dailypaths/12-21.json')
# a52 = pd.read_json('dailypaths/12-22.json')
# a53 = pd.read_json('dailypaths/12-23.json')
# a54 = pd.read_json('dailypaths/12-24.json')
# a55 = pd.read_json('dailypaths/12-25.json')
# a56 = pd.read_json('dailypaths/12-26.json')
# a57 = pd.read_json('dailypaths/12-27.json')
# a58 = pd.read_json('dailypaths/12-28.json')
# a59 = pd.read_json('dailypaths/12-29.json')
# a60 = pd.read_json('dailypaths/12-30.json')
# a61 = pd.read_json('dailypaths/12-31.json')

# all_files = pd.concat([a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,
#                        a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,
#                        a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,
#                        a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,
#                        a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,
#                        a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,
#                        a61], axis = 1, ignore_index=True)

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