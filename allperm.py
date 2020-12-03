# Assignment 7, Task 1
# Name: Andrew Stuber
# Collaborators: friend
# Time Spent: 3 hrs

from typing import Set, Tuple

def all_perm(n:int )-> Set[Tuple[int, ...]]:
    if n == 1:
        result = set()
        result.add((1,))
        return result
    else:
        pre = all_perm(n-1)
        if n == 2:
            result2 = set()
            for i in pre:
                tup = (n,) + i
                result2.add(tup)
            pre = tuple(result2)
            for j in range(len(pre)):
                for k in range(len(pre[0])-1):
                    new_tup = pre[j][k+1:] + (n,) + pre[j][len(pre[0])-1: k+1]
                    pre = set(pre)
                    pre.add(new_tup)
                    pre = tuple(pre)
            return set(pre)
        else:
            pre = tuple(pre)
            temp = set()
            for j in range(len(pre)):
                for k in range(len(pre[0])+1):
                    new_tup = pre[j][0:k] + (n,) + pre[j][k:len(pre[0])] 
                    temp.add(new_tup)
            return temp
                    
print(all_perm(4))

            








