# example usage: 
# python get_subset.py --part $(demo.test_part) --total $(demo.test_total) > run.sh

import click
from subprocess import Popen, PIPE
import sys
import numpy as np

@click.command()
@click.option('--part', type=int)
@click.option('--total', type=int)
def find_test(part, total):
    print("set -x")

    all_tests = []
    proc = Popen(['pytest', '--collect-only','-q'], stdout=PIPE)

    for l in proc.stdout:
        l = l.decode()
        if l != '\n' and '::' in l and 'test' in l:
            all_tests.append(l.strip())
    
    print("Found {} tests".format(len(all_tests)), file=sys.stderr)
    chosen_ones = np.array_split(all_tests, total)[part-1]
    print("Chosen {} tests \nFirst {} \nLast {}".format(len(chosen_ones), chosen_ones[0], chosen_ones[-1]), file=sys.stderr)

    print("pytest \\")
    for t in chosen_ones:
        print('  "{}" \\'.format(t))
    print() 

if __name__ == "__main__":
    find_test()
