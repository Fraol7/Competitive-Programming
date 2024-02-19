class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue = deque()
        for num in deck:
            if queue:
                queue.append(queue.popleft())
            queue.append(num)
        reverse_deck = []
        for idx in range(len(queue)-1, -1, -1):
            reverse_deck.append(queue[idx])
        return reverse_deck


        