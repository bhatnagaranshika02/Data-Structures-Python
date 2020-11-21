def bubble_sort(l):
    for i in range(1,len(l)-1):
        for j in range(1,len(l)-i-1):
            if l[j] > l[j-1]:
                l[j],l[j-1] = l[j-1],l[j]
    print(l)





def main():
    l = list(map(int,input().split()))
    bubble_sort(l)

main()
