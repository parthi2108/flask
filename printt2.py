comp={
  "company": {
    "name": "Tech Solutions",
    "employees": [
      {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "position": "Software Engineer",
        "skills": ["Python", "JavaScript", "Docker"],
        "salary": 80000
      },
      {
        "id": 2,
        "name": "Bob",
        "age": 28,
        "position": "DevOps Engineer",
        "skills": ["Kubernetes", "AWS", "Ansible"],
        "salary": 85000
      },
      {
        "id": 3,
        "name": "Charlie",
        "age": 32,
        "position": "Data Scientist",
        "skills": ["Python", "SQL", "Machine Learning"],
        "salary": 95000
      }
    ],
    "location": {
      "city": "New York",
      "address": "123 Tech Avenue"
    }
  },
  "projects": [
    {
      "name": "AI Development",
      "deadline": "2024-12-31",
      "team": ["Alice", "Charlie"]
    },
    {
      "name": "Cloud Infrastructure",
      "deadline": "2024-09-30",
      "team": ["Bob"]
    }
  ]
}
print(comp["projects"][0]["deadline"])
print(comp["company"]["employees"][2]["salary"])

print(comp["projects"][1]["name"],(comp["projects"][1]["team"]))

print(comp["company"]['employees'][2]['name'])
