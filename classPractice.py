# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성 되었습니다.".format(self.name))

    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

print('\n----------------------------\n')

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16, 3)
firebat1.attack("5 시")

firebat1.damaged(25)
firebat1.damaged(25)


# 날 수 있는 기능
class Flyable:
    def __init__(self, flying_speed):
        print("공중 기능 추가. 이동 속도 : {}".format(flying_speed))
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
    
    # overiding
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "5시")


vulture = AttackUnit("벌처", 80, 10, 20)

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("1시")


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # pass # 넘어감
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # self 사용하지 않음.

buildingUnit = BuildingUnit("서플라이 디폿", 500, "7시")


class MultipleExtends(Unit, Flyable):
    def __init__(self):
        # super().__init__("test1", 1, 1) # 상속 순서에 영향을 받음
        # 다중 상속된 부모 클래스 생성자 사용을 위해선 직접 호출해야함
        Unit.__init__(self, "test1", 1, 1)
        Flyable.__init__(self, 2)


multi = MultipleExtends()