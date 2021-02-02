import re

p = re.compile("ca.e")
# . : 하나의 문자를 의미.(어떤 것도 올 수 있음) - care, cafe (O) | caffe (X)
# ^ : 문자열의 시작 ex. ^de - desk, destination (O)| fade (X)
# $ : 문자열의 끝 ex. se$ - case, base (O)| face (X)

def print_match(m):
    if m:
        print("m.group(): ", m.group())  # 일치하는 문자열 반환
        print("m.string: ", m.string)   # 입력받은 문자열 반환
        print("m.start(): ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end(): ", m.end())  # 일치하는 문자열의 끝 index
        print("m.span(): ", m.span())  # 일치하는 문자열의 시작, 끝 index
    else:
        print("매치되지 않음")

# m = p.match("careless")
# print_match(m)

# m = p.search("good care")
# print_match(m)

lst = p.findall("careless")
print(lst)