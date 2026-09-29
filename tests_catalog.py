tests = [
    {"id": 1, "name": "Complete Blood Count (CBC)", "price": 300},
    {"id": 2, "name": "Blood Sugar (Fasting)", "price": 150},
    {"id": 3, "name": "Lipid Profile", "price": 600},
    {"id": 4, "name": "Liver Function Test (LFT)", "price": 700},
    {"id": 5, "name": "Kidney Function Test (KFT)", "price": 650},
    {"id": 6, "name": "Thyroid Profile (T3 T4 TSH)", "price": 500}]
def list_tests():
    for t in tests:
        print(f"{t['id']}. {t['name']} - Rs.{t['price']}")
    print()
def find_test(test_id):
    for t in tests:
        if t["id"] == test_id:
            return t
    return None