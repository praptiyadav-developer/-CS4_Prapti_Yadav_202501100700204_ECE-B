# -CS4_Prapti_Yadav_202501100700204_ECE-B


This project demonstrates Python file handling operations using a log file (CS4.txt).
It covers reading, writing, searching, and file pointer operations.

🚀 Features
✅ Task 1: Basic File Reading
Read file using:
read()
readline()
readlines()
Outputs:
Total number of lines
First 2 lines
Last 2 lines
✅ Task 2: Log Classification
Counts occurrences of:
INFO
WARNING
ERROR
Stores results in a dictionary
✅ Task 3: Filtered File Writing

Creates separate log files:

info_logs.txt
warning_logs.txt
error_logs.txt

Uses:

write()
writelines()
✅ Task 4: Search Feature
Takes user input (keyword)
Displays matching lines
Saves results in:
search_result.txt
⭐ File Pointer (seek) Operations
Read first 50 characters
Move pointer to:
Beginning → seek(0)
Middle → seek(len(file)//2)
End → last 100 characters
📄 Sample Input File (CS4.txt)
INFO System started successfully
INFO User login successful
WARNING Disk space is low
ERROR Failed to connect to database
INFO Scheduled backup completed
WARNING High memory usage detected
ERROR Unable to open file
INFO Process completed
WARNING Network latency is high
ERROR Timeout occurred
▶️ How to Run
Clone this repository:
git clone https://github.com/your-username/file-handling-cs4.git
Navigate to project folder:
cd file-handling-cs4
Run the program:
python main.py
📂 Output Files Generated
info_logs.txt
warning_logs.txt
error_logs.txt
search_result.txt
💡 Concepts Covered
File handling in Python
Reading & writing files
String searching
Dictionaries
File pointer manipulation (seek())
