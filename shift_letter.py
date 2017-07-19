# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    if (ord(letter) + n) < ord('z') and (ord(letter) + n) >= ord('a') :
        return chr(ord(letter) + n)
    if (ord(letter) + n) >= ord('z') :
        remainder = (ord(letter) + n) - ord('z')
        return chr((ord('a') - 1) + remainder)
    if (ord(letter) + n) < ord('a'):
        remainder = ord('a') - (ord(letter) + n)
        return chr((ord('z') + 1) - remainder)

print ord('s')
print ord('z')
print ord('a')
print ord('`')
print shift_n_letters('b', -1)
#>>> z
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
