class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User("Young", "young@codeit.kr", "123456")

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user4 = User("Lisa", "lisa@codeit.kr", "abc123")

print(user1.email)
print(user2.name)
print(user3.password)
print(user4.email)
