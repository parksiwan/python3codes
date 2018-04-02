"""
Find the largest file of a given type in an arbitrary directory tree.
"""

import os, pprint
from sys import argv, exc_info

trace = 1  # 0=off, 1=dirs, 2=+files
dirname, extname = os.curdir, '.py'
if len(argv) > 1:
    dirname = argv[1]
if len(argv) > 2:
    extname = argv[2]
if len(argv) > 3:
    trace = int(argv[3])

def tryprint(arg):
    try:
        print(arg)
    except UnicodeDecodeError:
        print(arg.encode())

visited = set()
allsize = []
for (this_dir, subshere, files_here) in os.walk(dirname):
    if trace:
        tryprint(this_dir)
    this_dir = os.path.normpath(this_dir)
    fixname = os.path.normcase(this_dir)
    if fixname in visited:
        if trace:
            tryprint('skipping ' + this_dir)
    else:
        visited.add(fixname)
        for filename in files_here:
            if filename.endswith(extname):
                if trace > 1:
                    tryprint('+++' + filename)
                fullname = os.path.join(this_dir, filename)
                try:
                    bytesize = os.path.getsize(fullname)
                    linesize = sum(+1 for line in open(fullname, 'rb'))
                except Exception:
                    print('error', exc_info()[0])
                else:
                    allsize.append((bytesize, linesize, fullname))
for (title, key) in [('bytes', 0), ('lines', 1)]:
    print ('\nBy %s...' % title)
    allsize.sort(key=lambda x: x[key])
    pprint.pprint(allsize[:3])
    pprint.pprint(allsize[-3:])
