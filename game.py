import random
import colorama 
from colorama import Fore, Style
colorama.init(autoreset=True)
from constant import MAX_LINES, MAX_BET, MIN_BET, ROWS, COLS, symbols_count, symbols_value
from utils import clear_screen

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings,winning_lines

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
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1 :
                print(Fore.LIGHTBLUE_EX + column[row], end=" | ")
            else:
                print(Fore.LIGHTBLUE_EX + column[row],end="")
            
        print()

def deposit():
    while True:
        amount=input(Fore.LIGHTCYAN_EX + "What would you like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(Fore.RED + "Amount must be greater than 0.")
        else:
            print(Fore.RED + "Please enter a number.")
    return amount

def get_num_lines():
    while True:
        lines=input(Fore.LIGHTCYAN_EX + "Enter the number of lines to bet on (1-"+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print(Fore.RED + f"Enter a valid number of lines between 1-{MAX_LINES}.")
        else:
            print(Fore.RED + "Please enter a number.")
    return lines

def get_bet():

    while True:
        bet_amount=input(Fore.LIGHTCYAN_EX + "What would you like to bet on each line? ₹")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(Fore.RED + f"Amount must be between ₹{MIN_BET} - ₹{MAX_BET}")
        else:
            print(Fore.RED + "Please enter a valid amount.")
    return bet_amount

def spin(balance):
    lines = get_num_lines()
    while True:
        bet=get_bet()
        total_bet=lines*bet

        if total_bet > balance:
            print(Fore.RED + f"You do not have enough balance to bet that amount, Your current balance is ₹{balance}.")
        else:
            break
    print(Fore.YELLOW + f"Balance : ₹{balance}\tLines : {lines} lines.\nTotal bet is : ₹{total_bet}." )

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print(Fore.GREEN + f"You won ₹{winnings}.")
    print(Fore.GREEN + f"You won on lines : ", *winning_lines)
    return winnings - total_bet 


def game():
    clear_screen()
    balance=deposit()
    while True:
        print(Fore.GREEN + f"Current balance is ₹{balance}.")
        user_answer = input(Fore.BLUE + "Press enter to play ('q' to quit).")
        if user_answer == "q":
            break
        balance += spin(balance)
    print(Fore.YELLOW + f"You left with ₹{balance}.")




    