class FibonacciNumber:
    def __init__(self):
        self.memorization = {}
        
    def calculate_fibonacchi(self,n):
        if n in self.memorization:
            return self.memorization[n]
        elif n < 2:
            return 1
        else:
            self.memorization[n] = self.calculate_fibonacchi(n-1) + self.calculate_fibonacchi(n-2)
            return self.memorization[n]

if __name__ == '__main__':
    obj = FibonacciNumber()
    print(obj.calculate_fibonacchi(100))
    print(obj.memorization)