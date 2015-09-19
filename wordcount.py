__author__ = 'pure'
import sys
import wcutils
import multiprocessing
import datetime
from multiprocessing import Pool

def print_help():
    print "wordcount <opts> <directories>"
    print ""
    print "OPTIONS:"
    print " -m     use multiprocessing (optional)"
    print " -h     print this help (optional)"
    sys.exit(0)

def main():

    if len(sys.argv) == 1:
        print_help()
        sys.exit(1)

    args = sys.argv[1:]
    pool = None

    if "-h" in args:
        print_help()
        sys.exit(0)

    if "-m" in args:
        cpu_count = multiprocessing.cpu_count()
        pool = Pool(cpu_count)
        print "using multiprocessing with %s cpu's" % (cpu_count)
        args.remove("-m")
    else:
        print "no multiprocessing"

    if len(args) == 0:
        print "error: missing directories as arguments"
        print_help()
        sys.exit(1)

    all_results = []

    before = datetime.datetime.now()
    for dir in args:
        results = wcutils.process_directory(dir, pool)
        for result in results:
            all_results.append(result)
    delta = datetime.datetime.now() - before

    total_lines = 0
    total_words = 0

    for result in all_results:
        total_lines = total_lines + result.line_count
        total_words = total_words + result.word_count

    print "files: %s, lines: %s, words: %s" % (len(all_results), total_lines, total_words)
    print "elapsed time: %s" % (delta)

if __name__ == "__main__":
    main()