import logic as lg
import logic_2 as lg2
# Driver code
if __name__ == '__main__':
    # calling start_game function
    # to initialize the matrix
    mat = lg.start_game()
    # pass the matrix in commands function !!
    lg2.commands_game(mat)


