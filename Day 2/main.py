data = open("D:\Python\AoC 2020\Day 2\input.txt", "r").readlines()
data = [line.strip(" ") for line in data]
data = [line.strip("\n") for line in data]
data = [line.replace(" ", "") for line in data]

#Part one

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

#Part two

def part_two():
        
    new_data = []
    for item in data:
        index_letter = str(item[item.index(":") - 1]) #Extracting the letter
        first_index = int(item[:item.index("-")]) #First letter
        second_index = int(item[item.index("-") + 1:item.index(":") - 1]) #Second letter
        string_cut = item[item.index(":"):]  #Only letters in a string

        if string_cut[first_index] == index_letter and not string_cut[second_index] == index_letter:
            new_data.append(item)
            
        if string_cut[second_index] == index_letter and not string_cut[first_index] == index_letter:
            new_data.append(item)
    return len(new_data)
