# -*- coding: utf-8 -*-

"""Run this script with either :code:`python3 -m bio2bel_ncbitaxon deploy`"""

from __future__ import print_function

import logging
import sys

import click

from pybel_tools.ols_utils import OlsConstrainedNamespaceOntology
from .run import MODULE_DOMAIN, MODULE_FUNCTIONS, MODULE_NAME, MODULE_ROOT

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


@click.group()
def main():
    """NCBI Taxonomy Tree to BEL"""


@main.command()
@click.option('-b', '--ols-base', help="Custom OLS base url")
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout)
def write(ols_base, output):
    """Writes BEL annotation file"""
    ontology = OlsConstrainedNamespaceOntology(
        ontology=MODULE_NAME,
        namespace_domain=MODULE_DOMAIN,
        bel_function=MODULE_FUNCTIONS,
        base_term_iri=MODULE_ROOT,
        ols_base=ols_base
    )

    log.info('Starting to download NCBI Taxon from OLS at %s', ontology.ols_client.base)

    ontology.write_annotation(output)


@main.command()
@click.option('-b', '--ols-base', help="Custom OLS base url")
@click.option('--no-hash-check', is_flag=True)
def deploy(ols_base=None, no_hash_check=False):
    """Deploy BEL annotation file to Artifactory"""
    ontology = OlsConstrainedNamespaceOntology(
        ontology=MODULE_NAME,
        namespace_domain=MODULE_DOMAIN,
        bel_function=MODULE_FUNCTIONS,
        base_term_iri=MODULE_ROOT,
        ols_base=ols_base
    )
    success = ontology.deploy_annotation(hash_check=(not no_hash_check))
    click.echo('Deployed to {}'.format(success) if success else 'Duplicate not deployed')


if __name__ == '__main__':
    main()
