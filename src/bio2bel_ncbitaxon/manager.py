# -*- coding: utf-8 -*-

from bio2bel import AbstractManager
from pytaxtree.manager.database import DbManager
from .constants import MODULE_NAME
from .models import Base, Citation, Division, GeneticCode, Name, Node

__all__ = ['Manager']


class Manager(AbstractManager, DbManager):
    """Bio2BEL Manager for NCBI TaxTree"""

    module_name = MODULE_NAME
    flask_admin_models = [Citation, Division, GeneticCode, Name, Node]

    @property
    def _base(self):
        return Base

    def count_nodes(self):
        return self._count_model(Node)

    def is_populated(self):
        return 0 < self.count_nodes()

    def populate(self):
        self.db_import()
