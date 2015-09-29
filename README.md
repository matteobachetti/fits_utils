FITS handling utilities
-----------------------

Sparse collection of command line scripts to handle FITS files, in particular
X-ray observation files.

+ `copy_spectra`: copy a XSpec-compatible spectrum from one directory to
    the current, together with response and background files. Let's assume that
    we have a file called `source_sr.pha`, containing an X-ray spectrum, two
    directories above ours, together with its response and background files.
    The names of these files will be written in the RESPFILE, ANCRFILE and
    BACKFILE keywords in the header of spectrum file. This scripts reads these
    keywords and copies the relevant files in the current directory, with a
    common root name, and changes the relevant keywords in the spectrum file.


    ```
    $ ls -al
    drwxrwxr-x 2 pulsar pulsar     4096 Sep 29 12:55 .
    drwxrwxr-x 3 pulsar pulsar     4096 Sep 29 10:04 ..

    $ copy_spectra ../../source_sr.pha out
    $ ls -al
    drwxrwxr-x 2 pulsar pulsar     4096 Sep 29 12:55 .
    drwxrwxr-x 3 pulsar pulsar     4096 Sep 29 10:04 ..
    -rw-r--r-- 2 pulsar pulsar    63360 Jun 23 10:27 out.arf
    -rw-rw-r-- 1 pulsar pulsar   120960 Sep 29 11:23 out.pha
    -rw-r--r-- 2 pulsar pulsar 26775360 Jun 23 10:28 out.rmf
    -rw-r--r-- 2 pulsar pulsar   120960 Jun 23 10:27 out_back.pha
    ```
