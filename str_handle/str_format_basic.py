'''
* 문자열 포맷팅

- 포맷팅은 문자열 사이사이에 다른 타입의 데이터를 넣어서
문자열을 조립하는 방식입니다.
'''
apple = 3
print('사과가 ', apple, '개 있습니다.', sep='')
print('사과가 %d개 있습니다.' % apple)

'''
여러 개의 데이터도 하나의 문자열에 포맷팅 할 수 있는데,
이 때는 % 연산자 뒤에 나열한 변수를 ()로 묶어 줍니다.
'''
month = 12
day = 25
anni = '크리스마스'
print('%d월 %d일은 %s입니다.' % (month, day, anni))


'''
* format 함수를 사용한 형식 지정 포맷팅

- 문자열의 format 함수를 사용하면 서식 문자를 지정하는 것보다
좀 더 유용하고 편하게 문자열 포맷팅을 할 수 있습니다.
'''
print('{}월 {}일은 {}입니다.'.format(month, day, anni))

# 소수점 표현
pi = 3.141592
print('원주율은 {:0.3f}입니다.'.format(pi))

# f 문자열 포맷팅
# 파이썬 3.6버전 이후로 사용할 수 있는 기능입니다.
# 접두어 f를 문자열 앞에 붙여서 사용합니다.
print(f'{month}월 {day}일은 {anni}입니다.')

# {} 안에서는수식도 사용이 가능합니다.
salary = 300
print(f'보너스를 합한 월급: {salary + 100}')

print(f'원주율은 {pi:0.2f} 입니다.')