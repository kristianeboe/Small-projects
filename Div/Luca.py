def encrypt_messege(messege, x):
    e_messege = ""
    if type(x) != int:
        raise ValueError()
    for l in messege:
        e_messege += chr(ord(l)+x)#(Char value of l) + x
    return e_messege

#print encrypt_messege("Meeting at 5PM tomorrow.", 6)

def left_aligned_triangle():
    hight = int(raw_input("Enter hight: "))
    for i in range(1,hight+1):
        print "*"*i

#left_aligned_triangle()

def right_aligned_triangle():
    hight = int(raw_input("Enter hight: "))
    for i in range(1,hight+1):
        print " "*(hight-i) + "*"*(i)

#right_aligned_triangle()

def diamond():
    hight = int(raw_input("Enter hight: "))
    for i in range(1,hight+1):
        print "*"*i + (" "*(hight-i) + "*"*(i))

#diamond()

def moby_ave_index(c):
    moby = '''Call me Ishmael. Some years ago - never mind how long precisely -
  having little or no money in my purse, and nothing particular to interest me on shore,
  I thought I would sail about a little and see the watery part of the world.
  It is a way I have of driving off the spleen and regulating the circulation.
  Whenever I find myself growing grim about the mouth;
  whenever it is a damp, drizzly November in my soul;
  whenever I find myself involuntarily pausing before coffin warehouses,
  and bringing up the rear of every funeral I meet;
  and especially whenever my hypos get such an upper hand of me,
  that it requires a strong moral principle to prevent me from deliberately stepping into the street,
  and methodically knocking people's hats off - then,
  I account it high time to get to sea as soon as I can.
  This is my substitute for pistol and ball.
  With a philosophical flourish Cato throws himself upon his sword;
  I quietly take to the ship.
  There is nothing surprising in this. If they but knew it, almost all men in their degree,
  some time or other, cherish very nearly the same feelings towards the ocean with me.'''
    indi = 0.0
    occ = 0.0
    length = len(moby)
    for index in range(length):
        if c == moby[index]:
            indi += index
            occ += 1.0
    if occ == 0:
        retrurn False
    return (indi/occ)/length

print moby_ave_index('.')
