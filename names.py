
def studentsInstructors(list):
    print users
    for key in list:
        print key
        #print list[key][i]["first_name"]
        for i in range(0,len(list[key])):
            first= list[key][i]["first_name"]
            last= list[key][i]["last_name"]
            print "{}: {} {} --{}".format(i+1,first,last,len(first)+len(last)) 



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

studentsInstructors(users)
"""
        for i in range(0,len(list)):
            print "{}. {} {} - {}".format(i+1,list[i]["first_name"],list[i]["last_name"],len(list[i]["first_name"])+len(list[i]["last_name"]))


            for i in range(0,len(list)):
                print "{}. {} {} - {}".format(i+1,list[i]["first_name"],list[i]["last_name"],len(list[i]["first_name"])+len(list[i]["last_name"]))


studentsInstructors(users)


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
#print students
#print students[0]
#print students[0]["first_name"]

def values(list):
    for i in range(0,len(list)):
        print "{}. {} {} - {}".format(i+1,list[i]["first_name"],list[i]["last_name"],len(list[i]["first_name"])+len(list[i]["last_name"]))

values(students)

Given the following list:

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
Copy
Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel

Part II
Now, given the following dictionary:

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
Copy
Create a program that prints the following format (including number of characters in each combined name):

Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13
Copy
Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application.

INSTRUCTOR SOLUTION

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def show_students(arr):
    for x in students:
        print x['first_name'], x['last_name']

def show_all(users):
    for role in users:
        counter = 0
        print role
        for person in users[role]:
            counter += 1
            first_name = person['first_name']
            last_name = person['last_name']
            length = len(person['first_name']) + len(person['last_name'])
            print "{} - {} {} - {}".format(counter, person['first_name'], person['last_name'], length)

show_students(students)
show_all(users)
"""