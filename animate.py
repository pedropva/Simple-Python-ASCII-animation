import time


def animate(seq,fps,repeat=20,end_reverse=False):
    i=1
    while i<repeat:
        print('   '+seq[i%len(seq)-1],end='\r'*(len(seq[0])+10))
        time.sleep(1/fps);i+=1
        if(end_reverse and i%len(seq)-1==0):
            seq = seq[::-1]
        start = 0

if __name__=='__main__':
    seq = [
    "∠( ᐛ 」∠)＿                        ",
    "∠( ᐛ 」∠)＿                        ",
    "∠( ᐛ 」∠)＿                        ",
    "三ᕕ( ᐛ )ᕗ                         ",
    "三三ᕕ( ᐛ )ᕗ                       ",
    "三三三ᕕ( ᐛ )ᕗ                     ",
    "三三三三ᕕ( ᐛ )ᕗ                   ",
    "三三三三三ᕕ( ᐛ )ᕗ                 ",
    "三三三三三三ᕕ( ᐛ )ᕗ               ",
    "三三三三三三三ᕕ( ᐛ )ᕗ             ",
    "三三三三三三三三ᕕ( ᐛ )ᕗ           ",
    "三三三三三三三三三ᕕ( ᐛ )ᕗ         ",
    "三三三三三三三三三三ᕕ( ᐛ )ᕗ       ",
    "三三三三三三三三三三三ᕕ( ᐛ )ᕗ     ",
    "三三三三三三三三三三三三ᕕ( ᐛ )ᕗ   ",
    "三三三三三三三三三三三三三ᕕ( ᐛ )ᕗ ",
    "三三三三三三三三三三三三三三ᕕ( ᐛ )ᕗ"]
 
    animate(seq,5,end_reverse=False)
