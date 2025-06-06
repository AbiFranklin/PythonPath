from sqlalchemy import String, Numeric, create_engine, select, Text, ForeignKey, join
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

class Base(DeclarativeBase):
    pass

class Investment(Base):
    __tablename__ = 'investment'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5,2))
    portfolio_id: Mapped[int] = mapped_column(ForeignKey('portfolio.id'))
    portfolio: Mapped["Portfolio"] = relationship(back_populates='investments')
    
    def __repr__(self):
        return f"<Investment(coin={self.coin}, currency={self.currency}, amount={self.amount})>"

class Portfolio(Base):
    __tablename__ = 'portfolio'
    
    id: Mapped[int] = mapped_column(primary_key=True) 
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text())
    investments: Mapped[list["Investment"]] = relationship(back_populates='portfolio')

    __repr__ = lambda self: f"<Portfolio(name={self.name}, description={self.description})>"

engine = create_engine('sqlite:///data_r.db')
Base.metadata.create_all(engine)

bitcoin = Investment(coin='bitcoin', currency='USD', amount=1000.00)
ethereum = Investment(coin='ethereum', currency='GBP', amount=2000.00)
dogecoin = Investment(coin='dogecoin', currency='EUR', amount=500.00)

portfolio = Portfolio(name='Crypto Portfolio', description='A portfolio for cryptocurrency investments')
bitcoin.portfolio = portfolio

otherPortfolio = Portfolio(name='Other Portfolio', description='A portfolio for other investments')

otherPortfolio.investments.extend([ethereum, dogecoin])

with Session(engine) as session:
    session.add_all([bitcoin, ethereum, dogecoin])
    session.commit()
    # stmt = select(Investment).join(Portfolio).where(Investment.coin == 'bitcoin')
    subq = select(Investment).where(Investment.coin == 'bitcoin').subquery()
    stmt = select(Portfolio).join(subq, Portfolio.id == subq.c.portfolio_id)

    for investment in session.execute(stmt).all():
        print(f"{investment} in {portfolio}")

