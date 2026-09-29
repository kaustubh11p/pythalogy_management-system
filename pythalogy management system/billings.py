def generate_bill(patient_id, bookings):
    patient_bookings = [b for b in bookings if b["patient_id"] == patient_id]
    if not patient_bookings:
        print("it is not booked for test.\n")
        return
    print("\n Bill")
    count = 0
    for b in patient_bookings:
        print("{b['test_name']} - Rs.{b['price']}")
        count = count + b["price"]

    print(f"Total: Rs.{count}\n")
    return count