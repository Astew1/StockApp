import gui as gui
import api as api
import time
import tkinter as tk


def main():
    symbols = ["FB", "AAPL", "TSLA", "AGIO"]
    while True:
        for sym in symbols:
            p = api.getPrice(sym)
            print("{}: {} | ".format(sym, p), end='')
        print()
        time.sleep(1)




if __name__ == '__main__':
    main()
