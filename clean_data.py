import os
import sys
from nltk.tokenize import word_tokenize
import re


def clean_sent(line):
    tokens = word_tokenize(line.lower().decode('utf-8'))
    return ' '.join(tokens).encode('utf-8')


def clean_data(filenames, outfiles, clean):
    for f in range(len(filenames)):
        with open(filenames[f]) as doc:
            orig_doc = doc.read().split('\n')
        if clean: # remove labels from starts of each line
            cleaned_lines = '\n'.join([clean_sent(' '.join(line.split()[1:])) for line in orig_doc])
        else:
            cleaned_lines = '\n'.join([clean_sent(line) for line in orig_doc])
        lines = cleaned_lines.replace('\n\n', '\n')
        while lines[-1] == '\n':
            lines = lines[:-1]
        with open(outfiles[f], 'w') as new_file:
            new_file.write(lines)


if __name__ == '__main__':
    orig_dir = sys.argv[1]
    res_dir = sys.argv[2]
    clean = False
    if len(sys.argv) == 4:
        clean = True
    if os.path.isdir(orig_dir):
        all_files = os.listdir(orig_dir)
        filenames = [orig_dir + x for x in all_files if not (x.startswith('.'))]
        outfiles = [res_dir + x for x in all_files if not (x.startswith('.'))]
        if not os.path.exists(res_dir):
            os.makedirs(res_dir)
    else:
        filenames = [orig_dir]
        outfiles = [res_dir]
    clean_data(filenames, outfiles, clean)
