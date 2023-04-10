# python3
M = 13
Q = 256
def read_input():
    
    inp = input()
    if 'I' in inp:
        P=input()
        T=input()
        
    elif 'F' in inp: 
        with open("./tests/06", mode='r',encoding="utf8") as fail:
            P=fail.readline()
            T=fail.readline()
    else: 
        print("Wrong format")
        return
    
    return (P.rstrip(), T.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def hashing(string):
    global M, Q

    res=0
    for ch in str(string):
        res = (M*res + ord(ch)) % Q

    return res

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    global M, Q 
    res=[]
    m = len(pattern)
    n = len(text)

    multiplier=1
    for i in range(m-1):
        multiplier = (multiplier*M) % Q
    
    t=text[:m]
    pHash = hashing(pattern)
    tHash = hashing(t)
    
    for i in range(n-m):

        if pHash == tHash:
            if t==pattern:
                res.append(str(i))
        t=t[1:]+text[i+m]
        tHash = (M*(tHash-ord(text[i])*multiplier) + ord(text[i+m])) % Q
        if tHash<0:
            t+=Q

    if pHash == tHash:
        if t==pattern:
            res.append(str(n-m))
        
    # and return an iterable variable
    return res


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

