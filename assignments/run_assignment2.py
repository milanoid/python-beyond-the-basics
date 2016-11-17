from assignments.assignment2 import CSVFormatter, LogFormatter

log = LogFormatter("log.txt")
log.write("some text")

csv = CSVFormatter("file.csv", ",")
csv.write(['a', 'b', 'c'])
