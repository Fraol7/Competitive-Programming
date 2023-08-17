class Solution:
	def maxEvents(self, events: List[List[int]]) -> int:
		n = len(events)
		events.sort()

		started = []
		count = i = 0
		curr_day = events[0][0]
		while i < n:
			while i < n and events[i][0]==curr_day:
				heappush(started, events[i][1])
				i += 1

			heappop(started)
			count += 1
			curr_day += 1
			
			while started and started[0]<curr_day: 
				heappop(started)
			if i<n and not started: 
				curr_day = events[i][0]

		while started:
			if heappop(started)>=curr_day:
				curr_day += 1
				count += 1

		return count
