def a():
        f=open('./files/seq.txt','r')
        d={}



        for line in f:

            for u in line:
                if(u in d):
                     d[u]+=1

                else:
                    d[u]=1
        return d