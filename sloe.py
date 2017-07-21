def sloe():
    print "The neon panel has a question\n"
    score = 0.0
    q = ["what is the square root of 81:\n[a] 1  [b] 2  [c] 3  [d] 9\n",
         "what is the Lancelots favourite colour:\n[a] blue  [b] green   [c] red  [d] yellow\n",
         "spell bee:\n[a] b  [b] be   [c] bee  [d] beee\n",
         "knock knock:\n[a] who's there?  [b] what?   [c] yes?  [d] good evening.\n"]
    a= ["d","a","c","a"]
    for i in range(len(q)):
        ans = raw_input(q[i])
        ans.lower()
        if(ans==a[i]):
            score+=1
            print "correct - score: " + str(score)
        else:
            print "incorrect the answer was " + a[i] + " - score: " + str(score)
    if(score == len(a)):
        print "congratulations"
    print "you got " + str((score/(len(a)))*100) +"%"
sloe()