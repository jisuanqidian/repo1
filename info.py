def color_format(color,bright=False) :
    colors = {
            'BLACK': '30', 'RED': '38;2;235;44;44', 'GREEN': '38;2;50;205;50', 'YELLOW': '38;2;255;215;0',
            'BLUE': '38;2;30;144;255', 'MAGENTA': '35', 'CYAN': '36', 'WHITE': '37',
            'DEFAULT': '0'}
    bright = '1;' if bright else ''
    if color not in colors :
        color = 'WHITE'
    return f'\033[{bright}{colors[color]}m'

def color_info(color,info,bright=False,prt=False) :
    formatted_info = color_format(color,bright) + info + color_format('DEFAULT',False)
    if prt :
        print(formatted_info)
    return formatted_info

def black_info(info,bright=False,prt=False) :
    return color_info('BLACK',info,bright,prt)

def red_info(info,bright=False,prt=False) :
    return color_info('RED',info,bright,prt)

def green_info(info,bright=False,prt=False) :
    return color_info('GREEN',info,bright,prt)

def yellow_info(info,bright=False,prt=False) :
    return color_info('YELLOW',info,bright,prt)

def blue_info(info,bright=False,prt=False) :
    return color_info('BLUE',info,bright,prt)

def magenta_info(info,bright=False,prt=False) :
    return color_info('MAGENTA',info,bright,prt)

def cyan_info(info,bright=False,prt=False) :
    return color_info('CYAN',info,bright,prt)

def white_info(info,bright=False,prt=False) :
    return color_info('WHITE',info,bright,prt)

def warn_info(warn_str) :
    print(yellow_info('[WARNING]',True)+f' {warn_str}')

def error_info(err_str) :
    print(red_info('[ERROR]',True)+f' {err_str}')
