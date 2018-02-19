# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from bio2bel.utils import get_connection
from pytaxtree.manager.database import DbManager
from .constants import MODULE_NAME


class Manager(DbManager):
    def __init__(self, connection=None, echo=False):
        self.connection = get_connection(MODULE_NAME, connection=connection)
        self.engine = create_engine(self.connection, echo=echo)
        self.session_maker = sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)
        self.session = scoped_session(self.session_maker)

    def populate(self):
        self.db_import()

    @staticmethod
    def ensure(connection=None):
        """
        :param connection: A connection string, a manager, or none to use the default manager
        :type connection: Optional[str or Manager]
        :rtype: Manager
        """
        if connection is None or isinstance(connection, str):
            return Manager(connection=connection)
        return connection
