from sqlalchemy.orm import Session
from models import User, Transaction


def create_user(db: Session, user):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, user):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


def create_transaction(db: Session, transaction):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def get_transactions(db: Session):
    return db.query(Transaction).all()


def delete_transaction(db: Session, transaction_id: int):
    txn = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if txn:
        db.delete(txn)
        db.commit()
    return txn