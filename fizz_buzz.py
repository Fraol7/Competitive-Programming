class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        my_result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                my_result.append("FizzBuzz")
            elif i % 3 == 0:
                my_result.append("Fizz")
            elif i % 5 == 0:
                my_result.append("Buzz")
            else:
                my_result.append(str(i))
        return my_result
