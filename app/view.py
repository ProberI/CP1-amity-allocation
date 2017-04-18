#!/usr/bin/env python
"""
Amitié is an interactive commandline application to help you allocate rooms to
Andela Employees randomly and efficiently.

Usage:
    Amitié create_room <room_type> <room_name>...
    Amitié add_person <first_name> <last_name> <role> <accomodation>
    Amitié reallocate_person <full_names> <room_name>
    Amitié load_people <file_name>
    Amitié print_allocations [--file_name]
    Amitié unallocated [--file_name]
    Amitié print_room <room_name>
    Amitié save_state <db_name>
    Amitié (-i | --interactive)
    Amitié (-h | --help | --version)


Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
import time

from docopt import docopt, DocoptExit

from termcolor import colored, cprint
from pyfiglet import figlet_format, Figlet

from cp.amity import Amity


def docopt_cmd(func):

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!\n')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def app_header():
    cprint("=================================================", 'blue')


class App(cmd.Cmd):
    intro = 'Welcome to Amitié!' + ' (Type help for a list of commands.)'
    custom_prompt = colored('Amitié ', 'green', attrs=[
        'bold']) + colored('-->', 'grey', attrs=['bold', 'blink'])
    prompt = custom_prompt
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""

        room_type = arg['<room_type>']
        room_name = arg['<room_name>']
        amity.create_room(room_type, room_name)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <role> <accomodation>"""

        first_name = arg['<first_name>']
        last_name = arg['<last_name>']
        role = arg['<role>']
        accomodation = arg['<accomodation>']
        amity.add_person(first_name, last_name, role, accomodation)

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <First_name> <Last_name> <room_name>"""

        First_name = arg['<First_name>']
        Last_name = arg['<Last_name>']
        room_name = arg['<room_name>']
        amity.reallocate_person(First_name, Last_name, room_name)

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <file_name>"""

        file_name = arg['<file_name>']
        amity.load_people(file_name)

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--file_name]"""

        amity.print_allocations()

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: unallocated [--file_name]"""

        amity.print_unallocated()

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""

        room_name = arg['<room_name>']
        amity.print_room(room_name)

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state <db_name>"""
        db_name = arg['<db_name>']
        amity.save_state(db_name)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    app_header()
    amity = Amity()
    App().cmdloop()

print(opt)
