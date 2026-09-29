patients = []
def add_patients():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter gender male/female: ")
    contact = input("Enter contact number: ")
    patient = {
        "id": len(patients) + 1,
        "name": name,
        "age": age,
        "gender": gender,
        "contact": contact
    }
    patients.append(patient)
    print("Patient registered:\n")
def list_patients():
    if not patients:
        print("No patients registered found\n")
    else:
        print("\nRegistered Patients")
    for p in patients:
        print(f"{p['id']}. {p['name']}  Age: {p['age']}  Gender: {p['gender']}  Contact: {p['contact']}")
    print()
def find_patient(patient_id):
    for p in patients:
        if p["id"] == patient_id:
            print("found")
        else:
            print("not found")