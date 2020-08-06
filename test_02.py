def concat_alternately(s1, s2):
    concatnated_str = ''
    for c1, c2 in zip(s1, s2):
        concatnated_str += (c1 + c2)
    return concatnated_str

def test():
    assert "パタトクカシーー" == concat_alternately("パトカー", "タクシー")
