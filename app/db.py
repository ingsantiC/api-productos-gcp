import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

# Cloud Run + Cloud SQL via Unix socket
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@/{DB_NAME}"
    f"?host=/cloudsql/{INSTANCE_CONNECTION_NAME}"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
