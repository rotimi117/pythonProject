student_records = [{ 'id' : 180584,'name' : "oluwadurotimi",'scores': (90,79,70)},
                    {'id' : 189356, 'name': 'bukayo saka', 'score' : (40,65,43)},
                    {'id' : 189356, 'name': 'bukayo saka', 'score' : (40,65,43)},
                    {'id' : 189356, 'name': 'bukayo saka', 'score' : (40,65,43)},
                    {'id' : 189356, 'name': 'bukayo saka', 'score' : (40,65,43)}
]
student_records.append({'id' : 189356, 'name': 'bukayo saka', 'score' : (40,65,43)})
student_records.append({'id' : 189356, 'name': 'bukayo saka', 'score' : (40,65,43)})

student_records.remove(student_records[3])

print(student_records)




# print(list(filter(lambda n: n % 2 != 0, list3)))