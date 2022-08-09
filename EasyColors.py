colors = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    None: ''
}
background_colors = {
    'black': '\033[40m',
    'red': '\033[41m',
    'green': '\033[42m',
    'yellow': '\033[43m',
    'blue': '\033[44m',
    'purple': '\033[45m',
    'cyan': '\033[46m',
    'white': '\033[47m',
    None: ''
}
attributes = {
    'bold': '\033[1m',
    'fade': '\033[2m',
    'italic': '\033[3m',
    'underline': '\033[4m',
    'blink': '\033[5m',
    'strikethrough': '\033[9m'
}

class Color():

    def color(self, text = 'Hello! This is EasyColor. By Dmitry Smotryaev!', color = None, background_color = None, attrs = None):
        result = colors[color] + background_colors[background_color] + text + '\033[0m'
        if attrs != None:
            for attribute in attrs:
                result = attributes[attribute] + result
        return result

    def printc(self, text = 'Hello! This is EasyColor. By Dmitry Smotryaev!', color = None, background_color = None, attrs = None):
        result = colors[color] + background_colors[background_color] + text + '\033[0m'
        for attribute in attrs:
            result = attributes[attribute] + result
        print(result)

    def cwarn(self, text = 'Hello! This is EasyColor. By Dmitry Smotryaev!', mode = None):
        modes = {
            'fail': '\033[31m',
            'cfail': '\033[1;31m',
            'success': '\033[32m',
            'failtext': '\033[3;31m',
            'marker': '\033[43m\033[1;30m'
        }
        return modes[mode] + text + '\033[0m'
