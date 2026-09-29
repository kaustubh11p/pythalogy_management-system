import patients
import tests_catalog
import bookings
import billings
def main():
    while True:
        print("Pathology Lab Management System")
        print("1.Register Patient")
        print("2.List of Patients")
        print("3.View Test Catalog")
        print("4.Book a Test")
        print("5.Collect Sample")
        print("6.Generate a report")
        print("7.View a Report")
        print("8.View all the bookings")
        print("9.Generate a Bill")
        print("10.Exist")
        choice = input("choose an option(1-10):")
        if choice=="1":
            patients.add_patients()
        elif choice=="2":
            patients.list_patients()
        elif choice=="3":
            tests_catalog.list_tests()
        elif choice=="4":
            patient_id=int(input("Enter patient ID:"))
            test_id=int(input("Enter test ID"))
            patient=patients.find_patient(patient_id)
            test = tests_catalog.find_test(test_id)
            if patient is None:
                print("Patient not found.\n")
            elif test is None:
                print("Test not found.\n")
            else:
                bookings.book_test(patient, test)
        elif choice == "5":
            booking_id = int(input("Enter booking ID: "))
            bookings.collect_sample(booking_id)
        elif choice == "6":
            booking_id = int(input("Enter booking ID: "))
            result = input("Enter test result in positive and negative: ")
            bookings.generate_report(booking_id, result)
        elif choice == "7":
            booking_id = int(input("Enter booking ID: "))
            bookings.view_report(booking_id)
        elif choice == "8":
            bookings.list_bookings()
        elif choice == "9":
            patient_id = int(input("Enter patient ID: "))
            billings.generate_bill(patient_id,bookings)
        elif choice == "10":
            print("Exiting program. Goodbye!")
            print("Invalid choice. Try again.\n")
 
 
if __name__ == "__main__":
    main()
 