def merge(words,left,mid,right):
    L = words[left:mid+1]
    R = words[mid+1:right+1]
    i = j = 0
    k = left
    while i <len(L) and j < len(R):
        if len(L[i]) <= len(R[j]):
            words[k] = L[i]
            i += 1
        else:
            words[k] = R[j]
            j +=1
        k +=1
    while i < len(L):
        words[k] = L[i]
        i +=1
        k +=1
    while j < len(R):
        words[k] = R(j)
        j +=1
        k +=1

def merge_sort(words,left,right):
    if left < right:
        mid=(left+right)//2
        merge_sort(words,left,mid)
        merge_sort(words,mid+1,right)
        merge(words,left,mid,right)

words = ["potato", "broccoli", "carrot", "turnip", "pumpkin", "plum", "apple", "orange", "banana", "kiwi", "grapefruit"]

merge_sort(words,0,len(words)-1)
print(words)