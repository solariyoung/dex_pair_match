import csv
import json
import pickle

pancake_in = open("./cakepairs.csv", mode='rb')
other_in = open("./pairs2.csv", mode='r')

result = open('./result.txt', mode='w')
cakeSingle = open('./cakesingle.txt',mode= 'w')

other_pairs = []
pancake_pairs = []
guitar_pairs = []
bsw_pairs = []
bakery_pairs = []
ape_pairs = []
mdex_pairs = []

available_pair = []

with open('./cakepairs.csv', encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        pancake_pairs.append(row)

with open('./pairs2.csv', encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        other_pairs.append(row)
        if row[0] == "Guitar-LP":
            guitar_pairs.append(row)
        if row[0] == "BSW-LP":
            bsw_pairs.append(row)
        if row[0] == "BLP":
            bakery_pairs.append(row)
        if row[0] == "MDEX LP":
            mdex_pairs.append(row)
        if row[0] == "APE-LP":
            ape_pairs.append(row)


# print(guitar_pairs)
cake_list = []
baseToken =['BUSD', 'USDT', 'USDC', 'TUSD', 'MIM']

for p in pancake_pairs:
    if p[1] in baseToken:
        if p[2] not in baseToken:
            cake_list.append(p)
    else:
        if p[2] in baseToken:
            cake_list.append(p)

# print(cake_list)

for c in cake_list:
    if c[1] in baseToken:
        for c2 in cake_list:
            if (c[4] in c2) and (c[1] not in c2):
                if c2[1] in baseToken:
                    pair1 = [
                        c[2],
                        c[4]
                    ]
                    pair = [
                        c[1],
                        c[2],
                        c2[1],

                    ]
                    cakeSingle.write(str(pair1))
                    cakeSingle.write('\n')
                    cakeSingle.write(str(pair))
                    cakeSingle.write('\n')



for row in other_pairs:
    key1 = row[-2]
    key2 = row[-1]
    for pancake_row in pancake_pairs:
        if pancake_row.count(key1) and pancake_row.count(key2):
            pairs = [
                    pancake_row[0],
                    row[0],
                    pancake_row[1],
                    pancake_row[2],
                    pancake_row[3],
                    pancake_row[4]
                ]
            available_pair.append(pairs)
            # result.write(str(pairs))
            # result.write('\n')

# print(available_pair)
result.close()
cakeSingle.close()
