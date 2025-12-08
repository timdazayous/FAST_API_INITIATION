# backend/modules/df_tools.py
from loguru import logger 
import pandas as pd
import os 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, session


DB_FILE_PATH = os.path.join("backend","data", "quotes_db.sql")
engine = create_engine(f"sqlite:///{DB_FILE_PATH}", echo=False)
session_locale = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class Quote(Base):
    __tablename__ = "Quote"
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)


#CSV_FILE_PATH = os.path.join("backend","data", "quotes_db.csv")

def write_db(df: pd.DataFrame):
    #df.to_csv(CSV_FILE_PATH, index=True, index_label='id')

def read_db()->pd.DataFrame:
    # df = pd.read_csv(CSV_FILE_PATH, index_col='id')

    # if df.isnull().any().any():
    #     # raise ValueError("Le CSV contient des valeurs nulles")
    #     df_clean = df.dropna()
    # for r, c in df.iterrows():
    #     print(c.text.isempty)

    return df

def initialize_db():
    # if os.path.exists(CSV_FILE_PATH):
    #     logger.info("La base de données existe")
    # else:
    #     logger.info(f"impossible de trouver le fichier {CSV_FILE_PATH}")
    #     df = pd.DataFrame(columns=['id', 'text'])
    #     df = df.set_index('id')
    #     write_db(df)
    #     logger.info(f"le fichier {CSV_FILE_PATH} a été créé")

    if os.path.exists(DB_FILE_PATH):
        logger.info("La base de données existe déjà")
    else:
        Base.metadata.create_all(bind=engine) 
        logger.info(f"Base de données SQL {DB_FILE_PATH} créée")