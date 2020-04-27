from subprocess import check_output


def print_contest_if_cwd():
    return check_output(['ls']).split()


print(print_contest_if_cwd())




