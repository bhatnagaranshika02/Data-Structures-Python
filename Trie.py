class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=False

class Trie:
    def __init__(self):
        self.root=self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self,ch):
        return ord(ch)-ord('a')

    def insert(self,key):
        pCrawl = self.root
        for i in range(len(key)):
            index = self._charToIndex(i)
            if not pCrawl.children[index]:
                pCrawl.children[index]=self.getNode()
            pCrawl=pCrawl.children[index]
        pcrawl.isEndOfWord=True


    def search(self,key):
        pCrawl=self.root
        for i in range(len(key)):
            index = self._charToIndex(key[i])
            if not pCrawl.children[i]:
                return False
            pCrawl=pCrawl.children[i]
        return pCrawl!=None and pCrawl.isEndOfWord


def main(): 

  

    # Input keys (use only 'a' through 'z' and lower case) 

    keys = ["the","a","there","anaswe","any", 

            "by","their"] 

    output = ["Not present in trie", 

              "Present in trie"] 

  

    # Trie object 

    t = Trie() 

  

    # Construct trie 

    for key in keys: 

        t.insert(key) 

  

    # Search for different keys 

    print("{} ---- {}".format("the",output[t.search("the")])) 

    print("{} ---- {}".format("these",output[t.search("these")])) 

    print("{} ---- {}".format("their",output[t.search("their")])) 

    print("{} ---- {}".format("thaw",output[t.search("thaw")])) 

  

if __name__ == '__main__': 

    main() 
