numberOfTests = 0
scorre = 0
total = 0
average = 0.0
scoreCount = 0

numberOfTests = int(input("Please enter the number of tests you want to average: "))

#Make these 3 lines repeat until scoreCount = numberOfTests
score = int(input("Please enter a score: "))
scoreCount = scoreCount + 1
total = total + score

average = total/scoreCount
print("The average is ",average)






