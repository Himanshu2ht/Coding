#function
'''def print_list(list):
    for el in list:
        print(el, end= " ")

nums=["her", "hhrr","jdjdh"]
print_list(nums)

def fac(n):
    f=1
    for i in range(1, n+1):
        f*=i
    print('\n',f, sep='')

fac(5)'''

# Recursion

'''def fac(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fac(n-1)

print(fac(5))'''

#prc

#q 1
'''def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
    
print(sum(10))'''

# q 2

def lst_prt(list, idx=0):
    if idx== len(list):
        return
    print(list[idx])
    lst_prt(list,idx+1)

lst=[1,2,3,4,5]
lst_prt(lst)