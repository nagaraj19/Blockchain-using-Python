import hashlib as hasher

class block:
    def __init__(self,index,timestamp,data,pre_hash):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.pre_hash=pre_hash
        self.hash1=self.hash_blck()

    def hash_blck(self):
        max_nounce=100000
        nounce=0
        pre_digit="0"
        while(nounce<max_nounce):
            sha=hasher.sha256()
            sha.update((str(self.index)+
                    str(self.timestamp)+
                    str(self.data)+
                    str(self.pre_hash)+
                    str(nounce)).encode())
            A=sha.hexdigest()
            if(A.startswith(pre_digit)):
                return A
            nounce=nounce+1

        print("unable to find")
            
    
import datetime as date

def C_G_B():
    return block(0,date.datetime.now(),"geneses block","0")

def next_block(last_block):
    index=last_block.index+1
    timestamp=date.datetime.now()
    data="block_num "+str(index)
    pre_hash=last_block.hash1


    return block(index,timestamp,data,pre_hash)

blocklist=[C_G_B()]
last_block=blocklist[0]
num=7
print("index {}".format(last_block.index))
print(" hash {}".format(last_block.hash1))
print("data is {}".format(last_block.data))
for i in range(0,num):
    block_add=next_block(last_block)
    blocklist.append(block_add)
    last_block=block_add

    print("index {}".format(block_add.index))
    print(" hash {}".format(block_add.hash1))
    print("data is {}".format(block_add.data))



#def SHA256(hello):
#    sha=sha256()
#    sha.update(hello).encode()
#    return sha.hexdigest()

#def SHA256(hello): #Use SHA256 encryption to find the correct hash
#  return sha256((hello).encode()).hexdigest()

"""def SHA256(hello):
        sha=hasher.sha256()
        sha.update((str(hello)).encode())
        return sha.hexdigest()
max=100000


def hash3(index,data,pre_hash,pre_zero):
    nounce=0
    prezero="a"*pre_zero
    while(nounce<max):
        h1=str(index)+str(time)+str(pre_hash)
        h2=SHA256(h1)
        if(h2.startswith(prezero)):
            return h2
        nounce=nounce+1
    print("unable to find")

a=hash3("1","00","000",1)
print(a) """

from bitcoin import *
a_valid_bitcoin_address = '329e5RtfraHHNPKGDMXNxtuS4QjZTXqBDg'
print(history(a_valid_bitcoin_address))
    
from blockchain import exchangerates



t= exchangerates.get_ticker()
for k in t:
    print(k ,t[k].last)

btc = exchangerates.to_btc('INR', 10000)
print("\n10000 INR in Bitcoin: {} " .format(btc))

from blockchain import statistics

stat=statistics.get()
print("{}".format(stat.trade_volume_btc))
print("{}".format(stat.btc_mined))
print("{}".format(stat.market_price_usd))




    



        
