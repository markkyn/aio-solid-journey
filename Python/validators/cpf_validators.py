INVALID_CPF = list()

for digit in range(0,10):
    cpf = str()
    for i in range(0,11):
        cpf += str(digit)
    
    INVALID_CPF.append(cpf)


def clear_cpf_mask(cpf) -> str:
    return cpf.replace(".", "").replace("-", "")

def is_cpf_valid(cpf: str) -> bool:
    _cpf : str = clear_cpf_mask(cpf)

    if len(_cpf) != 11:
        return False
    
    for invalid in INVALID_CPF:
        if _cpf == invalid:
            return False

    # First Digit    
    sum = 0
    for multiplier, index in zip(range(10, 1, -1), range(0, 9)):
        sum += int(_cpf[index]) * multiplier
    
    remainder = sum % 11

    if remainder < 2:
        first_digit = 0
    else:
        first_digit = 11 - remainder
    
    print(remainder)

    sum = 0
    for multiplier, index in zip(range(11, 0, -1), range(0, 10)):
        sum += int(_cpf[index]) * multiplier

    remainder = sum % 11

    if remainder < 2:
        second_digit = 0
    else:
        second_digit = 11 - remainder

    print(remainder)

    print(f"{first_digit} {second_digit}")

    if first_digit == int(_cpf[9]) and second_digit == int(_cpf[10]):
        return True
    else:
        return False