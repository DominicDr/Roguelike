def get_board_from_file(file_name):

    with open(file_name, "r") as file:
        board = file.read().splitlines()

    list_of_lists = []
    for row in board:
        splitted_score = row.split(",")
        for i in range(len(splitted_score)):
            splitted_score[i] = int(splitted_score[i])
        list_of_lists.append(splitted_score)
    
    return list_of_lists

def write_board_to_file(file_name, board):
 
    with open(file_name, "w") as export_file:
        export_file.write

    with open(file_name, "a") as export_file:
        for row in board:
            for i in range(len(row)):
                row[i] = str(row[i])
            row = ",".join(row)
            export_file.write(row + "\n")

def get_hint_from_file(file_name="hints.txt"):

    with open(file_name, "r") as file:
        all_hints = file.read().splitlines()

    return all_hints
