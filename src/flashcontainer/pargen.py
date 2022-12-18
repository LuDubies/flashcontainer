# BSD 3-Clause License
#
# Copyright (c) 2022, Haju Schulz (haju.schulz@online.de)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

__version__ = "0.0.4"

from flashcontainer.hexwriter import HexWriter
from flashcontainer.xmlparser import XmlParser
from flashcontainer.cfilewriter import CFileWriter
from flashcontainer.gnuldwriter import GnuLdWriter
from flashcontainer.pyhexdumpwriter import PyHexDumpWriter

import datetime
import argparse
import logging
import uuid
import sys
import os
from pathlib import Path

# List of output writers
_WRITER = [
    {"key": "ihex", "class": HexWriter, "help": "Generate intelhex file"},
    {"key": "csrc", "class": CFileWriter, "help": "Generate c/c++ header and source files"},
    {"key": "gld", "class": GnuLdWriter, "help": "Generate GNU linker include file for parameter symbol generation."},
    {"key": "dump", "class": PyHexDumpWriter, "help": "Generate pyHexDump print configuration file."}
]


def pargen() -> int:
    """ Parameter generator tool entry point"""

    logging.basicConfig(encoding='utf-8', level=logging.WARN)

    about = 'A tool for generating flashable parameter container.'
    name = "pargen"

    parser = argparse.ArgumentParser(prog=name, description=about)

    for writer in _WRITER:
        parser.add_argument("--" + writer["key"], action='store_true', help=writer["help"])

    parser.add_argument(
        '--destdir', '-o', nargs=1,
        help='Specify output directory for generated files', default=str(Path.cwd()))
    parser.add_argument(
        '--filename', '-f', nargs=1,
        help='Set basename for generated files.')

    parser.add_argument('file', nargs=1, help='XML parameter definition file')

    args = parser.parse_args()

    print(f"{name} {__version__}: {about}")
    print("copyright (c) 2022 haju.schulz@online.de\n")

    # Create output directory (if necessary)
    destdir = Path.resolve(Path(args.destdir[0]))
    destdir.mkdir(parents=True, exist_ok=True)

    outfilename = args.filename
    if (outfilename is None):
        outfilename = os.path.basename(args.file[0])
    outfilename = Path(outfilename).stem

    model = XmlParser.from_file(args.file[0])

    # writer context options
    param = {
        "PNAME": name,
        "VERSION": __version__,
        "INPUT": args.file[0],
        "GUID": uuid.uuid4(),
        "CMDLINE": ' '.join(sys.argv[0:]),
        "DATETIME": datetime.datetime.now(),
        "MODEL": model,
        "DESTDIR": destdir,
        "BASENAME": outfilename
        }

    if model.validate(param) is False:
        sys.exit(2)

    for writer in _WRITER:
        if getattr(args, writer["key"]):
            writer["class"](model, param).run()


if __name__ == "__main__":
    try:
        pargen()
        print("Done.")
        sys.exit(0)

    except Exception as exc:
        logging.exception(exc)
        sys.exit(1)
