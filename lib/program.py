from db.config import Session
from prompts.day_input import day_input
from prompts.select_days import select_days
from prompts.check_day_adjacency import check_day_adjacency

def run_program():
    print("Welcome to your workout planner!")
    number = day_input()
    print(number)
    days = select_days(number)
    print(days)
    check_day_adjacency(days)
    