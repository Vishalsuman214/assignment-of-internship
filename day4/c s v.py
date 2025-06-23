import csv

data=[[
    "name","address","mobile","email"]
      , ["Rahul", "Jaipur", "9348548556", "rahul@hmail.com"],
    ["pawan", "jaipur", "9348548556", "pawan@gmail.com"],
    ["sujal", "Bhilwara", "9812345678", "sujal@gmail.in"]
]
with open('data.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(data)
print("CSV file created successfully.")
            
# code of csv file
