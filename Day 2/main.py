data = open("D:\Python\AoC 2020\Day 2\input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]

def part_one():
    new_data = []
    for item in data:
        index_letter = str(item[item.index(":") - 1]) #Extracting the letter
        index_from = int(item[:item.index("-")]) #Min number of letters
        index_to = int(item[item.index("-") + 1:item.index(":") - 1]) #Max number of letters
        index_count = item.count(index_letter) - 1 #How many letters in the string
    
        if index_count >= index_from and index_count <= index_to:
            new_data.append(item)
    return len(new_data)

def part_two():
        
    new_data = []
    for item in data:
        index_letter = str(item[item.index(":") - 1]) #Extracting the letter
        first_index = int(item[:item.index("-")]) #First letter
        second_index = int(item[item.index("-") + 1:item.index(":") - 1]) #Second letter

        # print(index_letter)
        # print(first_index)
        # print(second_index)
        # print(item[first_index])
        
        print(item[item.index(":") + 1:])

        # if item[first_index] == index_letter and item[second_index] == index_letter:
        #     print(item)
    
        
            
    
print(part_two())
