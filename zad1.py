def suma(x,z=0):
    return x*x+z

def pierwszy_znak(q=10605):
    if q==10605:
        return "BUUM"
    else:
        return q[0]

def cyfry(w):
    if w==1:
        return "jeden"
    if w==2:
        return "dwa"
    if w==3:
        return "trzy"
    else:
        return "inna"

def kot(t,r=""):
    if r=="":
        return t+" ma kota"
    else:
        return t+" ma kota i "+r

def liczenie(u,y=1):
    return range (0,u,y)

def powtarzanie(p,o):
    return p*o

