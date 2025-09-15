from general_archive import General

def main():
    general = General()
    num_of_row_col = general._first_level
    maze = ellers(num_of_row_col)
    print(maze)

def ellers(num_of_row_col):
    maze = {}
    one_row = []
    second_row = []
    
    frst_row = " _" * num_of_row_col + " "


    
    return frst_row


if __name__ == "__main__":
    main()  




# Working idea
# Need to make { } with [ ] in it.
# Every [ ] has 1 row of the maze.


# Class General() for general variables