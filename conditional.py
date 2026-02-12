marks = input("your marks : ")
if (int(marks) <= 33):
    print("you are fail")
elif (int(marks) <=50):
    print("third division pass")
elif (int(marks) <=70):
    print ("second division pass")
else:
     print("first division pass")



#Concept: Decision making
#DevOps Example: Alert if CPU high

#Used in health checks & auto-alert tools

cpu_usage = 85

if cpu_usage > 80:
    print("⚠️ High CPU Alert!")
else:
    print("✅ CPU Normal")
