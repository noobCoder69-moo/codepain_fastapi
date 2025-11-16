import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import psycopg2

load_dotenv()

SQLALCHEMY_DB_URL = os.getenv("DATABASE_URL")

# SQLAlchemy engine with SSL
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"sslmode": "require"})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# Direct psycopg2 test
try:
    conn = psycopg2.connect(SQLALCHEMY_DB_URL, sslmode="require")
    print("✅ Connected to Postgres!")
    conn.close()
except Exception as e:
    print("❌ Could not connect:", e)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
