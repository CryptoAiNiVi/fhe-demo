print("🔒 Hello FHE World (demo)")

class EncryptedValue:
    def __init__(self, value):
        self.value = value  # encrypted placeholder

    def __add__(self, other):
        return EncryptedValue(self.value + other.value)

a = EncryptedValue(5)
b = EncryptedValue(3)
c = a + b

print(f"Decrypted result: {c.value}")
