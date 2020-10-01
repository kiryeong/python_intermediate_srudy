#Chapter 02-03
#객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
#규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
#클래스 중심 -> 데이터 중심 -> 객체로 관리

#class Car(object):와 같은 거임 object를 상속받은 것
class Car():
    """
    Car class
    Author : Nam
    Date : 2020.09.28
    Description : Class, Static, instance Method
    """

    #클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company #_가 있는 변수는 instance변수고, _가 없는 것은 모두가 공유하는 클래스 변수구나 암묵적 룰
        self._details = details


    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    #Instance method
    #Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    #Instance method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
    #Instance method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    #Class method
    @classmethod
    #cls는 Car class를 말하는 것임
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Suceed! price incresed.')

    #Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw'
#self가 붙어있는게 instance 변수
#self를 인자로 받는 것은 instance method

#Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower' : 270, 'price' : 5000})
'''
#전체정보
car1.detail_info()
car2.detail_info()

#가격정보(직접 접근 (좋지 않은 방법))
print(car1._details.get('price'))
print(car2._details['price'])

#가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())
#가격 인상(클래스 메소드 미사용) (직접 접근해서 이렇게 수정하는 거는 보기좋지 않다.)
Car.price_per_raise = 1.4

#가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

#클래스 변수를 핸들링 할 때는 클래스 메소드를 활용하는 것을 권장한다.
#가격 인상(클래스 메소드 사용)
Car.raise_price(1.8)
#가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

#인스턴스 호출(스테이틱)
print(car1.is_bmw(car1))
print(car1.is_bmw(car2))
#클래스로 호출(스테이틱)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
'''

car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower' : 270, 'price' : 5000})
print(car1)
