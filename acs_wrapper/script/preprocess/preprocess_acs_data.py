"""
Author: Diego Pinheiro
github: https://github.com/diegompin

"""
import itertools as it
from acs_wrapper.script.preprocess.acs_preprocess import AcsPreprocess
from acs_wrapper.src.util_multiprocessing import MyPool


def write_hdf(args):

    reader, level, year, estimate = args
    datapath_input = 'datalink/data_input'
    reader = reader(datapath_input)
    df = reader.get_data(level, year, estimate)
    datapath_outout = 'datalink/data_output/'
    df.to_csv(f'{datapath_outout}/df_{reader.prefix}_{level}_{year}_{estimate}.csv', index=True)


def main():
    print('INITIALIZING EXPORTING ACS DATA')
    list_reader, list_level, list_year, list_estimate = AcsPreprocess.get_param()

    data = dict()
    # for arg in it.product(list_reader, list_level, list_year, list_estimate):
        # name = reader.__name__.split('AcsRead')[1].lower()
        # data[f'{name}_{level}_{year}_{estimate}'] = reader(datapath=datapath % level, year=year,
        #                                                               estimates=estimate)
    # list_args = tuple(zip(data.keys(), data.values()))
    list_args = it.product(list_reader, list_level, list_year, list_estimate)
    with MyPool(processes=4) as pool:
        pool.map(write_hdf, list_args)
    print('FINISHED EXPORTING ACS DATA')


if __name__ == "__main__":
    main()
