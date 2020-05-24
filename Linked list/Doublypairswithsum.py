def pair_with_sum(self,summ):
    temp=self.head
    tmp=None
    pairs=[]
    while temp:
        tmp=temp.next
        while tmp:
            if temp.data+tmp.data==summ:
                pairs.append('('+str(temp.data)+','+str(tmp.data)+')')
            else:
                tmp=tmp.next
        temp=temp.next
    return pairs
