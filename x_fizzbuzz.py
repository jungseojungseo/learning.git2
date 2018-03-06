# -*- coding: utf-8 -*-

def fizzbuzz(x):
    """ 양의 정수 x를 전달받고, 1~x까지(경계 포함) 의 수를 리스트로 반환하는 함수를 작성한다
        단, 3의 배수는 "fizz", 5의 배수는 "buzz" 3과 5의 공배수는 "fizzbuzz"로 대체한다

        sample in/out:
            fizzbuzz(10) -> [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz']
            fizzbuzz(20) -> [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz']
    """
    # 여기 작성
    li = []
    li.append(1)
    li.append(2)
    
    for cnt in range(3, x + 1):
        if (cnt % 3 == 0 and cnt % 5 != 0):
            li.append('fizz')
        elif (cnt % 5 == 0 and cnt % 3 != 0):
            li.append('buzz')
        elif (cnt % 5 == 0 and cnt % 3 == 0):
            li.append('fizzbuzz')
        else:
            li.append(cnt)
        
    return li

if __name__ == "__main__":
    print fizzbuzz(10)
