import main as num

def test_find_min_max():
    testarr=[1,2,3]
    testarr2=[1,3]
    result = num.find_min_max(testarr)
    assert(testarr2 == result)

if __name__ == "__main__":
    test_find_min_max()