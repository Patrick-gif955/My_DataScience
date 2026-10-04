# Bank Account Simulator

A simple Python bank account program using **OOP**, **JSON**, and **file handling**.

Account data (name, balance, interest rate) is stored in `account.json` so the balance persists between runs.

## Features
- Deposit money (rejects $0 or less)
- Withdraw money (checks for insufficient funds)
- Apply interest
- Saves balance after every transaction

## Concepts Used
- OOP (classes & inheritance)
- JSON (`json.load` / `json.dump`)
- File handling

## Classes
**BankAccount**
- `add_money()` – Deposit funds
- `withdraw_money()` – Withdraw funds

**Interest** (inherits from BankAccount)
- `add_interest()` – Adds interest based on the stored rate

**save_balance()** – Writes the updated account data to `account.json`

##Run Code
https://onlinegdb.com/Jy2WTScPj