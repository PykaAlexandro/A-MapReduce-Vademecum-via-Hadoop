import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print("{0}\t{1}".format(store, cost))
#defining a mapper to output store name and transaction value with a little defensive coding for incorrect inputs
            
def reducer():
    salesTotal = 0
    oldKey = None
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        thisKey, thisSale = data
        if oldKey and oldKey != thisKey:
            print("{0}\t{1}".format(oldKey, salesTotal))
            salesTotal = 0
        oldKey = thisKey
        salesTotal += float(thisSale)
    if oldKey != None:
        print("{0}\t{1}".format(oldKey, salesTotal))
#defining a reducer that returns store names and the total transactions' amout per store
        
