__author__ = 'diegopinheiro'
__email__ = 'diegompin@gmail.com'
__github__ = 'https://github.com/diegompin'

from acs_wrapper.src.read.acs_read_base import AcsRead


class AcsReadIncome(AcsRead):

    def __init__(self, datapath):
        super().__init__(datapath=datapath, prefix='INC', datafile='S1901', column_format='HC01_EST_VC%02d',
                         is_percent=True)

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
