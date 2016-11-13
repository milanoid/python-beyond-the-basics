import datetime
import abc

DATE_TIME_STRING = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
NEWLINE = '\n'


class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        with open(self.filename, 'a') as FILE:
            FILE.write("{text}{newline}".format(text=text, newline=NEWLINE))


class CSVFormatter(WriteFile):
    def __init__(self, filename, delimiter):
        super(CSVFormatter, self).__init__(filename)
        self.delimiter = delimiter

    def write(self, list_of_characters):
        #[self.write_line("{item}{delimiter}".format(item=item, delimiter=self.delimiter)) for item in list_of_characters]
        line = self.delimiter.join(list_of_characters)
        self.write_line(line)


class LogFormatter(WriteFile):
    def __init__(self, filename):
        super(LogFormatter, self).__init__(filename)

    def write(self, text):
        self.write_line("{date_time} {message}".format(date_time=DATE_TIME_STRING, message=text, newline=NEWLINE))


