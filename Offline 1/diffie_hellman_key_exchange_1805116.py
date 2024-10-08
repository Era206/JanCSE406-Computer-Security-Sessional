import random
import time
from tabulate import tabulate

def prime_testing(n,k):
    if n%2==0 or n==1:
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
            
        
        if prime_testing(p,10)==True:
            return p
        

# def get_safe_prime_p(bits):
#     while True:
#         p=get_prime_p(bits)
#         q=p>>1
#         if prime_testing(q,15)==True:
#             return p

def get_safe_prime_p(bits):
    while True:
        q=get_prime_p(bits-1)
        p=(q<<1)|1
        if prime_testing(p,10)==True:
            return p

# g 1, p-1 hote parbena   
def get_generator_g(min, max,p):
    while True:
        g=random.randint(min, max)
        check1=mod_expo(g,2,p)
        check2=mod_expo(g,p//2,p)
        if check1!=1 and check1!=1:
            return g


def key_generation(size):
    p=get_safe_prime_p(size)
    min=2
    max=random.randint(3,p-2)
    g=get_generator_g(min,max,p)

    a=get_prime_p(size//2)
    
    A=mod_expo(g,a,p)

    b=get_prime_p(size//2)
    B=mod_expo(g,b,p)

    check1=mod_expo(A,b,p)
    check2=mod_expo(B,a,p)


    print("prime generation done, generated prime p : "+str(p))
    print("for checking purpose, q=(p-1)/2: "+str(p>>1))
    print("primitive root g: "+ str(g))
    print("sender side prime, a: "+str(a))
    print("receiver side prime,b : "+str(b))
    print("A=g^a(mod p): "+str(A))
    print("B=g^b(mod p): "+str(B))
    print("shared key sender gets: "+str(check2))
    print("shared key from receiver gets: "+str(check2))



def key_generation_times(size):
    t1=time.perf_counter_ns()
    p=get_safe_prime_p(size)
    t2=time.perf_counter_ns()
    p_generating_time=(t2-t1)/1000000000
    min=2
    max=random.randint(3,p-2)
    t1=time.perf_counter_ns()
    g=get_generator_g(min,max,p)
    t2=time.perf_counter_ns()
    g_generating_time=(t2-t1)/1000000000

    t1=time.perf_counter_ns()
    a=get_prime_p(size//2)
    t2=time.perf_counter_ns()
    a_generating_time=(t2-t1)/1000000000

    t1=time.perf_counter_ns()  
    A=mod_expo(g,a,p)
    t2=time.perf_counter_ns()
    A_generating_time=(t2-t1)/1000000000

    b=get_prime_p(size//2)
    B=mod_expo(g,b,p)
    t1=time.perf_counter_ns()
    check1=mod_expo(A,b,p)
    t2=time.perf_counter_ns()
    shared_key_generating_time=(t2-t1)/1000000000
    check2=mod_expo(B,a,p)

    return p_generating_time,g_generating_time,a_generating_time,A_generating_time,shared_key_generating_time


def calculate_time(iter):
    matrix = []
    for j in range(128,257,64):
        # print(j)
        p_generating_time=0.0
        g_generating_time=0.0
        a_generating_time=0.0
        A_generating_time=0.0
        shared_key_generating_time=0.0
        for i in range(iter):
            p,g,a,A,key=key_generation_times(j)
            p_generating_time+=p
            g_generating_time+=g
            a_generating_time+=a
            A_generating_time+=A
            shared_key_generating_time+=key

        matrix.append(str(j))
        matrix.append(str(p_generating_time/iter))
        matrix.append(str(g_generating_time/iter))
        matrix.append(str(a_generating_time/iter))
        matrix.append(str(A_generating_time/iter))
        matrix.append(str(shared_key_generating_time/iter))
    
    headers = ["k", "p", "g", "a or b", "A or B", "shared key"]
    matrix = [matrix[i:i+6] for i in range(0, len(matrix), 6)]
    table = tabulate(matrix, headers=headers, tablefmt="grid")
    print(table)

key_generation(128)
calculate_time(5)




