# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from core.logger import Logger
from dotenv import load_dotenv

load_dotenv()


class DbUtils:
    def __init__(self, database_url: str = None):
        url = database_url or os.getenv("TEST_DATABASE_URL")
        if not url:
            raise ValueError("TEST_DATABASE_URL not set")

        psycopg3_url = url.replace("postgresql://", "postgresql+psycopg://")
        self.engine = create_engine(psycopg3_url)
        Logger.info("DbUtils: connected to database")

    def execute(self, query: str, params: dict = None) -> list:
        Logger.info(f"DbUtils: execute query '{query}'")
        with Session(self.engine) as session:
            result = session.execute(text(query), params or {})
            return result.fetchall()

    def fetch_one(self, query: str, params: dict = None):
        Logger.info(f"DbUtils: fetch one '{query}'")
        with Session(self.engine) as session:
            result = session.execute(text(query), params or {})
            return result.fetchone()

    def close(self):
        self.engine.dispose()
        Logger.info("DbUtils: connection closed")

    def execute_dml(self, query: str, params: dict = None) -> None:
        """Для INSERT, UPDATE, DELETE — не возвращает строки"""
        Logger.info(f"DbUtils: execute DML '{query}'")
        with Session(self.engine) as session:
            session.execute(text(query), params or {})
            session.commit()