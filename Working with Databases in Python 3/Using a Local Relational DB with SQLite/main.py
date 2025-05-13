import requests
import click
import sqlite3
import datetime
import csv

CREATE_INVESTMENTS_SQL = """
CREATE TABLE IF NOT EXISTS investments (
    coin_id TEXT,
    currency TEXT,
    amount FLOAT,
    price FLOAT,
    sell BOOLEAN,
    date TIMESTAMP
);
"""


def get_coin_price(coin_id, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    data = requests.get(url).json()
    coin_price = data[coin_id][currency]

    if coin_id in data and currency in data[coin_id]:
        return coin_price
    else:
        raise ValueError(f"Could not retrieve price for {coin_id} in {currency}")


@click.group()
def cli():
    pass


@cli.command()
@click.option("--coin_id", default="bitcoin")
@click.option("--currency", default="usd")
def show_coin_prices(coin_id, currency):
    try:
        price = get_coin_price(coin_id, currency)
        print(f"The current price of {coin_id} in {currency.upper()} is: {price:.2f}")
    except ValueError as e:
        print(e)


@cli.command()
@click.option("--coin_id", default="bitcoin")
@click.option("--currency", default="usd")
@click.option("--amount", type=float)
@click.option("--sell", is_flag=True)
def add_investment(coin_id, currency, amount, sell):
    price = get_coin_price(coin_id, currency)  # fetch price
    sql = "INSERT INTO investments VALUES (?, ?, ?, ?, ?, ?);"
    values = (coin_id, currency, amount, price, sell, datetime.datetime.now())
    cursor.execute(sql, values)
    database.commit()

    action = "Sold" if sell else "Added"
    print(f"{action} {amount} of {coin_id} at {currency.upper()} price {price:.2f}.")


cli.add_command(show_coin_prices)
cli.add_command(add_investment)


@click.command()
@click.option("--coin_id", default="bitcoin")
@click.option("--currency", default="usd")
def get_investment_value(coin_id, currency):
    coin_price = get_coin_price(coin_id, currency)
    sql = """
    SELECT amount FROM investments WHERE coin_id=? AND currency=? AND sell=?;
    """
    buy_result = cursor.execute(sql, (coin_id, currency, False)).fetchall()
    sell_result = cursor.execute(sql, (coin_id, currency, True)).fetchall()
    sell_amount = sum([row[0] for row in sell_result])
    buy_amount = sum([row[0] for row in buy_result])
    total_value = (buy_amount - sell_amount) * coin_price


    print(f"Total amount of {coin_id} in {currency.upper()}: {total_value:.2f}")

@click.command()
@click.option("--csv_file")

def import_investments(csv_file):
    with open(csv_file, "r") as file:
        rdr = csv.reader(file, delimiter=",")
        rows = list(rdr)
        sql = "INSERT INTO investments VALUES (?, ?, ?, ?, ?, ?);"
        cursor.executemany(sql, rows)
        database.commit()

        print(f"Imported {len(rows)} investments from {csv_file}.")

cli.add_command(get_investment_value)
cli.add_command(import_investments)

if __name__ == "__main__":
    database = sqlite3.connect("portfolio.db")
    cursor = database.cursor()
    cursor.execute(CREATE_INVESTMENTS_SQL)
    cli()
