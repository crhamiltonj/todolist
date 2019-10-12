import secrets

class Config(object):

    SQLALCHEMY_DATABASE_URI = "sqlite:///test.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG=True
    SECRET_KEY='dsjflsdjkflakjf;lkdjfjkl'
    TESTING=True
    JWT_SECRET_KEY='QRpzr07ils9gkYmIHciPcbdYFu0JUeU_I8K1ld635nJXuPOapUwMAzSCKl79p6BMjaJN9xhqcIXHOlbVQKQdLA'
    SECURITY_PASSWORD_SALT='LEnMyXMPkUyzFcqc8_-U0tcAd20kBjy5OSmNZrLhJvLLxjdThcW9YhN_0k2wMV-Ehcjmtv6Ie4Qq4x6wfzMWxA'
