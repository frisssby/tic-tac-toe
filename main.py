from Game_class import Game


def user_input():
    print('Привет! Укажи размер поля n - одно число от 3 до 10.')
    n = input()
    while not n.isdigit() or int(n) < 3 or int(n) > 10:
        print('Размер поля должен быть целым числом от 3 до 10. Попробуй еще раз.')
        n = input()
    n = int(n)
    print('Сколько знаков подряд нужно поставить, чтобы победить?')
    k = input()
    while not k.isdigit() or int(k) > n or int(k) < 2:
        print('Количество знаков должно быть целым числом не меньшим 2 и не большим, чем размер поля. '
              'Попробуй еще раз.')
        k = input()
    k = int(k)
    print('Выбери режим игры:\n1) Сам с собой\n2) Против стратегии\n3) Стратегия против стратегии'
          '\n Введи номер режима - одну цифру:')
    mode = input()
    while not mode.isdigit() or int(mode) < 1 or int(mode) > 3:
        print('Попробуй еще раз. '
              'Выбери режим игры:\n1) Сам с собой\n2) Против стратегии\n3) Стратегия против стратегии'
              '\n Введи номер режима - одну цифру:')
        mode = input()
    mode = int(mode)
    # print('Удачной игры!')
    return ([n, k, mode])


def _play():
    game = Game(user_input())
    while not game.is_terminal():
        game.print_field()
        game.next_move()
    print('Игра окончена!')


if __name__ == '__main__':
    _play()
