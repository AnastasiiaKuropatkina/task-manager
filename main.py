from tasks.cli import handle_action, handle_interapt


def main():
    while True:
        try:
            handle_action()
        except KeyboardInterrupt:
            if handle_interapt():
                break

# name назва модуля яка інпортується from main import main
if __name__ == '__main__':
    main()