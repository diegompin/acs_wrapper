"""
Author: Diego Pinheiro
github: https://github.com/diegompin

"""

from acs_wrapper.src.read.acs_read_base import AcsRead


class AcsReadRace(AcsRead):

    def __init__(self, datapath, year, estimates):
        super().__init__(datapath=datapath, prefix='RAC', datafile='B03002', year=year, estimates=estimates,
                         column_format='HD01_VD%02d', is_percent=False)

    def get_mappings(self):
        """
        HD01_VD03
        Estimate; Not Hispanic or Latino: - White alone

        HD01_VD04
        Estimate; Not Hispanic or Latino: - Black or African American alone
        """
        mappings = [{
            'TOTAL': 1,
            'WHITE': 3,
            'BLACK': 4,
            'INDIAN': 5,
            'ASIAN': 6,
            'PACIFIC': 7,
            'OTHER': [8, 9],
            'HISPANIC': [13, 14, 15, 16, 17, 18, 19]
        }]
        return mappings


class AcsReadEducation(AcsRead):

    def __init__(self, datapath, year, estimates):
        super().__init__(datapath=datapath, prefix='EDU', datafile='S1501', year=year, estimates=estimates,
                         column_format='HC01_EST_VC%02d', is_percent=False)

    def get_mappings(self):
        """
                HC01_EST_VC02
                Total; Estimate; Population 18 to 24 years

                HC01_EST_VC03
                Total; Estimate; Population 18 to 24 years - Less than high school graduate

                HC01_EST_VC04
                Total; Estimate; Population 18 to 24 years - High school graduate (includes equivalency)

                HC01_EST_VC05
                Total; Estimate; Population 18 to 24 years - Some college or associate's degree

                HC01_EST_VC06
                Total; Estimate; Population 18 to 24 years - Bachelor's degree or higher

                HC01_EST_VC08
                Total; Estimate; Population 25 years and over

                HC01_EST_VC09
                Total; Estimate; Population 25 years and over - Less than 9th grade

                HC01_EST_VC10
                Total; Estimate; Population 25 years and over - 9th to 12th grade, no diploma

                HC01_EST_VC11
                Total; Estimate; Population 25 years and over - High school graduate (includes equivalency)

                HC01_EST_VC12
                Total; Estimate; Population 25 years and over - Some college, no degree

                HC01_EST_VC13
                Total; Estimate; Population 25 years and over - Associate's degree

                HC01_EST_VC14
                Total; Estimate; Population 25 years and over - Bachelor's degree

                HC01_EST_VC15
                Total; Estimate; Population 25 years and over - Graduate or professional degree

                """
        mappings = [
            {
                'TOTAL': [2],
                'ELEMENTAR': [3],
                'HIGH': [4],
                'COLLEGE': [5],
                'BACHELOR': [6]
            },
            {
                'TOTAL': [8],
                'ELEMENTAR': [9],
                'HIGH': [10, 11],
                'COLLEGE': [12],
                'BACHELOR': [13, 14, 15]
            }
        ]
        return mappings


class AcsReadIncome(AcsRead):

    def __init__(self, datapath, year, estimates):
        super().__init__(datapath=datapath, prefix='INC', datafile='S1901', year=year, estimates=estimates,
                         column_format='HC01_EST_VC%02d', is_percent=True)

    def get_mappings(self):
        """
        HC01_EST_VC02
        Households; Estimate; Less than $10,000

        HC01_EST_VC03
        Households; Estimate; $10,000 to $14,999

        HC01_EST_VC04
        Households; Estimate; $15,000 to $24,999

        HC01_EST_VC05
        Households; Estimate; $25,000 to $34,999


        HC01_EST_VC06
        Households; Estimate; $35,000 to $49,999

        HC01_EST_VC07
        Households; Estimate; $50,000 to $74,999

        HC01_EST_VC08
        Households; Estimate; $75,000 to $99,999


        HC01_EST_VC09
        Households; Estimate; $100,000 to $149,999

        HC01_EST_VC10
        Households; Estimate; $150,000 to $199,999

        HC01_EST_VC11
        Households; Estimate; $200,000 or more
        """
        mappings = [{
            'TOTAL': 1,
            'A': 2,
            'B': 3,
            'C': 4,
            'D': 5,
            'E': 6,
            'F': 7,
            'G': 8,
            'H': 9,
            'I': 10,
            'J': 11
        }]
        return mappings




datapath = 'data/data_input/%s'
l = 'county'
y = 16
e = 5
r = AcsReadRace(datapath=datapath % l, year=y, estimates=e)
r_edu = AcsReadEducation(datapath=datapath % l, year=y, estimates=e)
r_inc = AcsReadIncome(datapath=datapath % l, year=y, estimates=e)

df_rac = r.get_data()
df_edu = r_edu.get_data()
df_inc = r_inc.get_data()


df_rac.loc['01001']
df_edu.loc['01001']
df_inc.loc['01001']


import numpy as np
np.corrcoef(df_edu.loc[:, 'EDU_TOTAL'].values, df_rac.loc[:, 'RAC_TOTAL'].values)


