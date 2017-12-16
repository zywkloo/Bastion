def bubblesort(seq):  
    swap=False
    for j in range(len(seq)-1):
        for i in range(len(seq)-1-j):
            if seq[i]>seq[i+1]:
                seq[i],seq[i+1]=seq[i+1],seq[i]
                swap=True
        if swap==False:
            return seq   
    return seq 
if __name__=='__main__':  
    seq=[4,5,7,9,7,5,1,0,7,-2,3,-99,6]  
    print(bubblesort(seq))  
      