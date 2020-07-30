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
    url = "https://public-installer-pkg.s3.us-east-2.amazonaws.com/coderrect-linux-0.6.0.tar.gz"

    maintainers = ['coderrect']

    version('0.6.0', '40e74eca3fe096b05250c871de6dd273')
    
    def setup_run_environment(self, env):
        env.set('CODERRECT_HOME', self.prefix)
    
    def install(self, spec, prefix):
        install_tree('.', prefix)
