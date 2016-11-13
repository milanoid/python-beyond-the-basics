from assignment2 import WriteFile, CSVFormatter, LogFormatter

log = LogFormatter("log.txt")
log.write("some text")

csv = CSVFormatter("file.csv", ",")
csv.write(['a', 'b', 'c'])
