import os
import re
from multiprocessing import Pool

processes = []
config = open('config.txt')
react_app_name = 'coolreactapp'


def get_react_app_name():
    global react_app_name
    for line in config:
        if line.startswith('react_app_name'):
            react_app_name = line.split('=')[1][:-1]


def handle_config():
    for line in config:
        if line.startswith('create_react_app'):
            value = line.split('=')[1][:-1]

            if value == '1':
                processes.append('createReactApp.py')
            elif value != '0':
                print(f'"{value}" не является допустимым значением параметра create_react_app.')


def run_process(process):
    os.system('python {}'.format(process))


def generate_app():
    handle_config()

    with Pool(2) as pool:
        pool.map(run_process, processes)


def add_request(function_name, request_type, url):

    f = open('requestTemplate.txt', 'r')
    text = f.read()

    result = re.findall(r'{{ \w+ }}', text)
    sub_result = re.sub(result[0], function_name, text)
    sub_result1 = re.sub(result[1], request_type, sub_result)
    sub_result2 = re.sub(result[2], url, sub_result1)

    if len(react_app_name) < 1:
        get_react_app_name()

    file_object = open(f'{react_app_name}/src/api.js', 'a')
    file_object.write(sub_result2)
    file_object.close()

    f.close()


if __name__ == "__main__":
    while True:
        print(os.getcwd() + '>', end='')
        user_input = input()
        input_parts = user_input.split(' ')
        command = input_parts[0]

        if command == 'generate_app':
            generate_app()
        elif command == 'add_request':
            add_request()
        else:
            print(f'"{command}" не является поддерживаемой коммандой.')
