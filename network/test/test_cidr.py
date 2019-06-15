import pytest
from ipaddress.cidr import CIDR


@pytest.mark.parametrize(
    'cidr_str, expected_addresses',
    [
        ('10.0.0.45/8', ('10.0.0.1', '10.255.255.254')),
        ('201.222.10.60/26', ('201.222.10.1', '201.222.10.62')),
        ('201.222.10.124/26', ('201.222.10.65', '201.222.10.126')),
        ('15.16.193.6/21', ('15.16.192.1', '15.16.199.254')),
        ('128.16.32.13/30', ('128.16.32.13', '128.16.32.14')),
        ('198.51.100.39/28', ('198.51.100.33', '198.51.100.46'))
    ]
)
def test_address_range(cidr_str, expected_addresses):
     cidr = CIDR(cidr_str)
     assert cidr.first_last_address() == expected_addresses

@pytest.mark.parametrize(
 'cidr_str, expected_number',
     [
         ('201.222.10.60/26', 62),
         ('201.222.10.124/26', 62),
         ('15.16.193.6/21', 2046),
         ('128.16.32.13/30', 2)
     ]
)
def test_number_of_block(cidr_str, expected_number):
     cidr = CIDR(cidr_str)
     assert cidr.number_of_block() == expected_number