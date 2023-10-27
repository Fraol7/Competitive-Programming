class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        left, right = 0, len(plants) - 1
        alice = capacityA
        bob = capacityB
        ctr = 0
        while right >= left:
            if right == left and alice >= bob:
                if alice < plants[left]:
                    alice = capacityA
                    ctr += 1
                return ctr
            elif right == left:
                if bob < plants[left]:
                    bob = capacityB
                    ctr += 1
                return ctr

            if alice < plants[left]:
                alice = capacityA
                ctr += 1

            if bob < plants[right]:
                bob = capacityB
                ctr += 1
            
            alice -= plants[left]
            bob -= plants[right]
            right -= 1
            left += 1
        return ctr
