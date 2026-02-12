#Concept: Reusable logic
#DevOps Example: Health check function
#Used everywhere in automation
def check_cpu(cpu):
    if cpu > 80:
        return "High CPU"
    return "Normal"

status = check_cpu(90)
print(status)
