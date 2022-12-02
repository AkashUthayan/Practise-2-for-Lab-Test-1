import main as num

def test_find_min_max():
    testarr=[1,2,3]
    testarr2=[1,3]
    result = num.find_min_max(testarr)
    assert(testarr2 == result)

def test_find_average():
    testarr = [1, 2, 3]
    correctavg = 2
    result = num.find_average(testarr)
    assert ( correctavg == result)
if __name__ == "__main__":
    test_find_min_max()
    test_find_average()