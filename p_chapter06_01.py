#Chapter06-01
#병행성(Concurrency)
#이터레이터, 제너레이터
#Iterator, Generator (제너레이터를 통해서 이터레이터를 받음)

#파이선 반복 가능한 타입 (or문, while)
#collections, text file, list, Dict, Set, Tuple, unpacking, *args ...... :iterable

#반복 가능한 이유? -> iter(x) 함수 호출
t = 'ABCDEFGHIJKLMNOPQRXTUVWXYZ'

for c in t:
    pass
    #print(c)

#while
w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break
print()

#반복형 확인

from collections import abc
print(dir(t))
print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable)) #t가 abc 클래스의 iterable을 상속받았는지

print()
print()


#next 패턴
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

w1 = WordSplitter('Do today what you could do tomorrow')

print(w1)
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))
print(next(w1))

print()
print()
#Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Corotine) 구현과 연동
# 3. 작은 메모리 조각 사

class WorldSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word #제네레이터 #다음에 반환될 값의 위치를 안다.
        return

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wg =  WorldSplitGenerator('Do today what you could do tomorrow')
print(wg)
wt = iter(wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

print()
print()
