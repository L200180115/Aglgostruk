##def cariLurus(wadah,target):
##    n=len(wadah)
##    for i in range(n):
##        if wadah[i]==target:
##            return True
##    return False
##class mhsTi(object):
##    def __init__(self,nama,nim,kota,us):
##        self.nama=nama
##        self.nim=nim
##        self.kotaTinggal=kota
##        self.uangsaku=us
##        
##a1=mhsTi('Taki',12,'Solo',400000)
##a2=mhsTi('ciko',10,'Sukoharjo',4500000)
##a3=mhsTi('ahmad',11,'Klaten',475000)
##a4=mhsTi('zaki',13,'Kra',450000)
##a5=mhsTi('putri',14,'Jogja',300000)
##a6=mhsTi('malu',15,'Surabaya',600000)
##a7=mhsTi('wani',16,'Bandung',1000000)
##
##Daftar=[a1,a2,a3,a4,a5,a6,a7]
##
##target='Klaten'
##for i in Daftar:
##    if i.kotaTinggal==target:
##        print(i.nama+' tinggal di '+target)
##
##def cariTerkecil(kumpulan):
##    n=len(kumpulan)
##    terkecil=kumpulan[0]
##    for i in range(1,n):
##        if kumpulan[i]<terkecil:
##            terkecil=kumpulan[0]
##    return terkecil

def binSe(kumpulan,target):
    low=0
    high=len(kumpulan)-1
    while low<=high:
        mid=(high+low)//2
        if kumpulan[mid]==target:
            return True
        elif target<kumpulan[mid]:
            high=mid-1
        else:
            low=mid+1
    return False
