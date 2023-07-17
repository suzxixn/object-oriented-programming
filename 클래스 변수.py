class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")
user3 = User("서혜린", "lisa@codeit.kr", "123abc")

print(User.count)

