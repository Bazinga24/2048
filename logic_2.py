import logic as lg


def commands_game(mat):
    while True:

        # taking the user input
        # for next step
        x = input("Press the command : ")

        # we have to move up
        if x == 'W' or x == 'w':

            # call the move_up function
            mat, flag = lg.move_up(mat)

            # get the current state and print it
            status = lg.get_current_state(mat)
            print(status)

            # if game not ove then continue
            # and add a new two
            if status == 'GAME NOT OVER':
                lg.add_new_2(mat)

            # else break the loop
            else:
                break

        # the above process will be followed
        # in case of each type of move
        # below

        # to move down
        elif x == 'S' or x == 's':
            mat, flag = lg.move_down(mat)
            status = lg.get_current_state(mat)
            print(status)
            if status == 'GAME NOT OVER':
                lg.add_new_2(mat)
            else:
                break

        # to move left
        elif x == 'A' or x == 'a':
            mat, flag = lg.move_left(mat)
            status = lg.get_current_state(mat)
            print(status)
            if status == 'GAME NOT OVER':
                lg.add_new_2(mat)
            else:
                break

        # to move right
        elif x == 'D' or x == 'd':
            mat, flag = lg.move_right(mat)
            status = lg.get_current_state(mat)
            print(status)
            if status == 'GAME NOT OVER':
                lg.add_new_2(mat)
            else:
                break
        else:
            print("Invalid Key Pressed")

        # print the matrix after each
        # move.
        print(mat)
