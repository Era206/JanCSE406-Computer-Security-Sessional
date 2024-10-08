import random
import time
def prime_testing(n,k):
    if n%2==0:
        return False
    s=0
    d=n-1
    while d%2==0:
        d//=2
        s+=1
    for i in range(k):
        a=random.randint(2,n-2)
        x=mod_expo(a,d,n)
        for j in range(s):
            y=mod_expo(x,2,n)
            if y==1 and x!=1 and x!=n-1:
                return False
            x=y
        if y!=1:
            return False

    return True


def mod_expo(a,d,n):
    ans=1
    while d!=0:
        if d%2==0:
            a=(a*a)%n
            d=d>>1
        else:
            ans=(a*ans)%n
            a=(a*a)%n
            d=d>>1
    
    return ans


def get_prime_p(bits):
    while True:
        p=random.getrandbits(bits)
        if ((p>>(bits-1))&1)==0:
            p=p|1<<(bits-1)
        
        if prime_testing(p,30)==True:
            return p
        

def get_safe_prime_p(bits):
    while True:
        p=get_prime_p(bits)
        q=p>>1
        if prime_testing(q,30)==True:
            return p

# g 1, p-1 hote parbena   
def get_generator_g(min, max,p):
    while True:
        g=random.randint(min, max)
        check1=mod_expo(g,2,p)
        check2=mod_expo(g,p//2,p)
        if check1!=1 and check1!=1:
            return g
        


    

def key_generation_for_sender(size, g, p):
    b=get_prime_p(size//2)
    B=mod_expo(g,b,p)
    return B,b

def secret_key_generation_client(p, b,A):
    check2=mod_expo(A,b,p)
    return check2






