from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "hashed_password": get_password_hash("secret"),
        "role": "user",
    }
}
