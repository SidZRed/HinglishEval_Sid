
def f(n):
    """
    Function f ko implement karo jo n ko parameter ke roop mein leta hai,
    aur ek list return karta hai jiska size n hota hai, aisa ki index i par element ka value i ka factorial hota hai agar i even hai
    ya fir 1 se lekar i tak ke numbers ka sum hota hai otherwise.
    i ka start 1 se hota hai.
    i ka factorial 1 se lekar i tak ke numbers ka multiplication hota hai (1 * 2 *... * i).
    Udaharan:
    f(5) == [1, 2, 6, 24, 15]
    """
    if n in numbers:
            return numbers.index(n)
    else:
        for i in range(1, n+1):
                index = i-1
                count = i
                fact = 1
                while index >= 0:
                        element = i*index
                        index = index -1 
                        fact = fact * element
                fact = fact * i
        return fact