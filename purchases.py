"""
This file contains all the required methods for tracking purchase history
"""

from datetime import date
import numpy as np
import pandas as pd
import sqlite3


def add_purchase(
        purchase_date,
        amount,
        category,
        merchant,
        location,
        description,
        sub_category=None
):
    '''Add a row to the purchases table'''

    conn = sqlite3.connect('budget.db')
    c = conn.cursor()

    c.execute(
        '''
        INSERT INTO purchases 
        VALUES(
            :purchase_date,
            :amount,
            :category,
            :sub_category,
            :merchant,
            :location,
            :description
        )  
        ''',
        {
            'purchase_date': purchase_date,
            'amount': amount,
            'category': category,
            'sub_category': sub_category,
            'merchant': merchant,
            'location': location,
            'description': description
        }
    )

    conn.commit()
    conn.close()


def show_purchases(start_date='1970-01-01', end_date=date.today()):
    '''
    Shows all the purchases contained in the purchases table

    start_date: the date to start filtering purchases by
    end_date: the date to end filtering purchases by
    '''

    conn = sqlite3.connect('budget.db')
    c = conn.cursor()

    c.execute(
        '''
          SELECT rowid, * FROM purchases
          WHERE purchase_date BETWEEN :start AND :end
        ''',
        {
            'start': start_date,
            'end': end_date
        }
    )

    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    conn = sqlite3.connect('budget.db')
    c = conn.cursor()

    # c.execute('DROP TABLE purchases')
    # c.execute(
    #     '''
    #     CREATE TABLE purchases (
    #         purchase_date DATE NOT NULL,
    #         amount INT,
    #         category VARCHAR(255),
    #         sub_category VARCHAR(255),
    #         merchant VARCHAR(255),
    #         location VARCHAR(255),
    #         description VARCHAR(255)
    #         )
    #     '''
    # )
    conn.commit()
    conn.close()

    add_purchase(
        '2022-01-02',
        420.69,
        'shopping',
        'test',
        'noblesville, IN',
        'testing database',
        'test test'
    )

    show_purchases()
