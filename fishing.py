import socket
import argparse


class FishingIp:

    def __init__(self, sum_choice):
        """определяем обьекты и домены"""
        self.sum_choice = sum_choice
        self.host_name_one = ['group-iba', 'group-ibb', 'group-ibc']
        self.host_name_two = ['gr0up-iba', 'group-1ba', 'gr0up-1ba']
        self.host_name_three = ['group-i.b', 'grou.p-ib', 'gro.up-iba', 'gr.oup-iba', 'g.roup-ib']
        self.host_name_four = ['group-i', 'group-b', 'groupib', 'grou-ib']
        self.host_domen = ['.com', '.ru', '.net', '.org', '.info', '.cn', '.es', '.top', '.au', '.pl', '.it', '.uk',
                           '.tk', '.ml', '.ga', '.cf', '.us', '.xyz', '.top', '.site', '.win', '.bid']

    def get_host_ip(self, get_name):
        """посылаем/получаем запросы/ответы"""
        for dom in self.host_domen:
            for name in get_name:
                try:
                    sock = socket.gethostbyname(name + dom)
                    print(sock)
                except:
                    print(f'No domain name {name + dom}')

    def choice(self):
        if self.sum_choice == '1':
            return self.get_host_ip(self.host_name_one)
        elif self.sum_choice == '2':
            return self.get_host_ip(self.host_name_two)
        elif self.sum_choice == '3':
            return self.get_host_ip(self.host_name_three)
        else:
            return self.get_host_ip(self.host_name_four)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='выбор проверки\nДля вызова помощи:-h')
    parser.add_argument('-one', type=str, help='spec target change one letter')
    parser.add_argument('-two', type=str, help='spec target host')
    parser.add_argument('-three', type=str, help='spec target host')
    parser.add_argument('-four', type=str, help='spec target host')
    args = parser.parse_args('-two  2'.split())
    scan = FishingIp(args)
    scan.choice()

