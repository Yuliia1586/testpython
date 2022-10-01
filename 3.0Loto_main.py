from Lotomodul  import record,choice,pnumber,result,wnumber,readrec,saverec,readrecjson,saverecjson  
import time

def main(args):
    pname, qnumber,maxnumber, pchance=record()
    rnlist=choice(qnumber,maxnumber)
    for i in range(1, pchance+1):
        if i < pchance:
            print("Спроба №", i, ":")
        if i == pchance:
            print("Це Ваша остання спроба:")
        plist=pnumber(pchance,qnumber,maxnumber)
        #result(rnlist,plist)
        correctnumber = result(set(rnlist), plist)
        
    filename = pname + ".json"
    game = readrecjson(filename)
    
    game.append({
        "гравець": pname,
        "параметри": (qnumber,maxnumber),
        "генеровані числа": rnlist,
        #"числа гравця": plist,
        "співпадіння": correctnumber,
        "час": time.time()
        })
    
    saverecjson(filename, game)
    
    wnumber(rnlist)
    return 0

if __name__=='__main__':
    import sys
    sys.exit(main(sys.argv))
