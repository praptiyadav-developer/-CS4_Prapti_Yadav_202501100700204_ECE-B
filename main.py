
file = open("CS4.txt", "r")

content = file.read()
file.seek(0)   

line1 = file.readline()
line2 = file.readline()

file.seek(0)

lines = file.readlines()

total_lines = len(lines)

print("Total number of lines:", total_lines)

print("\nFirst 2 lines:")
print(lines[:2])

print("\nLast 2 lines:")
print(lines[-2:])

file.close()


file = open("CS4.txt", "r")
lines = file.readlines()

log_count = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

for line in lines:
    if "INFO" in line:
        log_count["INFO"] += 1
    if "WARNING" in line:
        log_count["WARNING"] += 1
    if "ERROR" in line:
        log_count["ERROR"] += 1

print("\nLog Counts:")
print(log_count)

file.close()

info_file = open("info_logs.txt", "w")
warning_file = open("warning_logs.txt", "w")
error_file = open("error_logs.txt", "w")

info_lines = []
warning_lines = []
error_lines = []

for line in lines:
    if "INFO" in line:
        info_lines.append(line)
    if "WARNING" in line:
        warning_lines.append(line)
    if "ERROR" in line:
        error_lines.append(line)

# Using write()
for l in info_lines:
    info_file.write(l)

# Using writelines()
warning_file.writelines(warning_lines)
error_file.writelines(error_lines)

info_file.close()
warning_file.close()
error_file.close()

keyword = input("\nEnter keyword to search: ")

file = open("CS4.txt", "r")
lines = file.readlines()

result_file = open("search_result.txt", "w")

print("\nMatching Lines:")

for line in lines:
    if keyword in line:
        print(line.strip())
        result_file.write(line)

file.close()
result_file.close()

file = open("CS4.txt", "r")

print("\nFirst 50 characters:")
print(file.read(50))

file.seek(0)
print("\nAfter seek(0):")
print(file.read(50))

file.seek(0)
content = file.read()
middle = len(content) // 2
file.seek(middle)

print("\nFrom middle:")
print(file.read(50))

file.seek(0, 2)  
file.seek(file.tell() - 100)

print("\nLast 100 characters:")
print(file.read())

file.close()
