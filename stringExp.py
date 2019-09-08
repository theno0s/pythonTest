# 문자열 사용방법

print("큰따옴표 :: Hello workd")
print('작은따옴표 :: python is fun')
print("""큰따옴표 3개 :: Life is too short, You need python""")
print('''작은따옴표 3개 :: Life is too short, You need python''')

# 문자열 안에 따옴표 포함 시키기

print('python\'s favorite food is perl')
print("python's favorite food is perl")
print('"python is very easy." he says.')

# 여러줄 문자열 변수 대입

multiline = "Life is too short\nYou need python"
print(multiline)

multiline2 = '''Life is too short
You need python'''
print(multiline2)

multiline3 = """Life is too short
You need python"""
print(multiline3)

print('\a')
print('\000')

# 문자열 연산하기

head = "python"
tail = " is fun!"
print(head + tail)

string1 = "python"
print(string1 * 2)

print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 인덱싱, 0부터 인덱싱/ -는 오른쪽 부터 카운트

a = "Life is too short, You need Python"
print(a[3])
print(a[-2])

