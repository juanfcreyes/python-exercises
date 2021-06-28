def validate_phone_number(number):
    pattern = '^09([0-9][- ]*[0-9]{3,3}[- ]*[0-9]{4,4})(?!.)'
    match = re.search(pattern, number)
    if match:
        print(match.group())

validate_phone_number("1234567980")
validate_phone_number("099527575578df")
validate_phone_number("0785275755")
validate_phone_number("099527575510")
validate_phone_number("0995275755")
validate_phone_number("099-527-5755")
validate_phone_number("099 527 5755")
