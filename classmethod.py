class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)
    
    @classmethod
    def number_of_users(cls):
        print("총 유저 수는 : {} 입니다".format(cls.count))

user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")
user3 = User("서혜린", "lisa@codeit.kr", "123abc")

User.number_of_users()
user1.number_of_users()