class User:
    def say_hello(some_user):
        print("안녕하세요! 저는 {}입니다!".format(some_user.name))

        
    def login(some_user, my_email, my_password):
        if(some_user.email == my_email and some_user.password == my_password): 
            print("로그인 성공, 환영합니다")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

user1 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user1.login("captain@codeit.kr", "12345")
