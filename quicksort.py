def quicksort(seq):  
    if len(seq)<=1:  
        return seq  
    return (quicksort([x for x in seq[1:] if x <= seq[0]])+[seq[0]]+quicksort([x for x in seq[1:] if x > seq[0]]))
if __name__=='__main__':  
    seq=[4,5,7,9,7,5,1,0,7,-2,3,-99,6]  
    print(quicksort(seq)) 