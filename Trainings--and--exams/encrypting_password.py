import re

number = int(input())
pattern = r"(?<![\!\@\#\$\%\^\&\*\(\)\,\.\?\"\:\{\}\||[A-Za-z0-9])([!@#$%^&*(),.?\":{}|[A-Za-z0-9]+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([!@#$%^&*(),.?\":{}|[A-Za-z0-9]{3})<([!@#$%^&*(),.?\":{}|[A-Za-z0-9]+)(?!\!\@\#\$\%\^\&\*\(\)\,\.\?\"\:\{\}\||[A-Za-z0-9])"

for n in range(number):
    data = input()
    result = re.findall(pattern, data)
    if result:
        if len(result[0][0]) != len(result[0][5]):
            print(f"Password: {result[0][1]}{result[0][2]}{result[0][3]}{result[0][4]}")
    else:
        print("Try another password!")