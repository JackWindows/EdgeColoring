import json
f=open('data')
data=json.load(f)
f.close()
totalCount=0
eCount={}
for key1 in data:
    for key2 in data[key1]:
        totalCount+=data[key1][key2]
        if key2 in eCount:
            eCount[key2]+=data[key1][key2]
        else:
            eCount[key2]=data[key1][key2]
avgCount=0.0
for key in sorted(eCount, key=int):
    ratio=float(eCount[key])/totalCount
    avgCount+=float(key)*ratio
    print key.ljust(4),' ratio:',(str(ratio*100)+'%').ljust(10),' Count:',eCount[key]
print avgCount
raw_input()
