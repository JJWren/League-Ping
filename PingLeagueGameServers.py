from pythonping import ping
from datetime import date

VERSION = '1.21.11.0'

league_game_servers = {'BR': '104.160.152.3', 'EUNE': '104.160.142.3', 'EUW': '104.160.141.3',
                       'LAN': '104.160.136.3', 'NA': '104.160.131.3', 'OCE': '104.160.156.1', 'RU': '162.249.73.2'}


def ping_single_game_server(server_key: str):
    print(
        f'\nPinging {server_key} game server [{league_game_servers[server_key]}]...')
    ping(league_game_servers[server_key], timeout=4, verbose=True)


def ping_all_game_servers():
    for key in league_game_servers:
        ping_single_game_server(key)


if __name__ == '__main__':
    def get_good_input(input_message: str, input_options: dict):
        user_input = ''
        while user_input not in input_options:
            user_input = input(input_message)
            if user_input not in input_options:
                print('Please choose a valid option...')
        return user_input

    def pause_sys():
        try:
            input('\nPress "ENTER" to continue...')
        except SyntaxError:
            pass

    print('Welcome to League Ping - The premiere League of Legends ping automation tool!')
    print(f'Author: Joshua Wren')
    print(f'Version: {VERSION}')
    print(f'Current Date/Time: {date.today().strftime("%B %d, %Y")}')
    try:
        ping_choice = get_good_input(
            '\nSelect "1" for pinging 1 server, "2" for all servers: ', {'1': 1, '2': 2})
        if ping_choice == '2':
            ping_all_game_servers()
        else:
            select_server_input = get_good_input(
                f'\nSelect from the following options:\nServer Options: {list(league_game_servers.keys())}\t', league_game_servers)
            ping_single_game_server(select_server_input)

    except Exception as e:
        print(
            f'An error occurred during user server selection.\n\tDetails: {e}')

    pause_sys()
