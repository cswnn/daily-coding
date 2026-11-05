def solution(phone_book):
    answer = True
    
    # 중복 x
#     phone_book.sort(key=lambda x: len(x))

#     for i in range(len(phone_book)):
#         # for j in range(i+1, len(phone_book)):
#         s = set(phone_book[j][:len(phone_book[i])] for j in range(i+1, len(phone_book)))
#         if phone_book[i] in s:
#             answer = False
#             break
    
    _phone_book = set(phone_book)
    for i in phone_book: # i: each phone number
        now = "" # prefix of i
        for j in i: 
            now += j # add prefix
            if now in _phone_book and now != i: # not itself but prefix is in phone_book
                answer = False
                return answer
    
    return answer