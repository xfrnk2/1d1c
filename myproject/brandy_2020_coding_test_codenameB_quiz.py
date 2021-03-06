#친구로 부터 공유받은 2020 브랜디 코딩대회 모의테스트 문제(근묵자흑)을 풀었다.


def func(arr, N, k):

    # 배열에서 가장 작은 값의 인덱스 i를 구한다.
    i = arr.index(min(arr))

    #i 기준 앞에 위치한 그룹의 횟수 = (i+1) // (k-1)
    #i 기준 뒤에 위치한 그룹의 횟수 = (N - i)  //  (k-1)
    return (i+1) // (k-1) + (N - i)  //  (k-1)

print(func([2, 3, 1, 4], 4, 3))
print(func([7, 3, 1, 8, 4, 6, 2, 5], 8, 3))

example3 = [5]*37
example3[4] = 1
print(func(example3, 37, 4))

def func_second(arr, N, k):
    print((N - arr.index(min(arr))) // (k-1)+1)


func_second([2, 3, 1, 4], 4, 3)
func_second([7, 3, 1, 8, 4, 6, 2, 5], 8, 3)
func_second(example3, 37, 4)