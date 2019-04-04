
#순차탐색
#순서대로 탐색, 
#input : 리스트 a, 찾고자 하는 값 x
#output : 찾고자 하는 값의 위치 / 못찾으면 -1

def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            return print("the index : ", i) 
    return print("not exist : ", -1)

aa = [15, 85, 0, 63]
search_list(aa, 85)
search_list(aa, 63)
search_list(aa, 2)


#선택정렬 1 
#최솟값을 찾는다. 최솟값의 인덱스를 반환한다.
#리스트에서 최솟값을 찾아, 새로운 리스트에 작은 값 순서대로 저장한다.
#input : unsorted list. a
#output : sorted list. result

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(0, n):
        if a[i] < a[min_idx]:
            min_idx = i 
    return min_idx

def selection_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        print("a1: ", a)
        min_value = a.pop(min_idx)
        print("min_value: ", min_value)
        #print("a2: ", a)
        result.append(min_value)
        print("sorted list: ", result)
        print("")
    #return result

aa = [15, 85, 0, 63]
selection_sort(aa)
#print(selection_sort(aa))


#선택정렬 2
#최솟값을 찾는다. 
# ㅑ 번째 값부터 끝까지 돌아다니면서 최솟값이 있으면 젤 앞 숫자와 자리바꾸기
#input : unsorted list a 
 
def selection_sort_2nd(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i 
        print("i = ", i, a)
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print("j = ", j, a)
        print("")

    #return a
aa = [15, 85, 0, 63]
selection_sort_2nd(aa)
bb = [5,4,3,2,1]
selection_sort_2nd(bb)


def selection_sort_error(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i 
        print("\ni = ", i, a)
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j
                a[i], a[min_idx] = a[min_idx], a[i]
                print("j = ", j, a)
    #return a
aa = [15, 85, 0, 63]
selection_sort_error(aa)





#버블정렬
#인근 두 값의 대소비교
#큰 값을 뒤로 보내기, 나머지 반복
#input : unsorted list a

def bubble_sort(a):
    n = len(a)
    for i in range(0, n):
        print("\ni = ", i, a)
        for j in range(0, n-1):
            if a[j] > a[j+1]:
               a[j], a[j+1] = a[j+1], a[j]
            print("j = ", j, a)
    print("\nresult = ", a)
    #return a

aa = [15, 85, 0, 63]
bubble_sort(aa)

bb = [78, 23, 45, 92, 12, 6]
bubble_sort(bb)
#print(bubble_sort(aa))


