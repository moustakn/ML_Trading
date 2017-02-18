import numpy as np


def building_arrays_example():

    #2D Sequence array. Useful to create spread sheet like layout
    print(np.array([(1,3,5),(2,4,6)]))

    print(np.empty(5))          #Built and empty array
    print(np.random.rand(5,4))  #2D array with 5 columns and 4 rows of random numbers

    # 2D array with a normal distribution and a mean of 50 and stard deviation of 10
    print(np.random.normal(50, 10, size=(2,3)))

    print(np.random,randit(0,10))               #Prints a random int from 1-10
    print(np.random.randint(0,10, size=5))      #5 random ints as a 1D array
    print(np.random.randint(0,10, size=(2,3)))  #2x3 array of random ints


def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    return a.argmax()


def test_run():

    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print("Array:", a)

    # Find the maximum and its index in array
    print("Maximum value:", a.max())
    print("Index of max.:", get_max_index(a))

def sum_example():

    np.random.seed(693)                         #Using this will get you the same random numbers
    a = np.random.randint(0,10, size=(5,4))     #5X4 random ints from 1-10

    print("Array:\n", a)
    print("Sum of elements", a.sum())
    print("Sum of each column", a.sum(axis=0))
    print("Sum of each row", a.sum(axis=0))
    print("Minimum of each column", a.min(axis=0))
    print("Maximum of each row", a.max(axis=0))
    print("Mean of all elements", a.mean())

def numpy_masking():

    a = np.array([(1,2,3,4),(5,6,7,8)])

    mean = a.mean()

    print(a[a < mean])    #Instead of looping over an array we can evaluate it in one line

    #Masking
    a[a < mean] = mean    #Relaces all of the values less than the mean with the mean
    print(a)

def numpy_arithmetic():

    a = np.array([(1,2,3,4),(10,20,30,40)])
    b = np.array([(1, 2, 3, 4), (10, 20, 30, 40)])

    print("\n Multiply by 2: \n", a * 2)        #Multiply each element by 2
    print("\n Divide by 2: \n", a / 2)          #Divid each element by 2
    print("\n Add two arrays: \n", a + b)       #Adds the elements of each array
    print("\n Multiply two arrays: \n", a * b)  #Multiply the elements of each array

if __name__=="__main__":
    numpy_arithmetic()












