from lib.music_list import *

"""
When add music to the list 
"""
def test_add_track_to_the_list():
    music_list = MusicList()
    music_list.add_track ("We will Rock You")
    assert music_list.tracks == ["We will Rock You"]


"""
When add multiple music to the list
"""
def test_add_multiply_track_to_the_list():
    music_list = MusicList()
    music_list.add_track("We will Rock You")
    music_list.add_track("Kiss Kiss")
    music_list.add_track("Hit me baby one more time")
    assert music_list.tracks == ["We will Rock You", "Kiss Kiss", "Hit me baby one more time"]
