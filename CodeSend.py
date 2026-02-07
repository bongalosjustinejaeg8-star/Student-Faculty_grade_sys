import json

s = {"student_1": "password_1"}
f = {"faculty_1": "fpassword_1"}
with open ("ProfCred.json","w") as f:
    json.dump(s,f)