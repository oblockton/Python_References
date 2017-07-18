# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required
# to make up that value. The return value should be a tuple of three numbers
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

#>>>>>>correct answer that solves for all #'s'
def stamps(n):
    tab = n
    fiver, twoper, penny = 0,0,0
    if (n / 5) > 0 :
        fiver = n / 5
        tab = tab - (5 * fiver)
        return fiver
    else:
        tab = n
        return fiver = 0

    if fiver > 0 :
        return twoper = tab / 2
        tab = tab - (2 * twoper)
    else:
        tab = n
        return twoper = 0

    if twoper > 0 :
        return penny = tab / 1
    else :
        return penny = 0
    if fiver,twoper,penny > -1,-1,-1 :
        return fiver, twoper, penny

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
#print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
#print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
#print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps


#>>>> only solves for #'s greater than largest possible denomintaor(e.g 5)
def stamps(n):
    tab = n
    if tab != 0 :
            if (tab / 5) > 0:
                fiver = tab / 5
                tab = tab - (5 * fiver)
                if fiver > 0 :
                    twoper = tab / 2
                    tab = tab - (2 * twoper)
                    if twoper > 0:
                        pence = tab / 1
                        return fiver, twoper, pence
                    else :
                        pence = 0
                else:
                    tab = n
                    twoper = 0
            else:
                tab = n
                fiver = 0
                return fiver, twoper, pence
    else :
        fiver, twoper, pence = 0, 0, 0
        return fiver, twoper, pence
