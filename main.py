import csv
import json
import pickle

pancake_in = open("./cakepairs.csv", mode='rb')
other_in = open("./pairs2.csv", mode='r')

result = open('./result.txt', mode='w')

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


for row in other_pairs:
    key1 = row[-2]
    key2 = row[-1]
    for pancake_row in  pancake_pairs:
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
            result.write(str(pairs))
            result.write('\n')

print(available_pair)
result.close()