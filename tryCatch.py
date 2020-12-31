
class CustomException(Exception):
    def __init__(self, msg):
        print(msg)


def divide(a, b):
    if b == 0:
        raise CustomException("분모가 0보다 작을 수 없습니다.")

    return a/b

print(divide(1,1))