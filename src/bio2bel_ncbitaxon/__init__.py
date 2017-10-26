# -*- coding: utf-8 -*-

from . import cli
from . import run
from .run import *

__all__ = run.__all__

__version__ = '0.0.1-dev'

__title__ = 'bio2bel_ncbitaxon'
__description__ = "A package for converting the NCBI Taxonomxy Tree to BEL"
__url__ = 'https://github.com/bio2bel/ncbitaxon'

__author__ = 'Charles Tapley Hoyt'
__email__ = 'charles.hoyt@scai.fraunhofer.de'

__license__ = 'Apache 2.0 License'
__copyright__ = 'Copyright (c) 2017 Charles Tapley Hoyt'
