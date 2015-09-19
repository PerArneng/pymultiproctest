__author__ = 'pure'
import sys
import wcutils
import multiprocessing
from multiprocessing import Pool

def main():

    if len(sys.argv) < 2:
        print("need folders with txt files as arguments")
        sys.exit(1)

    all_results = []

    cpu_count = multiprocessing.cpu_count()
    pool = Pool(cpu_count)

    for dir in sys.argv[1:]:
        results = wcutils.process_directory(dir, pool)
        for result in results:
            all_results.append(result)

    for result in all_results:
        print result

if __name__ == "__main__":
    main()