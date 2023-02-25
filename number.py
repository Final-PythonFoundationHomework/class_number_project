from math import sqrt

class Number:
    def __init__(self, value: int):
        self.value = value

    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.get_number() % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.is_odd() == False

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        for i in range(2, int(sqrt(self.get_number()))+1):
            if self.get_number() % i == 0:
                return False
        
        return True

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        l = []
        for i in range(1, self.value+1):
            if self.get_number() % i == 0:
                l.append(i)
        
        return l

    def get_length(self):
        """
        Returns the number of digits in the number. 

        returns: int
        """
        return len(self.get_digits())

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        s = 0
        for i in self.get_digits():
            s += i
        
        return s
 
    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.get_number())[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return self.get_number() == self.get_reverse()
    
    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        if self.value == 0:
            return [0]
        digits = []
        i = abs(self.value)
        while i > 0:
            n = i%10
            digits.append(n)
            i = i // 10 
        return digits[::-1]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max(self.get_digits())

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min(self.get_digits())

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        return self.get_sum() / self.get_length()

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        digits = self.get_digits().sort()  # 1, 2, 3, 4
                                           # 0  1  2  3

        if self.get_length() % 2 == 1:
            return digits[self.get_length() // 2]
        
        else:
            n = self.get_length() // 2 - 1
            m = self.get_length() // 2 
            return (digits[n] + digits[m]) / 2

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return [self.get_min(), self.get_max()]

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        unique_digit = set(self.get_digits())
        frequency = {}
        for i in unique_digit:
            frequency[i] = self.get_digits().count(i)

        return frequency


number = Number(658723389)

# print(number.get_number())
# print(number.is_even())
# print(number.is_prime())
# print(number.get_divisors())
# print(number.get_length())
# print(number.get_sum())
# print(number.get_reverse())
# print(number.is_palindrome())
# print(number.get_digits())
# print(number.get_max())
# print(number.get_min())
# print(number.get_median())
# print(number.get_range())
print(number.get_frequency())

