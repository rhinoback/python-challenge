votecount=0
kcount=0
corcount=0
licount=0
ocount=0

khanpt:int
correypt:int
lipt:int
otooleypt:int

filePath=os.path.join('election_data.csv')
with open(filePath, 'r') as file:
    csvReader=csv.reader(file, delimiter=',')
    next(csvReader)
    #csvReader is storing the object created by csv.reader
    #you will want to loop through the object to get your data.
    #Notice that row is a list!
    
    for row in csvReader:
        votecount=votecount+1       

        if row[2]==("Khan"):
            kcount=kcount+1
        if row[2]==("Correy"):
            corcount=corcount+1
        if row[2]==("Li"):
            licount=licount+1
        if row[2]==("O'Tooley"):
            ocount=ocount+1
            
(kcount/votecount),
(corcount/votecount),
(licount/votecount),
(ocount/votecount)


a_float = (.6300001050837531)
KhanPct = "{:.2f}".format(a_float)

a_float = (.19999994319797126)
CorPct = "{:.2f}".format(a_float)

a_float = (.13999996023857988)
LiPct = "{:.2f}".format(a_float)

a_float = (.02999999147969569)
OtoolPct = "{:.2f}".format(a_float)



a_number = .63
k = "{:.0%}".format(a_number)
a_number = .19999994319797126
c = "{:.0%}".format(a_number)
a_number = .13999996023857988
l = "{:.0%}".format(a_number)
a_number = .02999999147969569
o = "{:.0%}".format(a_number)
KhanPct
CorPct,
LiPct,
OtoolPct
#print(k)63%
#print(c)20%
#print(l)14%
#print(o)3%


print("Election Results")
print("------------------------")
print("Total Vote Count:",  (votecount))
print("------------------------")
print("Khan:",k,   (kcount))
print("Correy:",c,   (corcount))
print("Li:",l,   (licount))
print("O'Tooley:",o,   (ocount))
print("------------------------")
print("Winner:Khan")
print('-------------------------')



