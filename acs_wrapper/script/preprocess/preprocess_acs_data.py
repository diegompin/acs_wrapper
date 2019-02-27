"""
Author: Diego Pinheiro
github: https://github.com/diegompin

"""
import itertools as it
from acs_wrapper.script.preprocess.acs_preprocess import AcsPreprocess
from acs_wrapper.src.util_multiprocessing import MyPool


def write_hdf(args):
    filename, f_data = args
    df = f_data.get_data()
    datapath = 'datalink/acs_wrapper/data_output/'
    df.to_csv('%s/df_%s.csv' % (datapath, filename), index=True)


def main():
    print('INITIALIZING EXPORTING ACS DATA')
    readers, level, year, estimates = AcsPreprocess.get_param()
    datapath = 'datalink/acs_wrapper/data_input/%s'
    data = dict()
    for (r, l, y, e) in it.product(readers, level, year, estimates):
        data['%s_%s_%d_%d' % (r.__name__, l, y, e)] = r(datapath=datapath % l, year=y, estimates=e)
    args = tuple(zip(data.keys(), data.values()))
    with MyPool(processes=4) as pool:
        pool.map(write_hdf, args)
    print('FINISHED EXPORTING ACS DATA')


if __name__ == "__main__":
    main()
