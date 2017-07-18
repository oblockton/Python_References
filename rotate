# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(string, n):
    rotated = ''
    for letter in string:
        rotated = rotated + shift_n_letters(letter,n)
    return rotated
    # Your c

def shift_n_letters(letter, n):
    if (ord(letter) + n) <= ord('z') and (ord(letter) + n) >= ord('a') :
        return chr(ord(letter) + n)
    if (ord(letter) + n) > ord('z') :
        remainder = (ord(letter) + n) - ord('z')
        return chr((ord('a') - 1) + remainder)
    if (ord(letter) + n) < ord('a'):
        remainder = ord('a') - (ord(letter) + n)
        if remainder < 26:
            return chr((ord('z') + 1) - remainder)
        else:
            return chr(32)

print ord(' ')
print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
print rotate("this course teaches you to code", 7)
#>>>> 'aopz jvbyzl alhjolz fvb av jvkl'
