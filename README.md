# 🎰 Slot Machine CLI

A command-line slot machine game built in Python — created as a **practice/learning project** to explore probability-driven randomness, grid-based game logic, and interactive terminal loops.

> 🧪 **Status:** Practice Project — built for learning purposes, simulated currency only, not a real gambling application.

---

## 📸 Preview

```
What would you like to deposit? ₹500
Current balance is ₹500.
Press enter to play ('q' to quit).
Enter the number of lines to bet on (1-3)? 3
What would you like to bet on each line? ₹50
Balance : ₹500	Lines : 3 lines.
Total bet is : ₹150.
B | C | A
D | B | D
C | D | B
You won ₹0.
You won on lines :  
Current balance is ₹350.
Press enter to play ('q' to quit).
```

*(Every spin prints a 3x3 grid of symbols, tallies up matching rows, and updates your balance live in the terminal.)*

---

## ✨ Features

| Feature | Description |
|---|---|
| 💰 **Deposit System** | Start by depositing any positive amount as your play balance |
| 📊 **Adjustable Lines** | Bet on 1 to 3 horizontal lines per spin |
| 🎯 **Bet Limits** | Enforced minimum (₹10) and maximum (₹1000) bet per line to keep play sane |
| 🎲 **Weighted Symbol Pool** | Symbols `A`, `B`, `C`, `D` appear with different frequencies and payout values, mimicking real slot machine odds |
| 🧮 **Line-by-Line Win Checking** | Checks every bet line across all columns to detect matching symbols |
| 🖨️ **Visual Grid Output** | Renders the spin result as a clean `3x3` grid separated by `|` |
| 🔁 **Play Loop** | Keep spinning until you quit (`q`) or want to check your balance |
| ✅ **Input Validation** | Every prompt (deposit, lines, bet) rejects invalid or out-of-range input and re-asks |

---

## 🛠️ How It Works

The program flows through a repeating cycle:

```
┌─────────────┐     ┌──────────────────┐     ┌────────────────┐     ┌───────────────────┐     ┌─────────────────┐
│  Deposit     │ ──▶ │  Choose Lines &   │ ──▶ │  Spin Machine  │ ──▶ │  Check Winnings    │ ──▶ │  Update Balance  │
│  (once)      │     │  Bet Amount       │     │  (random grid) │     │  (per line match)  │     │  & Loop / Quit   │
└─────────────┘     └──────────────────┘     └────────────────┘     └───────────────────┘     └─────────────────┘
```

### 1. `deposit()`
Asks the player for a starting balance. Validates that the input is a positive whole number before the game begins.

### 2. `get_num_lines()` and `get_bet()`
- `get_num_lines()` asks how many horizontal lines (1–`MAX_LINES`) the player wants to bet on.
- `get_bet()` asks how much to bet **per line**, enforcing `MIN_BET` and `MAX_BET`.
- Both loop until a valid integer within range is entered.

### 3. `spin(balance)`
- Collects the number of lines and bet per line, calculating `total_bet = lines * bet`.
- Re-prompts for a bet if the total exceeds the player's current balance — no going into debt.
- Calls `get_slot_machine_spin()` to generate the grid, then `print_slot_machine()` to display it.
- Calls `check_winnings()` to calculate the payout and returns the **net change** in balance (`winnings - total_bet`) back to `main()`.

### 4. `get_slot_machine_spin(rows, cols, symbol)`
- Builds a master list of symbols where each symbol appears according to `symbols_count` (e.g. `A` appears twice, `D` appears eight times) — this weighting is what makes rarer symbols pay out more.
- For each column, takes a **copy** of the symbol pool and randomly removes symbols one at a time (`random.choice` + `.remove()`), guaranteeing no duplicate symbol placement conflicts within that column's draw pool.
- Returns a list of columns, where each column is a list of symbols (top to bottom).

### 5. `print_slot_machine(columns)`
- Iterates row by row across all columns to print the grid in the familiar slot-machine layout, separating symbols with ` | ` and dropping the trailing separator on the last column.

### 6. `check_winnings(columns, lines, bet, values)`
- For each line (row index) the player bet on, checks whether **every column** has the same symbol in that row.
- Uses a `for...else` loop: if the inner loop completes without hitting `break` (meaning all symbols matched), the `else` block runs, adding `values[symbol] * bet` to the total winnings and recording the winning line number.
- Returns both the total winnings and the list of winning line numbers.

### 7. `main()`
- Calls `deposit()` once to set the starting balance.
- Loops: shows the current balance, lets the player press Enter to spin or `q` to quit.
- Adds the net result of each spin (which can be negative) to the running balance.
- Prints the final balance once the player quits.

---

## 📦 Requirements

- Python 3.6+
- No external dependencies — built entirely with the standard library (`random`).

---

## 🚀 Usage

```bash
python slot_machine.py
```

Then just follow the prompts:
1. Enter a deposit amount to fund your balance
2. Press Enter to spin (or `q` to quit and cash out)
3. Choose how many lines to bet on and your bet per line
4. Watch the grid spin and see if you matched a line!

---

## 🎲 Symbol Odds & Payouts

| Symbol | Count in Pool | Payout Multiplier | Rarity |
|---|---|---|---|
| A | 2 | 5x | Rarest, highest payout |
| B | 4 | 4x | Uncommon |
| C | 6 | 3x | Common |
| D | 8 | 2x | Most common, lowest payout |

This inverse relationship between frequency and payout is the same core principle real slot machines use to balance risk and reward.

---

## 🧠 What This Project Demonstrates (Learning Goals)

This project was built to practice:
- ✅ Weighted randomness using a frequency-based symbol pool instead of uniform `random.choice`
- ✅ Multi-dimensional data handling (columns of rows) without external libraries
- ✅ The `for...else` loop pattern for clean "all matched" checks
- ✅ Layered input validation loops for multiple related prompts (deposit, lines, bet)
- ✅ Structuring a stateful game loop that passes balance between functions
- ✅ Formatting terminal output to visually resemble a grid/UI

---

## ⚠️ Disclaimer

This is a **practice/educational project** simulating slot machine mechanics with fake currency for learning purposes. It does not involve real money, is not a gambling product, and has not been designed or tested for real-world wagering use.

---

## 📄 License

Free to use for learning and practice purposes.
