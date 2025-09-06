def main():
    general = General()
    num_of_row_col = general._first_level
    maze = ellers(num_of_row_col)
    print(maze)



class General():
    def __init__(self, first_level, second_level, third_level):
        self._first_level = 5
        self._second_level = 50
        self._third_level = 500

def ellers(num_of_row_col):
    frst_row = " _" * num_of_row_col + " "
    return frst_row


if __name__ == "__main__":
    main()  




# Working idea
# Need to make { } with [ ] in it.
# Every [ ] has 1 row of the maze.


# Class General() for general variables