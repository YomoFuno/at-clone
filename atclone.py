from atclone import game

def main():
    g = game.Game()
    g.basic_setup()
    vc = game.CliViewControl(g)
    vc.jour_fix()
    vc.office()
    vc.quit_game()

if __name__ == '__main__':
    main()

