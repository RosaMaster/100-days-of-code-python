# # link: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
#  #link: https://pandas.pydata.org/docs/reference/index.html
 
 
# '''with open("weather_data.csv") as data_file:
# #    data = data_file.readlines()
# #    print(data)'''
    
    
import pandas
import csv

# '''with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row[1])
        
        

        
# with open("weather_data.csv") as data_file2:
#     data2 = csv.reader(data_file2)
#     temperatura_string = []
#     temperatures = []
#     for row in data2:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#             temperatura_string.append(row[1])
#     print(temperatures)
#     print(temperatura_string)'''
    
    
# data = pandas.read_csv("weather_data.csv")
# print(data)

# # Tabela para dicionario
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# '''# media
# media = data["temp"].mean()
# print(media)'''

# # maximo
# maximo = data["temp"].max()
# print(maximo)

# # minimo
# minimo = data["temp"].min()
# print(minimo)

# # get data in columns
# print(data["condition"])
# print(data.condition)

# # get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# # get data day == Monday
# monday = data[data.day == "Monday"]
# print(monday.condition)

# # Convert temp em Celsius para Firenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("./new_data.csv")

