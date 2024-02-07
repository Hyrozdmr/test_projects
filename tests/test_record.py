from lib.record import Record

def tests_left_front_format(): 
    recorder = Record("left", "front", "19/04/1997", "2", "6")
    res = recorder.format()
    assert res == {"position": "left, front", "date": "19/04/1997", "tyre tread": "2", "tyre depth": "6"}

def tests_back_right_format(): 
    recorder = Record("back", "right", "19/07/1981", "3", "8")
    res = recorder.format()
    assert res == {"position": "back, right", "date": "19/07/1981", "tyre tread": "3", "tyre depth": "8"}
