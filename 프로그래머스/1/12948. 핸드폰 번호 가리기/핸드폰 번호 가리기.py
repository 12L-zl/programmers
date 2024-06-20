def solution(phone_number):
    star = '*' * (len(phone_number) - 4)
    num = phone_number[-4:]
    return star + num