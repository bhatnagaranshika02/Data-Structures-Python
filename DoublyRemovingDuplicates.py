def removedupli(self):
    temp=self.start
    d=[]
    while temp:
        if temp.data not in l:
            l.append(temp.data)
            temp=temp.next
        else:
            nxt=temp.next
            self.delete(temp)
            temp=nxt
            
