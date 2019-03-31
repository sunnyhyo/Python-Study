# -*- coding: utf-8 -*-

# =============================================================================
# BIZ & AI lab study 1-1. numpy
# =============================================================================

import numpy as np

# =============================================================================
# list
# =============================================================================
ex_str = 'pandas'
a_list = list(ex_str)
print(a_list)

print(a_list[0])
print(a_list[1])
print(a_list[-1])
print(a_list[-2])

print(a_list[0:3])
print(a_list[:3])
print(a_list[1:3])

print(a_list[-3:])
print(a_list[-3:-1])

a_list[0] = '!'
print(a_list)
a_list[0] = 'p'
print(a_list)

# =============================================================================
print(a_list.index('n'))
print(a_list.index('a'))
print(a_list.index('a', 2))
print(a_list.index('a', 1))
print(a_list.index('a', 5))

print(a_list.index('a', a_list.index('a')+1))

a_list.insert(2, 99)
print(a_list)

a_list.insert(4, 999)
print(a_list)

del a_list[4]
print(a_list)

a_list.remove(99)
print(a_list)


b_list = [3,1,4,2]
print(b_list)

b_list = sorted(b_list)
print(b_list)
b_list = sorted(b_list, reverse=True)
print(b_list)

a_list.append(10)
print(a_list)

b_list.append(['x', 100])
print(b_list)
print(b_list[-1])
print(b_list[-1][1])

print(b_list + ['x', 100])
b_list.extend(['x', 100])
print(b_list)

# =============================================================================
# 배열 생성
# =============================================================================
print(np.zeros((3,2)))
print(np.ones((3,2)))
print(np.full((3,2), 99))
print(np.eye(3))

tmp_data = np.array([[1,2,3], [4,5,6]])
print(tmp_data)
print(tmp_data.shape)

print(np.zeros_like(tmp_data))
print(np.zeros(tmp_data.shape))

print(np.ones_like(tmp_data))
print(np.full_like(tmp_data, 99))

print(np.linspace(0, 1, 5))
print(np.arange(0, 10, 2, np.float))

print(a_list)
print(np.array(a_list))
print(b_list)
print(np.array(b_list))

# =============================================================================
# np.random
# =============================================================================
print(np.random.random((2, 3))) # uniform dist.
print(np.random.rand(2, 3)) # gaussian normal dist.
print(np.random.normal(0, 1, (2, 3))) # normal dist.
print(np.random.randn(2, 3)) # standard normal dist.

np.random.seed(1234)
print(np.random.normal(0, 1, (2, 3)))
np.random.seed(1234)
print(np.random.randn(2, 3))

print(np.random.randint(0, 5, size=(2, 3)))

# =============================================================================
# array shpe type
# =============================================================================
data = np.array([[1,2], [3,4], [5,6]])
print(data)
print(data.shape)
print(data.dtype)

float_data = data.astype(np.float64)
print(float_data)
print(float_data.dtype)

str_data = data.astype(np.string_)
print(str_data)

print(np.reshape(data, (2,3)))
print(np.reshape(data, (3,3)))

print(data)
print(data.T)

#np.int64 : 64 비트 정수 타입
#np.float32 : 32 비트 부동 소수 타입
#np.complex : 복소수 (128 float)
#np.bool : 불린 타입 (Trur, False)
#np.object : 파이썬 객체 타입
#np.string_ : 고정자리 스트링 타입
#np.unicode_ : 고정자리 유니코드 타입

# =============================================================================
# array slicing
# =============================================================================
print(data)

print(data[1])
print(data[0:2])
print(data[:2])
print(data[:])

print(data[1,:])
print(data[1][:])

print(data[:,1])
print(data[:][1])

print(data[0,0])

print(data[1:2])
print(data[1])
print(data[1:2].shape)
print(data[1].shape)

print(data[:2, 1:])

data[:2, 1:] = 0
print(data)

# =============================================================================
# array copy
# =============================================================================
tmp_data = data
copy_data = data.copy()
copy_data = np.copy(data)

print(tmp_data)
print(copy_data)

data[0,0] = 0
print(data)
print(tmp_data)
print(copy_data)

data = np.copy(copy_data)
print(data)

# =============================================================================
# array 연산
# =============================================================================
data_list = [[1,2], [3,4], [5,6]]
data = np.array(data_list)

print(data_list)
print(data)

print(data+3)
print(data_list + 3)

print(data*3)
print(data_list*3)

print(data**3)
print(data_list**3)

print(data + data)
print(data_list + data_list)
print(np.add(data, data))

print(data - data)
print(np.subtract(data, data))

print(data * data)
print(np.multiply(data, data))

print(data / data)
print(np.divide(data, data))

print(data ** data)
print(np.power(data, data))

print(np.dot(data, data.T))

print(np.log(data))

print(np.exp(data))

print(np.sqrt(data))

print(np.sin(data))
print(np.cos(data))
print(np.tan(data))

print(np.array_equal(data, data.copy()))

# =============================================================================

print(data)
print(data.sum())
print(np.sum(data))

print(data.sum(axis=0))
print(np.sum(data, axis=0))

print(data.sum(axis=1))
print(np.sum(data, axis=1))

data_3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(data_3.shape)

print(data_3)
print(np.sum(data_3))
print(np.sum(data_3, axis=0))
print(np.sum(data_3, axis=1))
print(np.sum(data_3, axis=2))

# =============================================================================

print(data.cumsum())
print(np.cumsum(data))
print(data.cumsum(axis=0))
print(np.cumsum(data, axis=0))
print(data.cumsum(axis=1))
print(np.cumsum(data, axis=1))


print(data.max())
print(np.max(data))


print(data.min())
print(np.min(data))

print(data.mean())
print(np.mean(data))


print(data.std())
print(np.std(data))


print(data.median())
print(np.median(data))

# =============================================================================
# array 추가 삭제
# =============================================================================
print(data)

print(np.insert(data, 1, 99))
print(np.insert(data, 0, 99))
print(np.insert(data, 0, 99, axis=0))
print(np.insert(data, 0, 99, axis=1))

print(np.delete(data, 0))
print(np.delete(data, 0, axis=0))
print(np.delete(data, 0, axis=1))

# =============================================================================
# array 결합
# =============================================================================
a_array = np.arange(1,5).reshape(2,2)
print(a_array)
b_array = np.arange(11,15).reshape(2,2)
print(b_array)

print(np.append(a_array, b_array))
print(np.append(a_array, b_array, axis=0))
print(np.append(a_array, b_array, axis=1))

print(np.concatenate((a_array, b_array)))
print(np.concatenate((a_array, b_array), axis=0))
print(np.concatenate((a_array, b_array), axis=1))

print(np.vstack((a_array, b_array)))
print(np.hstack((a_array, b_array)))

# =============================================================================
# array 분할
# =============================================================================
c_array = np.arange(0,12).reshape(6,2)
print(c_array)

print(np.vsplit(c_array, 2))
print(type(np.vsplit(c_array, 2)))
print(np.vsplit(c_array, 2)[0])
print(np.vsplit(c_array, 2)[1])

print(np.vsplit(c_array, 3))
print(np.vsplit(c_array, 3)[0])
print(np.vsplit(c_array, 3)[1])
print(np.vsplit(c_array, 3)[2])


print(np.hsplit(c_array, 2))
print(np.hsplit(c_array, 2)[0])
print(np.hsplit(c_array, 2)[1])

print(np.hsplit(c_array, 3))
