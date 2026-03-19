
MAX_LINES=3
MAX_BET=1000
MIN_BET=10

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
        bet_amount=input("What would you like to deposit? ₹")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if bet_amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return bet_amount



def main():
    balance = deposit()
    lines=get_num_lines()
    print(f"Balance : ₹{balance}\tLines : {lines}")
main()