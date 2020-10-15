import random
iRange = 0
iHead = 0
iTail = 0
while iRange<100:
    iEvent = random.randint(0,1) #let 0 means head, 1 means tail.
    if iEvent==0:
        iHead=iHead+1
    else:
        iTail=iTail+1
    iRange=iRange+1
print("Total No. of test cases: ", iRange)
print("No. of heads: ", iHead)
print("No. of tails ", iTail)