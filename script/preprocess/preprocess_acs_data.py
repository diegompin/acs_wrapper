"""
Author: Diego Pinheiro
github: https://github.com/diegompin

"""
import itertools as it
from src.util.util_multiprocessing import *
from scripts.acs.preprocess.acs_preprocess import AcsPreprocess



def write_hdf(args):
    filename, f_data = args
    df = f_data.get_data()
    datapath = 'datalink/acs/data_output/'
    df.to_csv('%s/df_%s.csv' % (datapath, filename), index=True)


def main():
    print('INITIALIZING EXPORTING ACS DATA')
    readers, level, year, estimates = AcsPreprocess.get_param()
    datapath = 'datalink/acs/data_input/%s'
    data = dict()
    for (r, l, y, e) in it.product(readers, level, year, estimates):
        data['%s_%s_%d_%d' % (r.__name__, l, y, e)] = r(datapath=datapath % l, year=y, estimates=e)
    args = tuple(zip(data.keys(), data.values()))
    with MyPool(processes=4) as pool:
        pool.map(write_hdf, args)
    print('FINISHED EXPORTING ACS DATA')


if __name__ == "__main__":
    main()
