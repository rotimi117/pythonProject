# file = open("student_records.txt", mode='w')
# file.write("001 rotimi 89 \n")
# file.write("002 bukayo 89\n")
# file.write("003 smith-rowe 89\n")
# file.write("004 saliba 89\n")
# file.write("005 zinchenco 89\n")
# file.write("006 martinelli 89\n")
# file.close()
#
# with open("record2.txt", mode='w') as file:
#     file.write("007 gabriel 78 \n")
#     file.write("007 nkietah 78 \n")
#     file.write("007 trossard 78 \n")
#     file.write("007 partey 78 \n")
<<<<<<< HEAD


with open("product.txt", mode='w') as file:
    file.write("200_000 bag of rice 4 \n")
    file.write("300_000 bag of beans 7 \n")
    file.write("200_000 bag of garri 6 \n")
    file.write("200_000 bag of salt 7 \n")
    file.write("200_000 bag of meat 5 \n")
    file.write("200_000 bag of bread 4 \n")

=======
import json

# with open("product.txt", mode='w') as file:
#     file.write("200_000 bag of rice 4 \n")
#     file.write("300_000 bag of beans 7 \n")
#     file.write("200_000 bag of garri 6 \n")
#     file.write("200_000 bag of salt 7 \n")
#     file.write("200_000 bag of meat 5 \n")
#     file.write("200_000 bag of bread 4 \n")


records = {
    "Student record": [
        {"id": 1, "name": "Ebuka", "age": 41},
        {"id": 2, "name": "Ebuk", "age": 44},
        {"id": 3, "name": "Ebua", "age": 42}
    ]
}

with open("records.json", mode="w") as record:
    json.dump(records, record)

with open("records.json", mode="r") as record2:
    print(json.dumps(json.load(record2), indent=4))
>>>>>>> d3c72c6 (Initial commit)

