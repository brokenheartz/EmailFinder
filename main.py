#!/usr/bin/python3

import os, sys
from emailfinder.color import *
from emailfinder.email_finder import *

color = Color()

def output_format(function):
    def banner():
        print(color.GREEN + ' _____                _ _______ _           _')
        print(color.GREEN + '|  ___|              (_) |  ___(_)         | |')
        print(color.GREEN + '| |__ _ __ ___   __ _ _| | |_   _ _ __   __| | ___ _ __')
        print(color.GREEN + '|  __| \'_ ` _ \ / _` | | |  _| | | \'_ \ / _` |/ _ \ \'__|')
        print(color.GREEN + '| |__| | | | | | (_| | | | |   | | | | | (_| |  __/ |')
        print(color.GREEN + '\____/_| |_| |_|\__,_|_|_\_|   |_|_| |_|\__,_|\___|_|')
        print(color.YELLOW+ '                                      [Version 1.0]\n')
        function()
    return banner


@output_format
def usage():
    print('[+] Usage\t: {} <url> <filename>'.format(sys.argv[0]))
    print('[+] Example\t: {} http://target.com/ list_mail.txt'.format(sys.argv[0]))


@output_format
def main():
    try:
        target = sys.argv[1]
        file = sys.argv[2]
        email_finder = EmailFinder(url_target = target, file_name = file)
        email_finder.start_crawling()
    except KeyboardInterrupt:
        print(color.RED + current_time(), 'you stoped the program.')
        sys.exit(1)


if __name__ == '__main__':

    if os.path.exists(DIRECTORY) != True:
        print(color.RED + current_time(), 'Can\'t find {} directory.'.format(DIRECTORY))
        sys.exit(1)

    if len(sys.argv) != 3:
        usage()
        sys.exit(0)

    main()
