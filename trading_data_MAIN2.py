import subprocess

values=str(subprocess.getoutput('cat *csv >combined.csv'))

valueS=str(subprocess.getoutput('cat combined.csv'))
#print(valueS)
ValueS=valueS.strip().split("\n")
#print(ValueS)
string=ValueS[0]
vals=list(string.split(","))


price_chunks = [vals[x:x+24] for x in range(0, len(vals), 24)]

def pair_prices():
    global price_chunks
    return price_chunks
print(pair_prices())
