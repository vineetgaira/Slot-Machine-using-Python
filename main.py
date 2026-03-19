import random

MAX_LINES=3
MAX_BET=1000
MIN_BET=10

ROWS=3
COLS=3

symbols_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get_slot_machine_spin(rows, cols, symbol):
    all_symbols = []
    for symbol,symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1 :
                print(column[row], end=" | ")
            else:
                print(column[row],end="")
            
        print()



def deposit():
    while True:
        amount=input("What would you like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_num_lines():
    while True:
        lines=input("Enter the number of lines to bet on (1-"+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print(f"Enter a valid number of lines between 1-{MAX_LINES}.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():

    while True:
        bet_amount=input("What would you like to bet on each line? ₹")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET} - ₹{MAX_BET}")
        else:
            print("Please enter a valid amount.")
    return bet_amount


def main():
    balance = deposit()
    lines=get_num_lines()
    while True:
        bet=get_bet()
        total_bet=lines*bet

        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount, Your current balance is ₹{balance}.")
        else:
            break
    print(f"Balance : ₹{balance}\tLines : {lines} lines.\nTotal bet is : ₹{total_bet}." )

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    
main()