details = [
  {
    "id": 1,
    "firstName": "John",
    "lastName": "Doe",
    "age": 28,
    "email": "john.doe@example.com",
    "occupation": "Software Engineer"
  },
  {
    "id": 2,
    "firstName": "Jane",
    "lastName": "Smith",
    "age": 32,
    "email": "jane.smith@example.com",
    "occupation": "Data Analyst"
  },
  {
    "id": 3,
    "firstName": "Michael",
    "lastName": "Johnson",
    "age": 40,
    "email": "michael.johnson@example.com",
    "occupation": "Project Manager"
  },
  {
    "id": 4,
    "firstName": "Emily",
    "lastName": "Davis",
    "age": 25,
    "email": "emily.davis@example.com",
    "occupation": "Marketing Specialist"
  },
  {
    "id": 5,
    "firstName": "Daniel",
    "lastName": "Martinez",
    "age": 35,
    "email": "daniel.martinez@example.com",
    "occupation": "UX Designer"
  },
  {
    "id": 6,
    "firstName": "Sarah",
    "lastName": "Brown",
    "age": 30,
    "email": "sarah.brown@example.com",
    "occupation": "Accountant"
  },
  {
    "id": 7,
    "firstName": "David",
    "lastName": "Wilson",
    "age": 29,
    "email": "david.wilson@example.com",
    "occupation": "Business Analyst"
  },
  {
    "id": 8,
    "firstName": "Jessica",
    "lastName": "Moore",
    "age": 27,
    "email": "jessica.moore@example.com",
    "occupation": "HR Manager"
  },
  {
    "id": 9,
    "firstName": "Christopher",
    "lastName": "Taylor",
    "age": 42,
    "email": "christopher.taylor@example.com",
    "occupation": "IT Consultant"
  },
  {
    "id": 10,
    "firstName": "Amanda",
    "lastName": "Anderson",
    "age": 26,
    "email": "amanda.anderson@example.com",
    "occupation": "Content Writer"
  }
]


for i in details:
    if i["firstName"]:
         print("His name is,", i["firstName"], i["lastName"], "He is doing as: ",i["occupation"], "The mail id is :", i["email"]+".")
        # print("His mail id is :",i["email"])
        # print("The age of ", i["firstName"] , i["lastName"],  "is :" ,i["age"])
        
# for person in details:
    # if person['id'] != [1] :  # Skip the first id
    #  if person['id'] > 2 :  # Skip the first id
    #     print(person['firstName'])
    #  if person['id'] not in [1,5] :  # Skip the first id
    #     print(person['firstName'])    