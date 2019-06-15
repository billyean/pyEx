# Start you local environment

## MacOSX/Linux

```bash
# Create a virtual environment and activate it
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Windows

```bash
# Create a virtual environment and activate it
python -m venv venv
venv\Scripts\activate
(venv) pip install -r requirements.txt
```

# run test

```bash
$ pytest
```

or 

```bash
$ pytest --verbose

latform darwin -- Python 3.7.3, pytest-4.6.3, py-1.8.0, pluggy-0.12.0 -- /Users/h0y01c9/code/pyEx/network/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/h0y01c9/code/pyEx/network
collected 11 items                                                                                                                                                                                                                                                                                         

test/test_cidr.py::test_address_range[10.0.0.45/8-expected_addresses0] PASSED                                                                                                                                                                                                                        [  9%]
test/test_cidr.py::test_address_range[201.222.10.60/26-expected_addresses1] PASSED                                                                                                                                                                                                                   [ 18%]
test/test_cidr.py::test_address_range[201.222.10.124/26-expected_addresses2] PASSED                                                                                                                                                                                                                  [ 27%]
test/test_cidr.py::test_address_range[15.16.193.6/21-expected_addresses3] PASSED                                                                                                                                                                                                                     [ 36%]
test/test_cidr.py::test_address_range[128.16.32.13/30-expected_addresses4] PASSED                                                                                                                                                                                                                    [ 45%]
test/test_cidr.py::test_address_range[198.51.100.39/28-expected_addresses5] PASSED                                                                                                                                                                                                                   [ 54%]
test/test_cidr.py::test_number_of_block[10.0.0.45/8-16777214] PASSED                                                                                                                                                                                                                                 [ 63%]
test/test_cidr.py::test_number_of_block[201.222.10.60/26-62] PASSED                                                                                                                                                                                                                                  [ 72%]
test/test_cidr.py::test_number_of_block[201.222.10.124/26-62] PASSED                                                                                                                                                                                                                                 [ 81%]
test/test_cidr.py::test_number_of_block[15.16.193.6/21-2046] PASSED                                                                                                                                                                                                                                  [ 90%]
test/test_cidr.py::test_number_of_block[128.16.32.13/30-2] PASSED  
```