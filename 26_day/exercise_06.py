studant_dict = {
    "studant": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas
studant_data_frame = pandas.DataFrame(studant_dict)
print(studant_data_frame)

for (key, value) in studant_data_frame.items():
    print(key)
    print(value)
    

for (index, row) in studant_data_frame.iterrows():
    print(row)
    print(row.studant)
    print(row.score)
    if row.score > 80:
        print(row.studant, row.score)