

# Nested: Ekta Dictionary-Er, Vhitor Erekta Dictionary...

student ={"Name": "Ahamad Ullah",
         "Subject":{"Physics":90,
         "Biology":80,               
         "Math":70,
         "ICT": 90}
         }


print(student.get("Subject")) 
print("\nBiology Marks:",student["Subject"]["Biology"])