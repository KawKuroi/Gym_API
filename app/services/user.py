from app.schemas.user import User
import bcrypt

class UserService:

    @staticmethod
    def _to_byte(text:str) -> bytes:
        return text.encode("utf-8")

    def check_user(self, password_hashed: str, password: str):
        return bcrypt.checkpw(self._to_byte(password), self._to_byte(password_hashed))


if __name__ == '__main__':
    user = User(username="Axel", email="kevina@a.com", password="1231asdASD!A")
    print(UserService().check_user(user.password, "1231asdASD!A"))
