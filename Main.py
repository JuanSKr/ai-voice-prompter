import Listener


class Main:
    def __init__(self):
        self.listener = Listener.Listener()

    def run(self):
        self.listener.voicePrompter()


if __name__ == "__main__":
    main = Main()
    main.run()
