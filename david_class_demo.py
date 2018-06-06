class Holding(object):
    def __init__(self,name,date,share,price):
        self.name = name
        self.date = date
        self.price = price
        self.share = share

    def __repr__(self):
        return 'Holding ({!r},{!r},{!r},{!r})'.format(self.name,self.date,self.share,self.price)
    
    def cost(self):
        return self.price * self.share

    def sell(self,nshare):
        self.share-=nshare
    
AA = Holding('Mic','22-10-2018',12,20)

print(AA)

print (AA.cost())

print(getattr(AA,'date'))

#setattr(AA,'share',30)

out_name = ['name' , 'date' , 'price' , 'share']

##for obj in objects:
##    for out in out_name:
##        print('{:>10s}'.format(str(getattr(obj,out))))
