from lib.car import Car 
from lib.record import Record 

def test_empty_lists():
    car = Car() 
    res = car.front + car.back 
    assert res == []

def test_add_to_list(): 
    car = Car() 
    record = Record("left", "front", "19/04/1997", "2", "6")
    res = record.format()
    car.add(res)
    assert car.front == [{"position": "left, front", "date": "19/04/1997", "tyre tread": "2", "tyre depth": "6"}]

def test_add_two_to_list(): 
    car = Car() 
    position1 = Record("left", "front", "19/04/1997", "2", "6")
    position2 = Record("back", "right", "19/07/1981", "3", "8")
    position1 = position1.format()
    position2 = position2.format()
    car.add(position1)
    car.add(position2)
    assert car.back + car.front == [{"position": "back, right", "date": "19/07/1981", "tyre tread": "3", "tyre depth": "8"}, {"position": "left, front", "date": "19/04/1997", "tyre tread": "2", "tyre depth": "6"}]  