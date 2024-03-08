from exos.exo13 import filter_students
def test_filter_students():
    assert filter_students({'Alice': 17, 'Bob': 12, 'Charlie': 15, 'David': 19}) == {'Alice': 17, 'Charlie': 15, 'David': 19}
    assert filter_students({'Alice': 12, 'Bob': 12, 'Charlie': 12, 'David': 12}) == {}
    assert filter_students({'Alice': 20, 'Bob': 20, 'Charlie': 20, 'David': 20}) == {'Alice': 20, 'Bob': 20, 'Charlie': 20, 'David': 20}
    assert filter_students({'Alice': 15, 'Bob': 15, 'Charlie': 15, 'David': 15}) == {'Alice': 15, 'Bob': 15, 'Charlie': 15, 'David': 15}