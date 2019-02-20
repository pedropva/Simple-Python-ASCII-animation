import time

def animate(seq,fps,end_reverse=False):
    i=1
    while 1:
        print('   '+seq[i%len(seq)-1],end='\r'*(len(seq[0])+10))
        time.sleep(1/fps);i+=1
        if(end_reverse and i%len(seq)-1==0):
            seq = seq[::-1]
        start = 0

if __name__=='__main__':
    seq = [
    "o/        o",
    "o->       o",
    "o- >      o",
    "o-  >     o",
    "o-   >    o",
    "o-    >   o",
    "o-     >  o",
    "o-      > o",
    "o-       >o",
    "o-        *",
    "o-        #",
    "o          ",
    "o          ",
    "o          "]
    animate(seq,5,end_reverse=False)
