# -*- coding: utf-8 -*-

from pybel_tools.ols_utils import OlsConstrainedAnnotationOntology

__all__ = [
    'MODULE_NAME',
    'MODULE_ROOT',
    'ontology',
]

MODULE_NAME = 'ncbitaxon'
MODULE_ROOT = 'http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCBITaxon_131567'
MODULE_DOMAIN = False
MODULE_FUNCTIONS = False

ontology = OlsConstrainedAnnotationOntology(
    ontology=MODULE_NAME,
    base_term_iri=MODULE_ROOT,
)
