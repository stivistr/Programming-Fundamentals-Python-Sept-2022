import re

number = int(input())
for n in range(number):
    data = input()
    pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
    result = re.match(pattern, data)
    if not result:
        print("Invalid barcode")
    else:
        extract_nums = re.findall('\d', result.group())
        if not extract_nums:
            print('Product group: 00')
        else:
            print(f"Product group: {''.join(extract_nums)}")