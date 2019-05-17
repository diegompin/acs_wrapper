__author__ = 'diegopinheiro'
__email__ = 'diegompin@gmail.com'
__github__ = 'https://github.com/diegompin'

from acs_wrapper.src.read.acs_read_base import AcsRead


class AcsReadTypeHealthInsuranceAge(AcsRead):

    def __init__(self, datapath):
        super().__init__(datapath=datapath, prefix='INSURANCECOREVAGE', datafile='B27001',
                         column_format='HC01_EST_VC%02d', is_percent=True)

    def get_mappings(self):

        '''
        HD01_VD01
        Estimate; Total:

        HD01_VD13
        Estimate; Under 19 years:
        - With two or more types of health insurance coverage:
        - With Medicare and Medicaid/means-tested public coverage

        HD01_VD14
        Estimate; Under 19 years:
        - With two or more types of health insurance coverage:
        - Other private only combinations

        HD01_VD15
        Estimate; Under 19 years:
        - With two or more types of health insurance coverage:
        - Other public only combinations

        HD01_VD16
        Estimate; Under 19 years:
        - With two or more types of health insurance coverage:
        - Other coverage combinations

        HD01_VD17
        Estimate; Under 19 years:
        - No health insurance coverage


        '''
        mappings = [
            {
                'TOTAL': [1],
                'NO_INSURANCE': [17],
                'PRIVATE': [],
                'MEDICARE': [6, 12, 13],
                'MEDICAID': [7, 13],
                'MILITARY': []

                'EMPLOYER_BASED': [4, 11, 12],
                'DIRECT_PURCHASE': [5, 11, 14],

                'TRICARE_MILITARY': [8],
                'VETERAN': [9]

            }
        ]
        return mappings
