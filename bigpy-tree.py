import os, sys, pprint

trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Python31\Lib'
else:
    dirname = '/usr/lib/python2.7'

allsize = []
for (this_dir, subs_here, files_here) in os.walk(dirname):
    if trace:
        print(this_dir)
    for filename in files_here:
        if filename.endswith('.py'):
            if trace:
                print('...', filename)
            fullname = os.path.join(this_dir, filename)
            fullsize = os.path.getsize(fullname)
            allsize.append((fullsize, fullname))

allsize.sort()
pprint.pprint(allsize[:2])
print(allsize[-2:])
pprint.pprint(allsize[-2:])