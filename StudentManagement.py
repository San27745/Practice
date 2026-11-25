students ={
    101:{"name":"Sahil","Scores":[99,97,100]},
    102:{"name":"Mahesh","Scores":[69,91,10]},
    103:{"name":"Vibhav","Scores":[19,46,78]},
    104:{"name":"Atharva","Scores":[99,9,39]}
}

for sid,details in students.items():
    avg=sum(details["Scores"])/len(details["Scores"])
    details['Avg']=avg
    details['passed']=avg>=50

print("studens wjho paased")
for sid,details in students.items():
    if details['passed']:
        print(details['name'])
