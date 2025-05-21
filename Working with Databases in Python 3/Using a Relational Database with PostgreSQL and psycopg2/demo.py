import psycopg2
import psycopg2.extras

from dataclasses import dataclass

@dataclass
class Investment:
    id: int
    coin: str
    currency: str
    amount: float

connection = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="1234"
)

cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

create_investment_table = """
create table investment (
    id serial primary key,
    coin varchar(32),
    currency varchar(3),
    amount real
    )
"""

add_bitcoin_investment = """
insert into investment (
    coin, currency, amount
    ) values (
        'bitcoin', 'USD', 1000
    );
"""

add_investment_template = """
INSERT INTO investment (coin, currency, amount) VALUES %s;
"""

data = [
    ('bitcoin', 'USD', 1000),
    ('ethereum', 'USD', 500),
    ('litecoin', 'USD', 200)
]

select_bitcoin_investment = "SELECT * FROM investment WHERE coin = 'bitcoin';"

# cursor.execute(create_investment_table)

# cursor.execute(add_bitcoin_investment)

# psycopg2.extras.execute_values(cursor, add_investment_template, data)

cursor.execute(select_bitcoin_investment)
data = [Investment(**dict(row)) for row in cursor.fetchall()]
print(data)

for investment in data:
    print(f"Coin: {investment.coin}, Currency: {investment.currency}, Amount: {investment.amount}")

connection.commit()
cursor.close()
connection.close()