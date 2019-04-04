# -*- coding: utf-8 -*-

# insert sort
# input : 리스트 a


def insert_sort(a):
    n = len(a)
    for i in range(1, n):  # 1부터 n 까지
        key = a[i]  # i 번 위치에 있는 값을 key 에 저장
        j = i - 1  # j 를 i 바로 왼쪽으로 저장

        # 리스트의 i 번 위치에 있는 값과 key 를 비교해 key 가 삽입될 적절한 위치를 찾음
        while a[j] > key and j >= 0:
            a[j+1] = a[j]  # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j = j - 1
        a[j+1] = key  # 찾은 삽입 위치에 key 를 저장
    return a



# merge sort
# input list a
# output noting


def merge_sort(a):
    n = len(a)
    # 종료조건 : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음
    if n == 1:
        return a
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n //2  # 중간을 기준으로 두 그룹을 나눔
    g1 = merge_sort(a[:mid])  # 재귀 호출로 첫 번째 그룹을 나눔
    g2 = merge_sort(a[mid:])  # 재귀 호출로 두 번째 그룹을 나눔

    # 두 그룹을 하나로 병합
    result = []  # 두 그룹을 합쳐 만들 최종 결과
    while g1 and g2:  # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[0] < g2[0]:  # 두 그룹의 맨 낲 자료 값을 비교
            result.append(g1.pop(0))
            # g1 값이 더 작으면 그 값을 빼내어 결과로 추가
        else:
            result.append(g2.pop(0))
            # g2 값이 더 크면 그 값으 빼내어 결과로 추가
    # 아직 남아 있는 자료들을 결과에 추가
    # g1 과 g2 중 이미 빈것은 while 을 바로 지나감
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result


# quick sort
# input : unsorted list 1
# 리스트 a 에서 어디부터(start) 어디까지(end)가 정렬 대상인지
# 범위를 지정하여 정렬하는 재귀 호출 함수

def quick_sort_sub(a, start, end):
    # 종료 조건 : 정렬 대상이 한 개 이하면 정렬 종료
    if end - start <= 0:
        return
    # 기준 값을 정하고 기준 값에 맞춰 리스트 안에서 각 자료의 위치를 맞춤
    # [기준 값보다 작은 값들, 기준값, 기준값보다 큰 값]
    pivot = a[end]  # 편의상 리스트 마지막 값을 기준값으로 정함
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    # 재귀 호출
    quick_sort_sub(a, start, i - 1)  # 기준 값보다 작은 그룹을 재귀 호출로 다시 정렬
    quick_sort_sub(a, i + 1, end)  # 기준 값보다 큰 그룹을 재귀 호출로 다시 정렬


# 리스트 전체 (0~ len(a)-1)를 대상으로 재귀 호출 함수 호출
def quick__sort(a):
    quick_sort_sub(a, 0, len(a)-1)


def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)


def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr





if __name__ == "__main__":
    d = [2, 3, 4, 12, 7, 5, 8]
    print(insert_sort(d))
    print(merge_sort(d))
    quick__sort(d)
    print(d)
    print(quick_sort(d, 0, len(d)-1))