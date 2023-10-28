class GridTraveller:
    def __init__(self):
        self.memo = {}
        
    def grid_travel(self, m, n):
        key = str(m) + ',' + str(n)
        rev_key = str(n) + ',' + str(m)
        if key in self.memo:
            return self.memo[key]
        if rev_key in self.memo:
            return self.memo[rev_key]
        elif m == 0 or n == 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        else:
            self.memo[key] = self.grid_travel(m-1, n) + self.grid_travel(m, n-1)
            return self.memo[key]
            
if __name__ == '__main__':
    obj = GridTraveller()
    print(obj.grid_travel(4,4))