
no_of_errors = 0
with open("D:/Python/LogsToRead/.logs/combined-log-24-08-2020.log", "r") as a_file:
    for line in a_file:
        stripped_line = line.strip()
        if stripped_line.startswith("{\"error\""):
            no_of_errors += 1
        print(stripped_line)

print(no_of_errors)
# Open directory with logs files
# log_file_path = {path to dir}
# create regex for various scenarios e.g error, context etc
# create list of matches
# match_list = []
# search files for lines matching regex
# with open (file) as file
# for line in file
# for match in re.finditer(regex, line, re.S):
# match_text = match.group()
# math_list.append(match_text)
# print match_text
