print("🔒 Hello FHE World (demo with user input)")

class EncryptedValue:
    def __init__(self, value):
        self.value = value  # placeholder for encrypted data

    def __add__(self, other):
        return EncryptedValue(self.value + other.value)

x = int(input("Enter first number to encrypt: "))
y = int(input("Enter second number to encrypt: "))

a = EncryptedValue(x)
b = EncryptedValue(y)

c = a + b

print(f"Decrypted result: {c.value}")

12
