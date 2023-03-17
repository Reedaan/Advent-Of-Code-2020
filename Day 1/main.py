data = open("D:\Python\AoC 2020\Day 1\input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]
data = [int(x) for x in data]

def calculate():
    for position in range(len(data)- 1):
        for a in range(len(data)- 1):
            for c in range(len(data)):
                d = data[position] + data[a] + data[c]
                if d == 2020:
                    print(data[position])
                    print(data[a])
                    print(data[c])
                    result = data[position] * data[a] * data[c]
                    return result
        
    
    
print(calculate())
    
