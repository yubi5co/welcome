# 함수 def (박스)
def openaccount():
    print('새로운 계좌가 생성되었습니다.')

openaccount()

# 전달값과 반환값
def deopsit(balance,money):   #입금
    print('입금이 완료되었습니다. 잔액은 {0}원 입니다.'.format(balance+money))
    return balance+money

def withdraw(balance,money): #출금
    if balance >= money: # 잔액이 출금보다 많으면
        print('출금이 완료되었습니다. 잔액은 {0}원입니다.'.format(balance-money))
        return balance-money
    else:
        print('출금이 완료되지 않았습니다. 잔액은 {0}원입니다.' .format(balance))
        return balance
def withdrawnight(balance,money): # 저녘에 출금 (수수료 추가) 
    commission = 100 # 수수료 100원
    return commission,balance - money - commission

balance = 0 # 잔액
balance = deopsit(balance,1000)
#balance = withdraw(balance,500)
commission, balance = withdrawnight(balance,500)
print('수수료 {0}원이며, 잔액은 {1}원 입니다.' .format(commission, balance))

