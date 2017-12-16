def selectionsort(seq):  
    for j in range(len(seq)-1):
        low=j
        for i in range(j+1,len(seq)):
            if seq[low]>seq[i]:
                low=i
        if low!=j:
            seq[low],seq[j]=seq[j],seq[low]
    return seq 
if __name__=='__main__':  
    seq=[4,5,7,9,7,5,1,0,7,-2,3,-99,6]  
    print(selectionsort(seq))  
      