from pythonds.basic import Queue
def hotpotato(li,n):
    simqueue = Queue()
    for i in li:
        simqueue.enqueue(i)
    while simqueue.size() > 1:
        for i in range(n):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()
print(hotpotato(['anshika','aman','goru','harsh']))
            
