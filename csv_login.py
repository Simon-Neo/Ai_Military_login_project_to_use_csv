import csv


s_csv_address = './info.csv'

list_field_names = ['id', 'password']

def user_input():
    try:
        id, pw = map(str, input("아이디와 비밀번호를 차례로 입력해주세요 : ").split())
        return id, pw
    except:
        print("올바르지 않은 입력입니다!")
        id, pw = user_input()
        return id, pw

def is_in_id(id):
    with open(s_csv_address, 'r') as csv_file:
        dic_reader = csv.DictReader(csv_file)

        for dic_row in dic_reader:
            print(dic_row['id'])
            if dic_row['id'] == id:
                return True

        return False

def is_ok_checing_password(id, password):
    with open(s_csv_address, 'r') as csv_file:
        dic_reader = csv.DictReader(csv_file)

        for dic_row in dic_reader:
            if dic_row['id'] == id:
                if dic_row['password'] == password:
                    return True

    return False



def signin(id, pw):
    # TODO_1 : signin 함수를 구현해서 로그인 시키기
    # 1. csv 파일에서 존재하는 아이디인지 확인하기
    # 2. 존재하면 비밀번호 맞는지 체크
    # 3. 비밀번호도 맞으면 로그인성공 출력하기
    if False == is_in_id(id):
        print('I do not have your id. Login fail.. -_-')
        return False

    if False == is_ok_checing_password(id, pw):
        print('it is wrong password ! Sorry.!!')
        return False

    print('Login is successful! Thank you!^^')
    return True

def signup():
    # TODO_2 : csvfile 에 유저가 존재하는지 확인하는 함수 구현해서 호출하기
    # 1. 아이디를 기준으로 존재하는 유저인지 확인
    # 2. 존재한다면 다시 아이디를 입력받고,
    # 3. 존재하지 않는다면 다음 단계로 넘겨주기
    while(1):
        id, pw = user_input()

        if True == is_in_id(id):
            print('your input id is exist Sorry Try Again!! -_-')
            continue

        break
    print('sign up is successful!! Thank you!')

    return id, pw


def append_csv_data(list_dict_user):
    # TODO_3 : csvfile 에 등록되어있는 형태로 유저 등록하는 함수 구현하기
    # 1. 아이디와 비밀번호를 그냥 데이터로 받아서 추가해보기
    # 2. 아이디와 비밀번호를 '딕셔너리' 형태로 받아서 추가해보기 (프로그래밍 실력의 기본은 구글링! 최대한 구글링 해보세요!!)

    with open(s_csv_address, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=list_field_names)
        for data in list_dict_user:
            writer.writerow(data)

def userlist():
    print("현재 존재하는 유저 :")

    # TODO_4 : csvfile 에서 현재 가입되어 있는 유저 전부 출력하기
    with open(s_csv_address, 'r') as csv_file:
        readCsv = csv.reader(csv_file)
        for i, row in enumerate(readCsv):
            for column in row:
                print(f'{column}\t\t\t',end='')
            print()
            if i == 0:
                print('-----------------------------------')


def exitcheck():
    stop = int(input("\n계속하시려면 0, 종료하시려면 1을 눌러주세요. : "))
    if stop == 0:
        start()
    elif stop == 1:
        exit()

def create_init_csv_file():
    with open(s_csv_address, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(list_field_names)

def start():
    # create_init_csv_file && make filed row
    #create_init_csv_file()

    print('csv 로 데이터 다루기 로그인 예제')

    signup_or_login = int(input('1 - 로그인 / 2 - 회원가입 : \n'))

    if signup_or_login == 1:
        id, pw = user_input()

        signin(id, pw) # TODO_5 : 위의 TODO1 참고 후 signin 함수 실행하기
        userlist()
    elif signup_or_login == 2:
      # TODO_6 : 회원가입을 아이디와 비밀번호만 받아서 진행할 것
      # 1. 존재하는지 확인 (위의 TODO_2의 함수 활용)
      # 2. 문제 없으면 회원가입 완료 후 userlist() 함수 구현
        id, pw = signup()

        dict_user = {
            "id": id,
            "password": pw
        }
        append_csv_data([dict_user])
        # signup(id, pw)
        # signup(dict_user)
        userlist()
    else:
        print("올바른 숫자를 입력하세요!")

    exitcheck()
    return

start()

# TODO_7 : 깃헙에 업로드하고 깃헙 주소 제출!
