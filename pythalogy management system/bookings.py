bookings = []
def book_test(patient, test):
    booking = {
        "id": len(bookings) + 1,
        "patient_name": patient["name"],
        "patient_id": patient["id"],
        "test_name": test["name"],
        "price": test["price"],
        "status": "Sample Pending",
        "result": None
    }
    bookings.append(booking)
    print(f"Test booked! Booking ID: {booking['id']} for {patient['name']} - {test['name']}\n")
def list_bookings():
    if not bookings:
        print("No bookings yet.\n")
        return
    print("\n--- All Bookings ---")
    for b in bookings:
        print(f"{b['id']}. {b['patient_name']} | {b['test_name']} | Status: {b['status']}")
    print()
def find_booking(booking_id):
    for b in bookings:
        if b["id"] == booking_id:
            return b
    return None
def collect_sample(booking_id):
    booking = find_booking(booking_id)
    if not booking:
        print("Booking not found.\n")
        return
    if booking["status"] != "Sample Pending":
        print(f"Sample already {booking['status'].lower()}.\n")
        return
    booking["status"] = "Sample Collected"
    print(f"Sample collected for booking {booking_id}.\n")
def generate_report(booking_id, result):
    booking = find_booking(booking_id)
    if not booking:
        print("Booking not found.\n")
        return
    if booking["status"] != "Sample Collected":
        print("Sample must be collected first.\n")
        return
    booking["result"] = result
    booking["status"] = "Report Ready"
    print(f"Report generated for booking {booking_id}.\n")
def view_report(booking_id):
    booking = find_booking(booking_id)
    if not booking:
        print("Booking not found.\n")
        return
    if booking["status"] != "Report Ready":
        print(f"Report not ready. Current status: {booking['status']}\n")
        return
    print("\nTest Report")
    print(f"Patient:{booking['patient_name']}")
    print(f"Test: {booking['test_name']}")
    print(f"Result: {booking['result']}")
    print()
 