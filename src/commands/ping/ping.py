


class PingCommand:

    command = "PING"

    def __init__(self, args):
        self.args = args
        

    def execute(self):
        if len(self.args) == 0:
            return "+PONG\r\n"
        elif len(self.args) == 1:
            return f"+{self.args[0]}\r\n"
        else:
            return "-ERR wrong number of arguments for 'ping' command\r\n"