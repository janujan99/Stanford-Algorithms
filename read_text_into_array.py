def read_array(filename):
     f = open(filename, "r")
     arr = f.read().split("\n")
     return [int(num) for num in arr[:-1]]

