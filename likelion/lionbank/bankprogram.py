# bank DB 대용 list를 활용하여 등록된 계좌 정보를 저장.
bank = list()

# managercode를 두어 매니저 모드 접속하여 전체 조회가 가능하게 함.
managercode = int(2016125069)

# 사용자가 입력한 작업수행 번호
select = 0

# menu 
def bankmenu():
    print("========Bank Menu=========")
    number = int(input("""1. 계좌개설
2. 입금하기
3. 출금하기
4. 계좌조회
5. 관리자 Mode
6. 종료하기
===========================
"""))
    return number


# manager인지 확인 하는 함수
def checkManager():
    while 1:
        managernum = int(input("매니져 번호를입력하세요(0 입력시 종료) : "))
        if managernum == 0:
            print("매니저 모드를 종료합니다.")
            break
        elif managernum == managercode :
            show_all_account() # 매니저 모드에서 사용 가능한 기능 : 모든 계좌 조회
            break
        elif managernum != managercode and managernum != 0:
            print("매니저 번호를 다시 입력하세요.")
            continue
    return 0


# 계좌와 계좌 비밀번호를 check 하는 함수
def checking_Account():
    listcount = 0
    check = 0
    while check != 1:
        accountnum = int(input("계좌번호를 입력해주세요 : "))
        for i in bank :
            if accountnum == i.accountNumber:
                pwd = int(input("계좌비밀번호를 입력해주세요 : "))
                if pwd == i.password:
                    check = 1
                    break
                else :
                    print("비밀번호를 잘못 입력하셨습니다. 다시 입력해 주세요.")
                    continue
            listcount += 1
        if check == 0:
            print("잘못 입력하셨습니다. 다시 입력해 주세요.")
            continue   
    return listcount


# 모든 계좌 조회 함수
def show_all_account():
    ok = int(input("""전체계좌를 조회하시겠습니까? 
1. 네 2. 아니요
"""))
    if ok == 1 :
        for i in bank:
            print (i.name, "님의 계좌 잔액 : ", i.money)
    elif ok == 2 :
        print("매니저 모드를 종료하겠습니다.")
    return 0

# 계좌 class
class Account:
    accountNumber = ""
    name= ""
    money = ""
    def __init__(self,accountNumber,name,password,moeny):
        self.accountNumber = accountNumber
        self.password = password
        self.name = name
        self.money = moeny
# 잔액 조회    
    def showaccount(self):
        print("잔액 : ", self.money)

# 적금 계좌
class Saving_Account(Account):
    def __init__(self,accountNumber,name,password,moeny):
        self.accountNumber = accountNumber
        self.password = password
        self.name = name
        self.money = moeny
    # 출금이 불가능함.
    def cantAccess(self):
        print("적금기간 내에 해지할 수 없습니다!")

# 예금 계좌
class Deposit_Account(Account):
    def __init__(self,accountNumber,name,password,moeny):
        self.accountNumber = accountNumber
        self.password = password
        self.name = name
        self.money = moeny
    # 출금
    def withdraw(self, wm):
        if self.money < wm:
            print("잔고가 부족해서 출금 할 수 없습니다!")
        else : 
            self.money = self.money - wm
            print("출금이 완료 되었습니다.")
    # 입금
    def deposit(self, dm):
        self.money = self.money + dm
        print("입금이 완료 되었습니다.")

# ATM 실행.
while select != 6 :
    select = bankmenu()
    if select>6 or select<1:
        print("올바른 숫자를 입력해주세요")
        continue
    # 계좌 개설
    elif select == 1 :
        print("========계좌개설========")
        select_account = int(input("""1. 예금계좌  2. 적금계좌
=========================
"""))
        a = int(input("계좌번호(숫자 8자리) :"))
        name = input("이름 : ")
        password = int(input("password(숫자 4자리) : "))
        money = int(input("입급할 금액 : "))
        if select_account == 1 :    
            bank.append(Deposit_Account(a,name,password,money))
        elif select_account == 2 :
            bank.append(Saving_Account(a,name,password,money))
        continue
        end = input("확인을 완료하셨으면 \"enter\"를 눌러주세요.")
    # 입금
    elif select == 2 :
        listnum = checking_Account()
        if type(bank[listnum]) is Deposit_Account :
            print(bank[listnum].name + " 님의 계좌입니다.")
            dm = int(input("입금할 금액을 입력해 주세요: "))
            bank[listnum].deposit(dm)
            bank[listnum].showaccount()
        elif type(bank[listnum]) is Saving_Account :
            print(bank[listnum].name + " 님의 계좌입니다.")
            bank[listnum].cantAccess()
            bank[listnum].showaccount()
        end = input("확인을 완료하셨으면 \"enter\"를 눌러주세요.")
    # 출금
    elif select == 3 :
        listnum = checking_Account()
        if type(bank[listnum]) is Deposit_Account :
            print(bank[listnum].name + "님의 계좌입니다.")
            wm = int(input("출금할 금액을 입력해 주세요 : "))
            bank[listnum].withdraw(wm)
            bank[listnum].showaccount()
        elif type(bank[listnum]) is Saving_Account:
            print(bank[listnum].name + "님의 계좌입니다.")
            bank[listnum].cantAccess()
            bank[listnum].showaccount()
        end = input("확인을 완료하셨으면 \"enter\"를 눌러주세요.")
    # 계좌 조회
    elif select == 4 : 
        listnum = checking_Account()
        print(bank[listnum].name + "님의 계좌입니다.")
        bank[listnum].showaccount()
        end = input("확인을 완료하셨으면 \"enter\"를 눌러주세요.")
    # 매니저 모드
    elif select == 5 :
        checkManager()
        end = input("확인을 완료하셨으면 \"enter\"를 눌러주세요.")

