def test():
    assert list(map(len, "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".replace('.','').replace(',','').split(" "))) == [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]
