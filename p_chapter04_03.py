#Chapter04-03
#시퀀스형
#컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
#플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
#가변(list, bytearray, array.array, memoryview, deque)
#불변(tuple, str, bytes)
# 해시테이블
# Key에 Value를 저장하는 구조
# 파이썬에서는 dictionary type이 해쉬 테이블의 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key값을 해싱 함수를 통해서 해쉬 주소 값이 나오고, 이걸 기반으로 key에 대한 value의 위치를 알고 참조할 수 있음


# Dict 구조
#print(__builtins__.__dict__)

# Hash 값 확인

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50]) #list는 값을 수정할 수 있기때문에 고유하지 않아서 hash를 사용할 수 없다.

print(hash(t1))
# print(hash(t2)) # 예외

print()
print()

#tuple에서 dictionary 만들기
# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

#No use Setdefqult
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

#Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print(new_dict2)

#주의
new_dict3  = {k: v for k, v in source}

print(new_dict3)

print()
print()