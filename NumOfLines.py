#Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.

file = open("sample.txt", "r")
lines = file.readlines()
file.close()

total_lines = len(lines)
print("Total number of lines:", total_lines)


if total_lines >= 2:
    print("2nd Line:", lines[1].strip())
    
if total_lines >= 4:
    print("4th Line:", lines[3].strip())
