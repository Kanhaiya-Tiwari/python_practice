import psutil

def check_cpu_usage():
    user_cpu = int(input("Enter the CPU threshold"))
    current_cpu = psutil.cpu_percent(interval=1)
    if current_cpu > user_cpu:
        print("cpu alert email send")
    else:
        print("cpu is normal")
check_cpu_usage()