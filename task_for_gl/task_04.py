import crypt

ADMIN_USER = "vasja.pupkin"
ADMIN_PASSWORD = "passsecret"
hash_cred = crypt.crypt(ADMIN_PASSWORD, ADMIN_USER)


def get_user():
    return ADMIN_USER


def get_password():
    return hash_cred


def valid_admin_user(username, password):
    return username.lower() == get_user() and crypt.crypt(password, hash_cred) == get_password()
