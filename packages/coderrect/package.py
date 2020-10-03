# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
from spack import *

class Coderrect(Package):
    """A fast detector for C/C++ multi-threaded bugs"""
    
    homepage = "https://coderrect.com/"
    url = "https://public-installer-pkg.s3.us-east-2.amazonaws.com/coderrect-linux-0.8.0.tar.gz"

    maintainers = ['coderrect']

    version('0.8.0', sha256='b320c4e7b232a29a64b203f096f94af8cdc1291d91c1f694d0ea7344cac97d25')
    
    def install(self, spec, prefix):
        install_tree('.', prefix)
