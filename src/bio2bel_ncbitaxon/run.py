# -*- coding: utf-8 -*-

from pybel_tools.ols_utils import OlsConstrainedNamespaceOntology

__all__ = [
    'MODULE_NAME',
    'MODULE_ROOT',
    'ontology',
]

MODULE_NAME = 'ncbitaxon'
MODULE_ROOT = 'http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCBITaxon_131567'
MODULE_DOMAIN = False
MODULE_FUNCTIONS = False

ontology = OlsConstrainedNamespaceOntology(
    ontology=MODULE_NAME,
    namespace_domain=MODULE_DOMAIN,
    base_term_iri=MODULE_ROOT,
    bel_function=MODULE_FUNCTIONS,
)
