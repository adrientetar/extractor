#!/usr/bin/env python

import sys
from distutils.core import setup

try:
    import fontTools
except:
    print("*** Warning: extractor requires FontTools, see:")
    print("    github.com/behdad/fonttools")

try:
    import ufoLib
except:
    print("*** Warning: extractor requires RoboFab, see:")
    print("    robofab.com")


setup(name="extractor",
    version="0.1",
    description="Tools for extracting data from font binaries into UFO objects.",
    author="Tal Leming",
    author_email="tal@typesupply.com",
    url="http://code.typesupply.com",
    license="MIT",
    packages=[
        "extractor",
        "extractor.formats"
    ],
    package_dir={"":"Lib"}
)
