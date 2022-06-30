class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        self.followers = 0

    def follow(self):
        self.followers += 1

    def show_data(self):
        secret_password = ''
        for _ in self.password:
            secret_password += '*'

        print(f'{self.id} - {self.username} - {secret_password} - {self.followers}')


if __name__ == '__main__':
    user_1 = User('001', 'pedrinho_danado', '12345')
    user_1.show_data()

    for _ in range(10):
        user_1.follow()

    user_1.show_data()