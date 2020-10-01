#Chapter04-02
#시퀀스형
#컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
#플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
#가변(list, bytearray, array.array, memoryview, deque)
#불변(tuple, str, bytes)
#리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

#b,a = a,b
#divmod는 몫과 나머지를 반환 해 주는 함수
a = divmod(100, 9)
print(type(a))
print(divmod(100, 9))
print(divmod(*(100, 9))) # *로 unpacking을 해줘야함
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1,2,3,4,5 #그냥 선언하면 tuple임
print(x, y, rest)

print()
print()


#Mutable(가변) vs Immutable(불변)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

print(l, id(l))
print(m, id(m))
#변동이 심한 거는 list에 넣어놓고 시도를 여러개 해보는게 좋음 안그러면 id가 계속 재할당이 이루어짐(tuple)

print()
print()

# sort vs sorted
# reverse, key = len, key=str.lower, key=func...

#sorted : 정렬 후 새로운 객체 반환 (원본이 수정 안된다)
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse = True))
print('sorted - ', sorted(f_list, key=len))
print('sorted - ', sorted(f_list, key=lambda x: x[-1]))
print('sorted - ', sorted(f_list, key=lambda x: x[-1], reverse=True))

print('sorted - ',f_list)
print()
print()
#sort : 정렬 후 객체 직접 변경 (원본이 수정된다)
print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse = True), f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('sort - ', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort - ', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

print('sorted - ',f_list)

#list vs Array 적합한 사용법 설명
#리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
#숫자 기반 : 배열(리스트와 거의 호환)
