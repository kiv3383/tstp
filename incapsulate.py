class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

data1 = Data()
print(data1.nums)
data1.change_data(0, 10)
print(data1.nums)
data1.nums[0] = 100
print(data1.nums)

