

def read_logs():
    with open("demo.txt","r") as file:
        return [line.rstrip("\n") for line in file]
lines = read_logs()

def analyze(lines):
     log_count = {
          "Trading": 0,
          "Overview": 0,
          "Error": 0,
          "Warning": 0

     }
     for line in lines:
            if "Trading" in line:
                 log_count["Trading"] += 1
            elif "Overview" in line:
                 log_count["Overview"] += 1
            elif "Error" in line:
                 log_count["Error"] += 1
            elif "Warning" in line:
                 log_count["Warning"] += 1
            else:
                 pass
     return log_count
import json
def write_json():
    with open("output.json","w+") as json_files:
         json.dump(counts,json_files)

lines = read_logs()   
counts = analyze(lines)
write_json(counts)