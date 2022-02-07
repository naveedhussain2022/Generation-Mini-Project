def twonum(a,b):
    try:
        return a+b
    except NameError:
        print("Only numbers")

def testaddnum():
    #arrange or assmeble
    a=7
    b=12
    expected = 19

    #act
    result = twonum(a,b)

    #assert checks expected with the result
    assert result == expected

def testaddnum1():
    #arrange or assmeble
    a=7
    b=-3
    expected = 4

    #act
    result = twonum(a,b)

    #assert checks expected with the result
    assert result == expected

def testaddnum2():
    #arrange or assmeble
    a=3.1
    b=3.1
    expected = 6.2

    #act
    result = twonum(a,b)

    #assert checks expected with the result
    assert result == expected

def testaddnum3():
    #arrange or assmeble
    a=3
    b=nav
    expected = 4

    #act
    result = twonum(a,b)

    #assert checks expected with the result
    assert result == expected

testaddnum()
testaddnum1()
testaddnum2()
testaddnum3()