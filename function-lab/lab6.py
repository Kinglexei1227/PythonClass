def wrap_in_tag(x, y):
    return f"<{x}>{y}</{x}>"

print(wrap_in_tag('p','hello')) # 출력: <p>hello</p>
print(wrap_in_tag('b','world')) # 출력: <b>world</b>