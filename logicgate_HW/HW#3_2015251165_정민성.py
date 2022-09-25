# 2015251165 정민성

print("4bit 데이터, 7bit 수신된 데이터를 기준으로 진행합니다.")
data_bit, input_data = input("\"데이터 비트, 수신된 데이터\" 양식에 맞춰서 입력해주세요.\n").split(", ")

while len(data_bit) != 4:
    print(f"데이터비트의 자릿수가 {len(data_bit)}로 보입니다. 다시 입력하세요.")
    data_bit = input("데이터 비트를 다시 입력해주세요.")

while len(input_data) != 7:
    print(f"수신된 데이터의 자릿수가 {len(input_data)}로 보입니다. 다시 입력하세요.")
    input_data = input("수신된 데이터를 다시 입력해주세요.")


print(f"입력하신 데이터비트는 {data_bit}, 수신된 데이터는 {input_data}")

p1, p2, p4, s1, s2, s4 = -1, -1, -1, -1, -1, -1

# 리스트는 0123 순서, 숫자는 7653 순서이니
p1 = (int(data_bit[3]) + int(data_bit[2]) + int(data_bit[0])) % 2
p2 = (int(data_bit[3]) + int(data_bit[1]) + int(data_bit[0])) % 2
p4 = (int(data_bit[2]) + int(data_bit[1]) + int(data_bit[0])) % 2
haming_code = str(f"{data_bit[0]}{data_bit[1]}{data_bit[2]}{p4}{data_bit[3]}{p2}{p1}")
print(f"해밍코드는 {haming_code}")

# 신드롬 7654321 s1=1357 s2=2367 s4=4567
# 역순인 0123456 S1=6420 s2=5410 s4=3210

s1 = (int(input_data[6]) + int(input_data[4]) + int(input_data[2]) + int(input_data[0])) % 2
s2 = (int(input_data[5]) + int(input_data[4]) + int(input_data[1]) + int(input_data[0])) % 2
s4 = (int(input_data[3]) + int(input_data[2]) + int(input_data[1]) + int(input_data[0])) % 2
syndrom = str(f"{s4}{s2}{s1}")
print(f"신드롬 단어는 {syndrom}")