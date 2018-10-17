"""
Author: Diego Pinheiro
github: https://github.com/diegompin

"""

from src.acs.read.acs_read import AcsReadRace, AcsReadEducation, AcsReadIncome


class AcsPreprocess(object):

    def __init__(self):
        pass

    @staticmethod
    def get_param():
        readers = [AcsReadRace, AcsReadEducation, AcsReadIncome]
        # readers = [AcsReadRace]
        level = ['county', 'zcta']
        year = [16]
        estimates = [5]
        return readers, level, year, estimates