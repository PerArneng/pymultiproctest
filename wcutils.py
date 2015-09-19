__author__ = 'pure'

from os import listdir
from os.path import isfile, join

class CountResult:

    def __init__(self, file, line_count, word_count):
        self.file = file
        self.line_count = line_count
        self.word_count = word_count

    def __str__(self):
        return "%s: lines %s words %s" % (self.file, self.line_count, self.word_count)



def process_directory(directory, pool = None):
    files = [ join(directory, f) for f in listdir(directory) if isfile(join(directory, f)) ]
    results = []

    if pool:
        results = pool.map(count_file, files)
    else:
        results = map(count_file, files)

    return results

def count_file(file):
    line_count = 0
    word_count = 0

    with open(file) as contents:
        for i, l in enumerate(contents):
            line_count = i
            word_count = len(l.split(" ")) + word_count

    return CountResult(file, line_count, word_count)