# -*- coding: utf-8 -*-
import argparse
from datetime import datetime
from common import config
from importlib import import_module # modules from "sites" folder.

if __name__ == '__main__':
    start = datetime.now()
    print("\n ### FAST SCRAPING ###\n")

    parser = argparse.ArgumentParser()
    site_choices = list(config()['sites'].keys()) #-> sites from config.yaml.

    # Terminal arguments:
    parser.add_argument('--c', help='País para Scrapear', type=str)
    parser.add_argument('site', help='Available sites',
                        type=str, choices=site_choices)

    args = parser.parse_args()
    site_country = args.c
    site = args.site

    MODULE_NAME = 'sites.' + site.lower()

    try:
        module = import_module(MODULE_NAME)
        SiteClass = getattr(module, site)
        SiteClass(site, site_country)
    except ModuleNotFoundError as exc:
        print(exc)
        print(f"The file must be called: \"{site.lower()}.py\"")

    end = datetime.now()

    print('Time elapsed:', end - start)