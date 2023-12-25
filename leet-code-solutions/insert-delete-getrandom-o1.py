class RandomizedSet:
    
    def __init__(self):
        self.bill = {} 
        self.val_bill = []   

    def insert(self, val: int) -> bool:
        if val in self.bill:    
            return False
        self.bill[val] = len(self.val_bill)    
        self.val_bill.append(val)          
        return True                     

    def remove(self, val: int) -> bool:
        if val not in self.bill:   
            return False
        index = self.bill[val]     
        last_val = self.val_bill[-1]           
        self.val_bill[index] = last_val         
        self.bill[last_val] = index 
        self.val_bill.pop()                    
        del self.bill[val]           
        return True                          

    def getRandom(self) -> int:
        return random.choice(self.val_bill)     
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()