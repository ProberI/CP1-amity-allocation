#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Amitié is an interactive commandline application to help you allocate rooms to
Andela Employees randomly and efficiently.

Usage:
    Amitié create_room <room_type> <room_name>...
    Amitié add_person <first_name> <last_name> <role> [<accomodation>]
    Amitié reallocate_person <emp_id> <room_name>
    Amitié load_people <file_name>
    Amitié print_allocations [--o=file_name]
    Amitié unallocated [--file_name]
    Amitié print_room <room_name>
    Amitié save_state <db_name>
    Amitié load_state <db_name>
    Amitié delete_person <person_id>
    Amitié delete_rooom <room_name>
    Amitié list_people
    Amitié list_rooms
    Amitié (-i | --interactive)
    Amitié (-h | --help | --version)


Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import os
import sys
import cmd
import time

from docopt import docopt, DocoptExit

from termcolor import colored, cprint

from pyfiglet import figlet_format

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
    cprint(' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ',
           'red', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ',
           'red', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ',
           'red', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ',
           'red', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ',
           'red', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@@#####@@@####@@@###+@@###@########@###@@@@#+@@@@@@@@@@@@@@@@@@@@ ',
           'red', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@@;`  ,@@@````#@#.` `@@` `@,```` ``@#` #@@;. @@@@@@@@@@@@@@@@@@@@ ',
           'red', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@@.`.` @@@`   #@@.` `@@   @:`` ` ``@@ `,@@ `:@@@@@@@@@@@@@@@@@@@@ ',
           'red', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@@ ` ` @@@     @#:`  @@  ,@@@@``:@@@@`` #@ ,@@@@@@@@@@@@@@@@@@@@@ ',
           'green', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@#``#``@@@` `..#``  ,@@`  @@@@. ,@@@@+`  @``#@@@@@@@@@@@@@@@@@@@@ ',
           'green', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@#``# .#@@   ``@. ```@@` `@@@@: ,@@@@#` :`.,@@@@@@@@@@@@@@@@@@@@@ ',
           'green', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@+ .@``+@@` `  @``   @@`.`@@@@:`:@@@@@`   .#@@@@@@@@@@@@@@@@@@@@@ ',
           'green', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@, `@` ,@@` .` @. ````@@``@@@@``.@@@@@+```.#@@@@@@@@@@@@@@@@@@@@@ ',
           'green', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@` .@```@@` ```#` `` #@` `@@@@..:@#@@@@` .,#@@@@@@@@@@@@@@@@@@@@@ ',
           'green', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@.``@.``@@  `:`.```  #@```@@@@``:@@@@@@``,#@@@@@@@@@@@@@@@@@@@@@@ ',
           'green', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@#. ````.@@. `# ` :  .@@`  @@@#,.,@@@@@@;` @@@@@@@@@@@@@@@@@@@@@@@ ',
           'green', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@#.`       @@```#   ''`.#@. `@@@@:`;@@@@@@; .@@@@@@@@@@@@@@@@@@@@@@@ ',
           'green', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@: ### `+@`.:@`` @```@@` `@@@@.;``@@@@@@;``@@@@@@@@@@@@@@@@@@@@@@@ ',
           'yellow', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@: `@@#`+@@@@@@##@@+, @@` `@@@@@@@@@@@@@;  @@@@@@@@@@@@@@@@@@@@@@@ ',
           'yellow', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@. ,@@@@@@;`. ` . #@@+@#`:#@@+`   ``.+@@@:`@@@@@@@@@@@@@@@@@@@@@@@ ',
           'yellow', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@#@@@@;` .`+:`#.```+#@@@@@``` #. # ,```#@@@@@@@@@@@@@@@@@@@@@@@@@ ',
           'yellow', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@@@@ ,```# ``.,.@`` `@@@,``.#`` ``  ,;`. #@@@@@@@@@@@@@@@@@@@@@@@ ',
           'yellow', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@@#````:  ,+##+.. +; ,#.``# `.+#@# `  ``;`@@#@@@@@@@@@@@@@@@@@@@@ ',
           'yellow', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@@@ `,: :@@@@#@#@@#``# ``@ `##@@@@@@@@# `; `#@@@@@@@@@@@@@@@@@@@@@ ',
           'yellow', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@#`:#`.@@####@##@@@@+``..`,##@#@@##@@@@@;`,# ##@@@@@@@@@@@@@@@@@@@ ',
           'yellow', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@@`,``:@@#@@##@+####@##.#.;##@@@@#@#@@#@@@#``  #@@@@@@@@@@@@@@@@@@@ ',
           'yellow', attrs=['bold'])
    time.sleep(0.2)
    cprint(' @@@@@@@@@@@@@@@@@@  # :@#.@#@###@###@#@@+`,@@####@##@@@#@#@@#`#``@@@@@@@@@@@@@@@@@@@ ',
           'yellow', attrs=['bold'])
    time.sleep(0.8)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    cprint(figlet_format('AMITY', font='eftichess'), 'cyan')
    cprint('=' * 70,  'cyan')
    cprint('=' * 70, 'green')
    cprint('=' * 70 + '\n', 'yellow')


class App(cmd.Cmd):
    os.system('cls' if os.name == 'nt' else 'clear')
    intro = 'Welcome to Amitié!' + ' (Type help for a list of commands.)'
    custom_prompt = colored('Amitié ', 'cyan', attrs=[
        'bold']) + colored('-->', 'grey', attrs=['bold', 'blink'])
    prompt = custom_prompt
    file = None

    @classmethod
    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""

        room_type = arg['<room_type>']
        room_name = arg['<room_name>']
        print(amity.create_room(room_type, room_name))

    @classmethod
    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <role> [<accomodation>]"""

        first_name = arg['<first_name>']
        last_name = arg['<last_name>']
        role = arg['<role>']
        if not arg['<accomodation>']:
            arg['<accomodation>'] = 'N'
        else:
            accomodation = arg['<accomodation>']

        print(amity.add_person(first_name, last_name, role, accomodation))

    @classmethod
    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <emp_id> <room_name>"""

        emp_id = arg['<emp_id>']
        room_name = arg['<room_name>']
        print(amity.reallocate_person(emp_id, room_name))

    @classmethod
    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <file_name>"""

        file_name = arg['<file_name>']
        print(amity.load_people(file_name))

    @classmethod
    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--o=file_name]"""
        if arg['--o']:
            file_name = arg['--o']
            print(amity.print_allocations(filename=file_name))
        else:
            print(amity.print_allocations())

    @classmethod
    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: unallocated [--o=file_name]"""

        if arg['--o']:
            file_name = arg['--o']
            print(amity.print_unallocated(filename=file_name))
        else:
            print(amity.print_unallocated())

    @classmethod
    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""

        room_name = arg['<room_name>']
        print(amity.print_room(room_name))

    @classmethod
    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--db=sqlite_database]"""

        if arg['--db']:
            sqlite_database = arg['--db']
            print(amity.save_state(db_name=sqlite_database))
        else:
            print(amity.save_state())

    @classmethod
    @docopt_cmd
    def do_get_id(self, arg):
        """Usage: get_person_id <f_name> <l_name>"""

        f_name = arg['<f_name>']
        l_name = arg['<l_name>']
        print(amity.get_person_id(f_name, l_name))

    @classmethod
    @docopt_cmd
    def do_delete_person(self, arg):
        """Usage: delete_person <person_id>"""

        employee = arg['<person_id>']
        print(amity.delete_person(employee))

    @classmethod
    @docopt_cmd
    def do_delete_room(self, arg):
        """Usage: delete_rooom <room_name>"""

        selected_room = arg['<room_name>']
        print(amity.delete_room(selected_room))

    @classmethod
    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state <db_name>"""

        db_name = arg['<db_name>']
        print(amity.load_state(db_name))

    @classmethod
    @docopt_cmd
    def do_list_people(self, arg):
        """Usage: list_people"""

        print(amity.list_people())

    @classmethod
    @docopt_cmd
    def do_list_rooms(self, arg):
        """Usage: list_rooms"""

        print(amity.list_rooms())

    @classmethod
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
