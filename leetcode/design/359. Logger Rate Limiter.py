"""
Design a logger system that receive stream of messages along with its timestamps, 
each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), 
return true if the message should be printed in the given timestamp, 
otherwise returns false.

It is possible that several messages arrive roughly at the same time.
"""

class Logger:
    def __init__(self):
        self.d = {}
    
    def shouldPrintMessage(self, timestamp: 'int', message: 'str') -> 'bool':
        if message not in self.d or self.d[message] + 10 <= timestamp:
            self.d[message] = timestamp
            return True
        return False

logger = Logger()

# logging string "foo" at timestamp 1
print(logger.shouldPrintMessage(1, "foo"))

#logging string “bar” at timestamp 2
print(logger.shouldPrintMessage(2, "bar"))

#logging string "foo" at timestamp 3
print(logger.shouldPrintMessage(3,"foo"))

#logging string “bar” at timestamp 8
print(logger.shouldPrintMessage(8,"bar"))

#logging string "foo" at timestamp 10
print(logger.shouldPrintMessage(10,"foo"))

#logging string "foo" at timestamp 11
print(logger.shouldPrintMessage(11,"foo"))

"""
结果
True
True
False
False
False
True
"""