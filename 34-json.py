import json

# P1

# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# data_json = json.dumps(data)
# print(data_json)

# with open('data.json', 'w') as f:
#     json.dump(data,f)
    
# with open('data.json') as f:
#     data1 = json.load(f)

# P2

# talaba = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
# talaba_json = json.dumps(talaba)

# with open('talaba.json', 'w') as f:
#     json.dump(talaba,f)
    
# with open('talaba.json') as f:
#     talaba1 = json.load(f)

# talaba1=json.loads(talaba_json)
# print(talaba1)

# P3

# with open('students.json') as f:
#     students = json.load(f)

# for item in students["student"]:
#     print(f"{item['name']} {item['lastname']}, {item['year']}-kurs, {item['faculty']} talabasi")

# P4

with open('python_json.json') as f:
    python_json = json.load(f)

title = python_json['query']['pages']['13801']['title']
data = python_json['query']['pages']['13801']['extract']

print(f"Agar Wikipediadan \t {title}\t deb qidirsangiz {data} chiqib keladi")