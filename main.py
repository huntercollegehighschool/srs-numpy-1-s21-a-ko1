# 1. Import the numpy package under the name `np`
import numpy as np

##### DECLARING NUMPY ARRAYS #####

# 2. Use np.array(<list>) to convert the list below into a numpy array. The array should be saved in a variable. Then print both the list and the array.
a = [300, -200, 100, 0, -100, 200, -300]
num_arr = np.array(a)

## The array method in numpy has an optional dtype argument which specifies the datatype each element should be. For the array above, it could be implemented using A = np.array(a, dtype=str) ##


# 3. Declare new arrays with different datatypes using the list from #2. Datatypes to use: str, float, np.int32, np.int8, np.uint32, up.uint8.
num_arr = np.array(a, dtype=str)
arr_float = np.array(a, dtype=float)
arr_i32 = np.array(a, dtype=np.int32)
arr_i8 = np.array(a, dtype=np.int8)
arr_ui32 = np.array(a, dtype=np.uint32)
arr_ui8 = np.array(a, dtype=np.uint32)

# 4. Use np.zeros(<int>) to create a array of zeroes of size 10. This should be saved in a variable. Then print the array.
arr_zeros = np.zeros(10)

# 5. In your array of zeroes, change the fifth 0 to a 6. (remember how indexing works in lists?) Print the array.
arr_zeros[4] = 6


# 6. Use np.arange(<int>, <int>) to create an array with values ranging from 11 to 46. Print the array.
arr_ranges = np.arange(11, 47)

# 7. Reverse the array you created in #6. Print the array.
arr_rev = arr_ranges[::-1]


# 8. Use <array>.reshape(<int>, <int>) to turn your array from #6 into a multidimensional 6x6 array. Print the array.
arr_reshaped = arr_ranges.reshape(6, 6)



# 9. Use np.random.random((<int>, <int>)) to create a 10x10 array with random values. Print the array.
arr_10b10 = np.random.random((10, 10))


# 10. Use np.random.randint(<int>, <int>, size=(<int>, <int>)) to create a 3x3 array with random integers. Print the array.
arr_3b3 = np.random.randint(3, 20, size=(3, 3))


# 11. Use <array>.max() and <array>.min to identify the maximums and minimums of the arrays you created in #9 and #10. Print the results.
max_9 = arr_10b10.max()
min_9 = arr_10b10.min()
max_10 = arr_3b3.max()
min_10 = arr_3b3.min()

# 12. Use <array>.mean() to find the means of the two arrays you created in #9 and #10. Print the results.
mean_9 = arr_10b10.mean()
mean_10 = arr_3b3.mean()

# 13. Convert the following two lists into 2X3 arrays. (You will need to use np.array and .reshape)

a = [2, 3, 5, 7, 11, 13]
b = [3, 1, 4, 1, 5, 9]
a_arr = np.array(a)
b_arr = np.array(b)
resh_a = a_arr.reshape(2, 3)
resh_b = b_arr.reshape(2, 3)

# 14. Add the two arrays from #13 (<array> + <array>)
add_13 = resh_a + resh_b

# 15. Multiply both arrays from #13 by 10.
mult_a = resh_a * 10
mult_b = resh_b * 10




