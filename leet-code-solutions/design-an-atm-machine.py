class ATM:

    def __init__(self):
        self.notes=[0,0,0,0,0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        withdraw_amount = [0,0,0,0,0]
        order = [500,200,100,50,20]
        for i in range(5):
            freq = self.notes[4-i]
            withdraw_amount[i] = amount//order[i]
            if withdraw_amount[i] > freq:
                withdraw_amount[i] = freq
                amount -= freq * order[i]
            else :
                amount = amount % order[i]
        if amount == 0:
            for i in range(5): 
                if self.notes[4-i] - withdraw_amount[i] < 0:
                    return ([-1])
            for i in range(5):
                self.notes[4-i] -= withdraw_amount[i]
            return (withdraw_amount[::-1])
        else :
            return ([-1])

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)