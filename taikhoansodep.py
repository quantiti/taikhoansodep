import sys
import inspect

def ThapQuy(format="AAAAAAAAAA"): #complete
#So tai khoan gom 10 ky tu trung nhau
    for i in range (1, 10):
        print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,i,i,i,i))

def CuuQuy(format="BAAAAAAAAA"): #complete
#BAAAAAAAAA
#BBBBBBBBBA
    for j in range (1, 10):
        for i in range (0,10):
            if j != i:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,i,i,i,i,i,i,i,i,i))
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,j,j,j,j,j,j,i))
def BatQuyVip(format="BBAAAAAAAA"): #complete
#BBAAAAAAAA
#BBBBBBBBAA
    for j in range (1, 10):
        for i in range (0,10):
            if j != i:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,i,i,i,i,i,i,i,i))
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,j,j,j,j,j,i,i))
def BatQuy(format="BCAAAAAAAA"): #complete
#BCAAAAAAAA
#AAAAAAAABC
    for j in range (1, 10):
        for k in range (0,10):
            for i in range (0,10):
                if j!=k and k!=i:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,i,i,i,i,i,i,i,i))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,j,j,j,j,j,k,i))
                    
def ThatQuyTamHoa(format="BBBAAAAAAA"): #complete
#BBBAAAAAAA
#BBBBBBBAAA
    for j in range (1, 10):
        for i in range (0,10):
            if j != i:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,i,i,i,i,i,i,i))
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,j,j,j,j,i,i,i))
                
def ThatQuyTien(format="BCDAAAAAAA"): #complete
#BCDAAAAAAA
#AAAAAAABCD    
    for j in range (0, 10):
        for i in range (0,10):
            if j!=0 and j+2!= i and j+2<10:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,int(j+1),int(j+2),i,i,i,i,i,i,i))
            if i!=0 and i!=j and j+2<10:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,i,j,int(j+1),int(j+2)))
                
def ThatQuyLapDoiCuoi(format="BCCAAAAAAA"): #complete
    for j in range (1, 10):
        for k in range (0,10):
            for i in range (0,10):
                if j!=k and k!=i:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,k,i,i,i,i,i,i,i))
def ThatQuyLapDoiDau(format="BBCAAAAAAA"): #complete
    for j in range (1, 10):
        for k in range (0,10):
            for i in range (0,10):
                if j!=k and k!=i:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,k,i,i,i,i,i,i,i))
def ThatQuyLocPhat(format="B68AAAAAAA"): #complete
    for j in (1,2,3,4,5,7,9):
        for i in  (0,1,2,3,4,5,6,7,9):
            if i!=j:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,6,8,i,i,i,i,i,i,i))
    for j in (0,1,2,3,4,5,7,9):
        for i in (0,1,2,3,4,5,6,7,9):
            if i!=j:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,6,8,j,i,i,i,i,i,i,i))
def ThatQuyPhatLoc(format="B86AAAAAAA"): #complete
    for j in (1,2,3,4,5,7):
        for i in range (0,10):
            if (i!=6):
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,8,6,i,i,i,i,i,i,i))
    for j in (0,1,2,3,4,5,7,9):
        for i in range (0,10):
            if (i!=j):
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,8,6,j,i,i,i,i,i,i,i))
def ThatQuyGanh(format="BCBAAAAAAA"): #complete
#BCBAAAAAAA
#AAAAAAABCB
    for j in range (0, 10):
        for k in range (0,10):
            for i in range (0,10):
                if j!=k and j!=i and j!=0:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,j,i,i,i,i,i,i,i))
                if j!=k and j!=i and i!=0:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,i,j,k,j))    
def ThatQuy(format="BDCAAAAAAA"): #complete
    for j in range (1, 10):
        for k in range (0,10):
            for l in range (0,10):
                if (j!=k) and (k!=l) and (j!=l):
                    if not ((j==6 and k==8) or (j==8 and k==6) or (k==6 and l==8) or (k==8 and l==6)):
                        if not (int(l)==int(k)+1 and int(k)==int(j)+1):
                            for i in range (0,10):
                                if (i!=l):
                                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,l,i,i,i,i,i,i,i))
                                if i!=0 and i!=j:
                                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,i,j,k,l))

def LucQuyVip(format="BBBBAAAAAA"): #complete
#BBBBAAAAAA
#BBBBBBAAAA
    for j in range (1, 10):
        for i in range (0,10):
            if j != i:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,j,i,i,i,i,i,i))
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,j,j,j,i,i,i,i))

def LucQuyTamHoa(format="BBBCAAAAAA"): #complete
    #BBBCAAAAAA
    #BCCCAAAAAA
    #AAAAAABCCC
    #AAAAAABCCC
    for j in range (0, 10):
        for k in range (0, 10):
            for i in range (0,10):
                if j != k and k!=i and j!=0:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,k,i,i,i,i,i,i))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,k,k,i,i,i,i,i,i))
                if i!=0 and i!=j and j != k:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,j,j,j,k))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,j,k,k,k))

def LucQuyLocPhatVip(format="BBBCAAAAAA"): #complete
    #6868AAAAAA
    #6688AAAAAA
    #8668AAAAAA
    #8686AAAAAA
    #AAAAAA6868
    #AAAAAA6688
    #AAAAAA8668
    #AAAAAA8686
            for i in range (0,10):
                if i!=8:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,6,8,6,8,i,i,i,i,i,i))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,6,6,8,8,i,i,i,i,i,i))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,8,6,6,8,i,i,i,i,i,i))
                if i!=6:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,8,6,8,6,i,i,i,i,i,i))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,8,8,6,6,i,i,i,i,i,i))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,6,8,8,6,i,i,i,i,i,i))
            for i in range (1,10):
                if i!=6:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,6,8,6,8))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,6,6,8,8))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,6,8,8,6))
                if i!=8:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,8,6,8,6))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,8,8,6,6))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,8,6,6,8))


def LucQuyTien(format="BCDEAAAAAA"):#complete
    #BCDEAAAAAA
    #AAAAAABCDE
    for j in range (0, 7):
        for i in range (0,10):
            if j+3 != i and j!=0:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,int(j+1),int(j+2),int(j+3),i,i,i,i,i,i))
            if j+3 <10 and i!=0 and i!=j:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,j,int(j+1),int(j+2),int(j+3)))

def LucQuyLapSongDoi(format="BBCCAAAAAA"):#complete
    #BBCCAAAAAA
    #AAAAAABBCC
    for j in range (0, 10):
        for k in range (0,10):
            for i in range (0,10):
                if j!=0 and j!=k and k!=i:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,k,k,i,i,i,i,i,i))
                if i!=0 and i!=j and j!=k:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,j,j,k,k))

def LucQuyLapDoiDau(format="BBCDAAAAAA"):#complete
    for j in range (1, 10):
        for k in range (0,10):
            for l in range (0,10):
                for i in range (0,10):
                    if j!=k and k!=l and l!=i:
                        print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,k,l,i,i,i,i,i,i))

def LucQuyLapDoiCuoi(format="CDBBAAAAAA"):#complete
    for j in range (1, 10):
        for k in range (0,10):
            for l in range (0,10):
                for i in range (0,10):
                    if j!=k and k!=l and l!=i:
                        print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,l,l,i,i,i,i,i,i))

def LucQuyGanh(format="BCCBAAAAAA"):#complete
    #BCCBAAAAAA
    #AAAAAABCCB
    for j in (0,1,2,3,4,5,7,9):
        for k in (0,1,2,3,4,5,7,9):
            for i in range (0,10):
                if j!=0 and j!=k and j!=i :
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,j,k,k,j))
                if i!=0 and i!=j and j!=k :
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,j,k,k,j))

def LucQuy(format="BDCEAAAAAA"):#complete
    #BDCEAAAAAA
    #AAAAAABDCE
    for j in range (0, 10):
        for k in range (0,10):
            for l in range (0,10):
                for m in range (0,10):
                    for i in range (0,10):
                        if j!=0 and j!=k and l!=m and not (j==6 and k==8) and not (j==6 and k==6) and  not (j==8 and k==6) and not (j==8 and k==8) and not (l==6 and m==8) and not (l==6 and m==8) and not (l==8 and m==6) and not(l==8 and m==8) and not (j==m and k==l):
                            print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,l,m,i,i,i,i,i,i))
                        if i!=0 and i!=j and j!=k and l!=m and not (j==6 and k==8) and not (j==6 and k==6) and  not (j==8 and k==6) and not (j==8 and k==8) and not (l==6 and m==8) and not (l==6 and m==8) and not (l==8 and m==6) and not(l==8 and m==8) and not (j==m and k==l):
                            print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,i,j,k,l,m))
def NguQuyVip(format="BBBBBAAAAA"):#complete
    #BBBBBAAAAA
    for j in range (1, 10):
        for i in range (0,10):
            if j != i:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,j,j,i,i,i,i,i))

def NguQuyTien(format="BCDEFAAAAA"):#complete
    #BCDEFAAAAA
    #AAAAABCDEF
    for j in range (0, 10):
        for i in range (0,10):
            if j!=0 and j+4<10 and j+4 != i:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,int(j+1),int(j+2),int(j+3),int(j+4),i,i,i,i,i))
            if i!=0 and j+4<10 and j != i:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,j,int(j+1),int(j+2),int(j+3),int(j+4)))

def NguQuyLap4Dau(format="BBBBCAAAAA"): #complete
    #BBBBCAAAAA
    #AAAAABBBBC
    for j in range (0, 10):
        for k in range (0,10):
            for i in range (0,10):
                if j!=0 and j!=k and k!=i:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,j,k,i,i,i,i,i))
                if i!=0 and j!=k and j!=i:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,j,j,j,j,k))

def NguQuyLap4Cuoi(format="BCCCCAAAAA"):#complete
    for j in range (0, 10):
        for k in range (0,10):
            for i in range (0,10):
                if j!=0 and j!=k and k!=i:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,k,k,k,i,i,i,i,i))
                if 0!=0 and j!=k and j!=i:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,j,k,k,k,k))

def NguQuyTamHoaLocPhat(format="68BBBAAAAA"):#complete
    #68BBBAAAAA
    #66BBBAAAAA
    #86BBBAAAAA
    #88BBBAAAAA
    #BBB68AAAAA
    #BBB66AAAAA
    #BBB86AAAAA
    #BBB88AAAAA

    #AAAAA68BBB
    #AAAAA66BBB
    #AAAAA86BBB
    #AAAAA88BBB
    #AAAAABBB68
    #AAAAABBB66
    #AAAAABBB86
    #AAAAABBB88
    for j in range (0, 10):
        for i in range (0,10):
            if j!=0 and j!=i and j!=6:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,6,6,j,j,j,i,i,i,i,i))
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,8,6,j,j,j,i,i,i,i,i))
            if j!=0 and i!=6 and j!=8:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,8,6,i,i,i,i,i))
            if j!=0 and i!=8 and j!=6:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,8,8,i,i,i,i,i))
            if j!=0 and j!=i and j!=i:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,6,6,j,j,j,i,i,i,i,i))
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,8,6,j,j,j,i,i,i,i,i))
            if j!=0 and j!=6 and i!=8:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,6,8,i,i,i,i,i))
            if j!=0 and j!=6 and j!=6:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,6,6,i,i,i,i,i))
            #---
            if i!=0 and i!=6 and j!=6:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,6,6,j,j,j))
            if i!=0 and i!=8 and j!=6:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,8,6,j,j,j))
            if i!=0 and i!=j and j!=8:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,j,j,j,8,6))
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,j,j,j,8,8))
            if i!=0 and i!=6 and j!=6:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,6,6,j,j,j))
            if i!=0 and i!=8 and j!=6:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,8,6,j,j,j))
            if i!=0 and i!=j and j!=6:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,j,j,j,6,8))
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,j,j,j,6,6))

def NguQuyTamHoaLap(format="BBCCCAAAAA"):#complete
    #BBCCCAAAAA
    #BBBCCAAAAA
    #AAAAABBCCC
    #AAAAABBBCC
    for j in range (0, 10):
        for k in range (0,10):
            for i in range (0,10):
                if j!=0 and j!=k and k!=i and not (j==6 or j==8 or k==6 or k==8):
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,k,k,k,i,i,i,i,i))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,k,k,i,i,i,i,i))
                if i!=0 and i!=j and j!=k and not (j==6 or j==8 or k==6 or k==8):
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,j,j,k,k,k))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,j,j,j,k,k))

def NguQuyGanh(format="BBCBBAAAAA"):#complete
    #BBCBBAAAAA
    #AAAAABBCBB
    for j in (0,1,2,3,4,5,6,7,8,9):
        for k in (0,1,2,3,4,5,6,7,8,9):
            for i in range (0,10):
                if j!=0 and j!=k and j!=i :
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,k,j,j,i,i,i,i,i))
                if i!=0 and i!=j and j!=k :
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,i,j,j,k,j,j))

def TuQuyVip(format="BBBBCCAAAA"):#complete
    #BBBBCCAAAA
    #BBCCCCAAAA
    #AAAABBBBCC
    for j in range (0, 10):
        for k in range (0,10):
            for i in range (0,10):
                if j!=0 and j != k and k!=i :
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,j,k,k,i,i,i,i))
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,k,k,k,j,i,i,i,i))
                if i!=0 and i!=j and j!=k :
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,j,j,j,j,k,k))

def TuQuyTamHoaLap(format="BBBCCCAAAA"):#complete
    #BBBCCCAAAA
    #AAAABBBCCC
    for j in range (0, 10):
        for k in range (0,10):
            for i in range (0,10):
                if j!=0 and j!=k and k!=i:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,k,k,k,i,i,i,i))
                if i!=0 and i!=j and j!=k:
                    print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,j,j,j,k,k,k))

def TuQuyTien(format="BCDEFGAAAA"):#complete
    #BCDEFGAAAA
    #AAAABCDEFG
    for j in range (0,10):
        for i in range (0,10):
            if j!=0 and j+5<10 and j+5 != i:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,int(j+1),int(j+2),int(j+3),int(j+4),int(j+5),i,i,i,i))
            if i!=0 and j+5<10 and j != i:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,i,i,i,i,j,int(j+1),int(j+2),int(j+3),int(j+4),int(j+5)))

def TamHoaVip(format="BCCCDDDAAA"):#complete
    #BCCCDDDAAA
    #CCCDDDAAAB
    for j in range (0, 10):
        for k in range (0,10):
            for l in range (0,10):
                for i in range (0,10):
                    if j!=0 and j != k and k!=l and l!=i :
                        print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,k,k,l,l,l,i,i,i))
                        print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,j,k,k,k,l,l,l,i))

def TamHoaTien(format="ABCDBCDBCD"):#complete
    #ABCDBCDBCD
    #BCDBCDABCD
    for j in range (0, 10):
        for k in range (0,8):
            for l in range (0,9):
                for i in range (0,10):
                    if j!=0 and l==k+1 and i==l+1:
                        print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,l,i,k,l,i,k,l,i))
                    if j!=0 and l==k+2 and i==l+2:
                        print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,l,i,k,l,i,k,l,i))
                    if j!=0 and k==j+1 and l==k+1:
                        print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,l,j,k,l,j,k,l,i))
                    if j!=0 and k==j+2 and l==k+2:
                        print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,l,j,k,l,j,k,l,i))

def TamHoaLap(format="ABBBCCCDDD"):#complete
    #ABBBCCCDDD
    #CCCDDDBBBA
    for j in range (0, 10):
        for k in range (0,10):
            for l in range (0,10):
                for i in range (0,10):
                    if j!=0 and j!=k and k!=l and l!=i:
                        print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,k,k,k,l,l,l,i,i,i))
                    if k!=0 and k!=l and l!=i and i!=j:
                        print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,k,k,k,l,l,l,i,i,i,j))

def SongHyVip(format="AABBCCDDEE"):#complete
    #AABBCCDDEE
    for j in range (1, 10):
        for k in range (0,10):
            for l in range (0,10):
                for h in range (0,10):
                    for i in range (0,10):
                        if j != k and k!=l and l!=h and h!=i :
                            print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,j,k,k,l,l,h,h,i,i))
def SongHyLap(format="ABABABABAB"):#complete
    for j in range (1, 10):
        for i in range (0,10):
            if j!=i:
                print("%s,%s,%d%d%d%d%d%d%d%d%d%d" %(str(sys._getframe().f_code.co_name),format,j,i,j,i,j,i,j,i,j,i))

def main():
    ThapQuy()
    CuuQuy()
    BatQuyVip()
    BatQuy()
    ThatQuyTamHoa()
    ThatQuyTien()
    ThatQuyLapDoiCuoi()
    ThatQuyLapDoiDau()
    ThatQuyLocPhat()
    ThatQuyPhatLoc()
    ThatQuyGanh()
    ThatQuy()
    LucQuyVip()
    LucQuyTamHoa()
    LucQuyLocPhatVip()
    LucQuyTien()
    LucQuyLapSongDoi()
    LucQuyLapDoiDau()
    LucQuyLapDoiCuoi()
    LucQuyGanh()
    LucQuy()
    NguQuyVip()
    NguQuyTien()
    NguQuyLap4Dau()
    NguQuyLap4Cuoi()
    NguQuyTamHoaLocPhat()
    NguQuyTamHoaLap()
    NguQuyGanh()
    TuQuyVip()
    TuQuyTamHoaLap()
    TuQuyTien()
    TamHoaTien()
    TamHoaLap()
    SongHyVip()
    SongHyLap()
    

if __name__ == "__main__":
    main()

