from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from . import schemas  # Import your schemas if necessary

# Secret key for JWT encoding/decoding
SECRET_KEY = "a_long_random_string"  # Change this to a secret key in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password context for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash a password
def get_password_hash(password: str):
    return pwd_context.hash(password)

# Function to verify if the entered password matches the hashed one
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Function to create an access token (JWT)
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta  # Set the expiration time for the token
    to_encode.update({"exp": expire})  # Add the expiration field to the data
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Encode the data into a JWT token
    return encoded_jwt

# Function to decode a JWT and extract its payload
def decode_access_token(token: str):
    try:
        # Decode the JWT token and return the payload
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        # Return None if the token is invalid or expired
        return None
