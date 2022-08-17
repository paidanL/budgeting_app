"""
This program is for all the basic budgeting calculation functions
"""

import numpy as np
import pandas as pd


class Budget():
    """A class for creating simple budgets"""

    def __init__(self, name):
        self.name = name
        self.categories_df = pd.DataFrame()
        self.subcategories = {}

        self.default_row = {"proportion": 0,
                            "budget": 0,
                            "spent": 0,
                            "difference": 0}

    def __repr__(self):
        return self.name

    def __str__(self):

        # Need to automate col_width so that it is just the longest entry + 1
        col_width = {"categories": 15,
                     "proportion": 12,
                     "budget": 10,
                     "spent": 10,
                     "difference": 12}

        table_width = sum(col_width.values())
        cols = col_width.keys()

        table = (f"{''.center(table_width + 1, '-')}\n" +
                 f"{self.name.center(table_width)}|\n")

        for key, val in col_width.items():
            if key == "categories":
                table += f"{''.center(val)}"
                continue

            table += f"{key.center(val)}"

        table += f"|\n{''.center(table_width + 1, '-')}"

        for cat, row in self.categories.items():
            table += f"\n{cat.ljust(col_width['categories'])}|"

            for col, val in row.items():
                table += f"{str(val).rjust(col_width[col] - 1)}|"

        table += f"\n{''.center(table_width + 1, '-')}"

        return table

    def setCategories(self, categories=None):
        if categories is None:
            categories = input("Enter the categories you want to budget for " +
                               "in a comma separated form (category1, category2, ...)\n")

        self.categories = self.categories.fromkeys(
            categories.split(', '),
            self.default_row)

    def addCategories(self, categories=None):
        if categories is None:
            categories = input("Enter additional categories to add to your budget " +
                               "in a comma separated form (category1, category2, ...)\n")

            categories = list(categories.split(', '))

        for cat in categories:
            self.categories.setdefault(cat, self.default_row)


if __name__ == "__main__":

    my_budget = Budget('test')
    my_budget.setCategories("savings, expenses, charity")
    print(my_budget)
