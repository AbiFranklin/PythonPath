from dataclasses import dataclass
import click
import psycopg2
import psycopg2.extras
import csv

@dataclass
class Investment:
    id: int
    coin: str
    currency: str
    amount: float

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="testdb",
        user="postgres",
        password="1234"
    )

@click.group()
def cli():
    pass

@cli.command()  
@click.option('--coin', prompt=True)
@click.option('--currency', prompt=True)
@click.option('--amount', prompt=True, type=float)
def new_investment(coin, currency, amount):
    stmt = """
    INSERT INTO investment (coin, currency, amount) VALUES (%s, %s, %s);
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(stmt, (coin.lower(), currency.lower(), amount))
    connection.commit()
    cursor.close()
    connection.close()
    click.echo(f"New investment: {coin} in {currency} for {amount}")

@cli.command()  
@click.option("--filename", prompt=True)
def import_investments(filename):
    stmt = "INSERT INTO investment (coin, currency, amount) VALUES %s;"
    connection = get_connection()
    cursor = connection.cursor()

    with open(filename, "r") as file:
        coin_reader = csv.reader(file)
        rows = [[x.lower() for x in row[1:]] for row in coin_reader]
    psycopg2.extras.execute_values(cursor, stmt, rows)
    connection.commit()
    cursor.close()
    connection.close()
    click.echo(f"Importing investments from {filename}")

@cli.command()
def view_investments():
    stmt = "SELECT * FROM investment;"
    connection = get_connection()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(stmt)
    data = [Investment(**dict(row)) for row in cursor.fetchall()]
    cursor.close()
    connection.close()

    for investment in data:
        click.echo(f"Coin: {investment.coin}, Currency: {investment.currency}, Amount: {investment.amount}")    

if __name__ == "__main__":
    cli()
