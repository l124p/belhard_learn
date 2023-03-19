from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(schemes=['bcrypt'], deprecated='auto')
SECRET_KEY = 'asdsaed32432543665876uhfgbvdsafsdfsfdsfds-f=-=-4324324'
EXPIRE_JWT_TOKEN = 20
TOKEN_TYPE = 'Bearer'
ALGORITHM = 'HS256'
