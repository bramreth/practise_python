def rev(arg):
    tmp = ""
    for x in range(len(arg)):
        tmp+=arg[len(arg)-x-1]
    print tmp
def fib(x):
    if(x<2):
        return x
    else:
        return fib(x-1) + fib(x-2)
def fizzbuzz(len):
    for i in range(1, len+1):
        if i%3==0:
            if i%5==0:
                print "fizzbuzz"
            else:
                print "fizz"
        elif i % 5 == 0:
            print "buzz"
        else:
            print i

pyg = 'ay'
original = raw_input('Enter a word:')
rev(original)
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'

