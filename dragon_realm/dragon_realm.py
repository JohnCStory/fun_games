from resources import display_intro, choose_cave, check_cave

play_again = 'yes'

while play_again == 'yes' or play_again == 'y':
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    print('Do you want to play again? (yes or no)')
    play_again = input()