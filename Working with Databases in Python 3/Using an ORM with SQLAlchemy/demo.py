from sqlalchemy import String, Numeric, create_engine, select, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

class Base(DeclarativeBase):
    pass

class Investment(Base):
    __tablename__ = 'investment'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5,2))
    portfolio_id: Mapped[int] = mapped_column(foreign_key='portfolio.id')
    portfolio: Mapped['Portfolio'] = relationship(back_populates='investments')
    
    def __repr__(self):
        return f"<Investment(coin={self.coin}, currency={self.currency}, amount={self.amount})>"
    
engine = create_engine('sqlite:///data.db')
Base.metadata.create_all(engine)

bitcoin = Investment(coin='bitcoin', currency='USD', amount=1000.00)
ethereum = Investment(coin='ethereum', currency='GBP', amount=2000.00)
dogecoin = Investment(coin='dogecoin', currency='EUR', amount=500.00)


class Portfolio(Base):
    __tablename__ = 'portfolio'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text())
    investments: Mapped[list[Investment]] = relationship(back_populates='portfolio')

    __repr__ = lambda self: f"<Portfolio(name={self.name}, description={self.description})>"

portfolio = Portfolio(name='Crypto Portfolio', description='A portfolio for cryptocurrency investments')
bitcoin.portfolio = portfolio


with Session(engine) as session:
    # session.add_all([bitcoin, ethereum, dogecoin])
    # session.commit()

    # investments = session.get
    # print("Investments in the database:", investments)

    # stmt = select(Investment).where(Investment.amount > 500)
    # results = session.execute(stmt).scalars().fetchall()
        
    # for investment in results:
    #     print(investment) 

    # bitcoin = session.get(Investment, 1)
    # bitcoin.amount = 1500.00
    # print(session.dirty)
    # session.commit()

    # dogecoin = session.get(Investment, 3)
    # session.delete(dogecoin)
    # print(session.deleted)
    session.commit()