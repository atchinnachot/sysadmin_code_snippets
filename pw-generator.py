import secrets
import string

alphabet = (
    string.ascii_lowercase
    + string.ascii_uppercase
    + string.digits
    + string.digits
    + string.digits
)
password = "".join(secrets.choice(alphabet) for i in range(10))

print(alphabet)
print(password)
