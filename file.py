# Day 9: file command: Determine type of FILEs
import re, argparse, subprocess, sys
# Try to add all options of file command
parser4 = argparse.ArgumentParser(description = 'Determine type of FILEs', add_help=False)
parser4.add_argument('filename', type = str, nargs = '*', help = 'test for a file with filename')
parser4.add_argument('--help', action='store_true', help = 'display this help and exit')
parser4.add_argument('-v', '--version', '-bcCdEhikLlNnprsSvzZ0', action='store_true', help = 'output version information and exit')
parser4.add_argument('-m', '--magic-file', type = str, metavar = 'LIST', help = 'use LIST as a colon-separated list of magic number files')
parser4.add_argument('-z', '--uncompress', type = str, nargs = '*', metavar = 'filename', help = 'try to look inside compressed files')
parser4.add_argument('-Z', '--uncompress-noreport', type = str, nargs = '*', metavar = 'filename', help = 'only print the contents of compressed files')
parser4.add_argument('-e', '--exclude', type = str, metavar = 'TEST', help = 'exclude TEST from the list of test to be performed from files. Valid tests are: apptype, ascii, cdf, compress, csv, compress, encoding, soft, tar, json, text, tokens')
parser4.add_argument('--exclude-quiet', type = str, metavar = 'TEST', help = 'like exclude, but ignore known tests')
parser4.add_argument('-f', '--files-from', type = str, metavar = 'FILE', help = 'read the filenames to be examined from FILE')
parser4.add_argument('-F', '--separator', type = str, metavar = 'STRING', help = 'use string as separator instead of `:\'')
parser4.add_argument('-i', '--mime', type = str, nargs = '*', metavar = 'filename', help = 'output MIME type strings')
parser4.add_argument('--apple', type = str, nargs = '*', metavar = 'filename', help = 'output the Apple CREATOR/TYPE')
parser4.add_argument('--extension', type = str, nargs = '*', metavar = 'filename', help = 'output the slash-separated list of extensions')
parser4.add_argument('--mime-type', type = str, nargs = '*', metavar = 'filename', help = 'output the MIME type')
parser4.add_argument('--mime-encoding', type = str, nargs = '*', metavar = 'filename', help = 'output the MIME encoding')
parser4.add_argument('-k', '--keep-going', type = str, nargs = '*', metavar = 'filename', help = 'don\'t stop at the first match')
parser4.add_argument('-l', '--list', type = str, nargs = '*', metavar = 'filename', help = 'list magic strength')
parser4.add_argument('-L', '--deference', type = str, nargs = '*', metavar = 'filename', help = 'follow symlinks')
parser4.add_argument('-h', '--no-deference', type = str, nargs = '*', metavar = 'filename', help = 'don\'t follow symlinks')
parser4.add_argument('-n', '--no-buffer', type = str, nargs = '*', metavar = 'filename', help = 'don\'t buffer output')
parser4.add_argument('-N', '--no-pad', type = str, nargs = '*', metavar = 'filename', help = 'don\'t pad output')
parser4.add_argument('-0', '--print0', type = str, nargs = '*', metavar = 'filename', help = 'terminate filenames with NULL')
parser4.add_argument('-p', '--preserve-date', type = str, nargs = '*', metavar = 'filename', help = 'preserve access times on files')
parser4.add_argument('-P', '--parameter', type = str, metavar = 'name=value', help = 'set file engine parameter limits')
parser4.add_argument('-r', '--raw', type = str, nargs = '*', metavar = 'filename', help = 'don\'t translate unprintable characters to \\ooo')
parser4.add_argument('-s', '--special-files', type = str, nargs = '*', metavar = 'filename', help = 'treat special files as ordinary ones')
parser4.add_argument('-S', '--no-sandbox', type = str, nargs = '*', metavar = 'filename', help = 'disable system call sandboxing')
parser4.add_argument('-C', '--compile', action='store_true', help = 'compile file specified by -m to magic.mgc')
parser4.add_argument('-d', '--debug', type = str, nargs = '*', metavar = 'filename', help = 'print debugging messages')
parser4.add_argument('-b', '--brief', type = str, nargs = '*', metavar = 'filename', help = 'display output in brief mode')
parser4.add_argument('-E', type = str, nargs = '*', metavar = 'filename', help = 'on file-system errors, instead of handling the error as regular output as POSIX man-date and keep going, issue an error message and exit')
args8 = parser4.parse_args()
# Force to run wsl to run the file command as Windows subsystem
args10 = ['wsl']
args11 = sys.argv
for abcxyz in args11:
    if len(re.findall('file.py', abcxyz)) > 0:
        args10.append(abcxyz.strip('.\\').strip('./').strip('.py'))
    else:
        args10.append(abcxyz)
print(subprocess.run(args10, shell=True, stdout=subprocess.PIPE).stdout.decode('utf8'))