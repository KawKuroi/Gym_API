from pydantic import BaseModel, Field, EmailStr, field_validator
import bcrypt
import re


class User(BaseModel):
    username: str = Field(min_length=1, max_length=30)
    email: EmailStr
    password: str

    @field_validator('password')
    def validate_and_hash_password(cls, v):
        pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&.,;:_\-])[A-Za-z\d@$!%*?&.,;:_\-]{8,}$'
        if not re.match(pattern, v):
            raise ValueError(
                "La contraseña debe tener al menos una mayúscula, un número y un carácter especial, "
                "y tener mínimo 8 caracteres.")

        hashed = bcrypt.hashpw(v.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')


if __name__ == '__main__':
    user = User(username="Axel", email="kevina@a.com", password="1231asdASD!A")
    print(user)


