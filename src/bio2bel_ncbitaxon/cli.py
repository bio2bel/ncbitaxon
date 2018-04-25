# -*- coding: utf-8 -*-

"""Run this script with either :code:`python3 -m bio2bel_ncbitaxon deploy`"""

import logging
import sys

import click

from .manager import Manager
from .run import MODULE_NAME, MODULE_ROOT

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

main = Manager.get_cli()


@main.group()
@click.option('-b', '--ols-base', help="Custom OLS base url. Defaults to {}")
@click.pass_context
def ols(ctx, ols_base):
    """OLS Utilities"""
    from pybel_tools.ols_utils import OlsConstrainedAnnotationOntology

    ctx.obj = OlsConstrainedAnnotationOntology(
        ontology=MODULE_NAME,
        base_term_iri=MODULE_ROOT,
        ols_base=ols_base
    )


@ols.command()
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout)
@click.pass_obj
def write(ontology, output):
    """Writes BEL annotation file"""
    log.info('Starting to download NCBI Taxon from OLS at %s', ontology.ols_client._base)
    ontology.write_annotation(output)


@ols.command()
@click.option('--no-hash-check', is_flag=True)
@click.pass_obj
def deploy(ontology, no_hash_check=False):
    """Deploy BEL annotation file to Artifactory"""
    success = ontology.deploy_annotation(hash_check=(not no_hash_check))
    click.echo('Deployed to {}'.format(success) if success else 'Duplicate not deployed')


if __name__ == '__main__':
    main()
