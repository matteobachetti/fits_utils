#!/usr/bin/env python
from __future__ import print_function, division, unicode_literals
import os
import errno
from astropy.io import fits
import sys


def force_link(file1, file2):
    try:
        os.link(file1, file2)
    except OSError as e:
        if e.errno == errno.EEXIST:
            os.remove(file2)
            os.link(file1, file2)


def main(args=None):
    if args is None:
        sys.exit("copy_spectra input_file.ext outroot")
    fname = args[1]
    outroot = args[2]

    dirname, basename = os.path.split(fname)

    paths_to_modify = ['BACKFILE', 'RESPFILE', 'ANCRFILE']
    suffixes = {'BACKFILE': '_back', 'RESPFILE': '', 'ANCRFILE': ''}

    hdulist = fits.open(fname)

    for p in paths_to_modify:
        name = hdulist[1].header[p]
        complete_name = os.path.join(dirname, name)

        base, extension = os.path.splitext(name)

        newname = outroot + suffixes[p] + extension
        force_link(complete_name, newname)

        hdulist[1].header[p] = newname

    base, extension = os.path.splitext(basename)
    hdulist.writeto(outroot + extension, clobber=True)
