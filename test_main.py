from log_manager import LogFile, DelimFile
from custom_exception import MyError

if __name__ == '__main__':
    log = LogFile('test.log')
    c = DelimFile('text.csv', ',')

    log.write('this lone is a log msg')
    log.write('this is second log')
    c.write(['a', 'b', 'v', 'f'])
    c.write(['1', '2', '3', '4'])

    raise MyError("")

