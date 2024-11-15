import webbrowser
import argparse

# create args
parser = argparse.ArgumentParser(prog="plinker", description="opens up the pixiv links generated by the plink script")
parser.add_argument(
    "-L", "--limit",
    default=5,
    help="throttle to how many links you want opened at once")
parser.add_argument(
    "input",
    help="input file with links")
args = parser.parse_args()


# create variables
limit = args.limit
input_file = args.input
links, count = [], 0

with open(input_file) as file:
    for link in file:
        webbrowser.open_new_tab(link)
        count += 1
        if count == limit:
            pause = input("Would you like to pause? [y/N] - ")
            if pause.upper() == 'Y':
                print(f"Last link accessed: {link}")
                break
            count = 0
