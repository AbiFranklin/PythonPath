import requests
import click
import datetime

from pymongo import MongoClient



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
    investment_document = {
        "coin_id": coin_id,
        "currency": currency,
        "amount": amount,
        "price": price,
        "sell": sell,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    investments.insert_one(investment_document)

    action = "Sold" if sell else "Added"
    print(f"{action} {amount} of {coin_id} at {currency.upper()} price {price:.2f}.")


cli.add_command(show_coin_prices)
cli.add_command(add_investment)



@click.command()
@click.option("--coin_id", default="bitcoin")
@click.option("--currency", default="usd")
def get_investment_value(coin_id, currency):
    coin_price = get_coin_price(coin_id, currency)
    sell_result = investments.find({"coin_id": coin_id, "currency": currency, "sell": True})
    buy_result = investments.find({"coin_id": coin_id, "currency": currency, "sell": False})
    sell_amount = sum([doc["amount"] for doc in sell_result])
    buy_amount = sum([doc["amount"] for doc in buy_result])
    total_value = (buy_amount - sell_amount) * coin_price


    print(f"Total amount of {coin_id} in {currency.upper()}: {total_value:.2f}")

cli.add_command(get_investment_value)
# @click.command()
# @click.option("--csv_file")

# def import_investments(csv_fil
#     with open(csv_file, "r") as file:
#         rdr = csv.reader(file, delimiter=",")
#         rows = list(rdr)
#         sql = "INSERT INTO investments VALUES (?, ?, ?, ?, ?, ?);"
#         cursor.executemany(sql, rows)
#         database.commit()

#         print(f"Imported {len(rows)} investments from {csv_file}.")


# cli.add_command(import_investments)

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
    db = client.portfolio
    investments = db.investments
    cli()
