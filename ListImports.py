import pefile
import sys
import os

if len(sys.argv) < 2:
    print('[!] Invalid amount of arguments specified.')
    print('python {} [executable]'.format(os.path.basename(__file__)))
    exit()

executable_path = sys.argv[1]
executable_name = os.path.basename(executable_path)
executable_pe = pefile.PE(executable_path)

print("[*] Listing imports for: {}".format(executable_name))

for entry in executable_pe.DIRECTORY_ENTRY_IMPORT:
    print(entry.dll.decode())
    for function in entry.imports:
        if function.ordinal:
            print('\t{}: {}'.format(hex(function.ordinal), function.name.decode()))
        else:
            print('\t{}'.format(function.name.decode()))
    print()







