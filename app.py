import csv
from enum import Enum


class Actions(Enum):
    HIGHEST_PRICE = 1
    AVARAGE = 2
    IDEL_NUMBER = 3
    CHECEK_COLOR_KIND = 4


def print_menu():
    for action in Actions:
        print(f"{action.name} - {action.value}")
    return Actions(int(input("select action : ")))


class Diamond:
    def __init__(self, carat, cut, color, clarity, depth, table, price, x, y, z):
        self.carat = float(carat)
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = float(depth)
        self.table = float(table)
        self.price = int(price)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

diamonds_data = []
diamonds=[]

def read_csv(file_path):
    
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row if exists
        for row in csv_reader:
            diamonds_data.append(Diamond(*row))
    return diamonds_data

def highest(diamonds):
    temp = 0
    for diamond in diamonds:
        if diamond.price > temp:
            temp = diamond.price
    print(temp)

def average_price(diamonds):
    total_price = sum(diamond.price for diamond in diamonds)
    average = total_price / len(diamonds)
    print(average)

def count_ideal_cut(diamonds):
    ideal_count = 0
    for diamond in diamonds:
        if diamond.cut == "Ideal":
            ideal_count += 1
    print(f"Number of 'Ideal' cut diamonds: {ideal_count}")

    


def count_colors(diamonds):
    color_count = {}
    for diamond in diamonds:
        color = diamond.color
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    print("Colors and their counts:")
    for color, count in color_count.items():
        print(f"{color}: {count}")





if __name__ == "__main__":
    file_path = 'C:/Users/AMIR/Documents/testjb/data.csv'
    diamonds = read_csv(file_path)
    while True:
       user_selection= print_menu()
       if user_selection == Actions.HIGHEST_PRICE:highest(diamonds)
       if user_selection == Actions.AVARAGE:average_price(diamonds)
       if user_selection == Actions.IDEL_NUMBER:count_ideal_cut(diamonds)
       if user_selection == Actions.CHECEK_COLOR_KIND:count_colors(diamonds)


