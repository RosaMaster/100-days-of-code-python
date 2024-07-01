with open("file1.txt") as file1:
    file1_data = file1.readlines()
    print(file1_data)

with open("file2.txt") as file2:
    file2_data = file2.readlines()
    print(file2_data)

# compare those two lists if common value
result = [int(number) for number in file1_data if number in file2_data]

# Write your code above 👆
print(result)
