# Day 9: cut command: Print selected parts of lines from each FILE to standard output
import re, argparse, subprocess, sys
# Try to add all options of cut command
parser4 = argparse.ArgumentParser(description = 'Print selected parts of lines from each FILE to standard output', add_help=False)
parser4.add_argument('-b', '--bytes', type = str, metavar = 'LIST', help = 'select only these bytes')
parser4.add_argument('-c', '--characters', type = str, metavar = 'LIST', help = 'select only these characters')
parser4.add_argument('-d', '--delimiter', type = str, metavar = 'DELIM', help = 'use DELIM instead of TAB for field delimiter')
parser4.add_argument('-f', '--fields', type = str, metavar = 'LIST', help = 'select only these fields; also print any line that contains no delimiter character, unless -s option is specified')
parser4.add_argument('-n', action='store_true', help = 'ignored')
parser4.add_argument('--complement', action='store_true', help = 'complement the set of selected bytes, characters, or fields')
parser4.add_argument('-s', '--only-delimited', action='store_true', help = 'do not print lines not containing delimiters')
parser4.add_argument('--output-delimiter', type = str, metavar = 'STRING', help = 'use STRING as output delimiter; the default is to use the input delimiter')
parser4.add_argument('-z', '--zero-terminated', action='store_true', help = 'line delimiter is NULL, not newline')
parser4.add_argument('filename', type = str, nargs='*', help = 'specify a filename')
parser4.add_argument('--help', action='store_true', help = 'display this help and exit')
parser4.add_argument('--version', action='store_true', help = 'output version information and exit')
args8 = parser4.parse_args()
# Force to run wsl to run the cut command as Windows subsystem
args10 = ['wsl']
args11 = sys.argv
for abcxyz in args11:
    if len(re.findall('cut.py', abcxyz)) > 0:
        args10.append(abcxyz.strip('.\\').strip('./').strip('.py'))
    else:
        args10.append(abcxyz)
print(subprocess.run(args10, shell=True, stdout=subprocess.PIPE).stdout.decode('utf8'))