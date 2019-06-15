import sys


class CIDR:
    """
    A class for CIDR address calculation, the class will take a CIDR address string as input. The initialization of
    the class will check:
    1. if a given ip address is a valid address.
    2. if given n is between 8 to 30(inclusive).
    3. when given ip address is a B class IP address, given n must be greater than 16.
    3. when given ip address is a C class IP address, given n must be greater than 24.
    """
    def __init__(self, cidr):
        try:
            ip_and_n = cidr.split("/")
            if len(ip_and_n) != 2:
                raise ValueError("Invalid CIDR address")
            self.ipv4 = self.valid_address(ip_and_n[0].strip())
            self.n = int(ip_and_n[1].strip())
            if self.ipv4[0] < 128:
                if self.n < 8 or self.n > 30:
                    raise ValueError("Invalid CIDR address")

            elif self.ipv4[0] < 192:
                if self.n < 16 or self.n > 30:
                    raise ValueError("Invalid CIDR address")

            elif self.ipv4[0] < 224:
                if self.n < 24 or self.n > 30:
                    raise ValueError("Invalid CIDR address")
        except ValueError:
            raise ValueError("Invalid CIDR address")

    def first_last_address(self):
        """
        Calculate the first usable host address and last host address in the subnet.
        The code set up default network mask and hosts inside the sub network for class A address; it checks n to decide
        if next segment of network mask or hosts need to be changed or not.
        :return: first host address and last host address by given CIDR string.
        """
        # Set mask and address for class A
        mask = [255, 0, 0, 0]
        address = [0, 255, 255, 255]

        if self.n > 8:
            if self.n < 16:
                address[1] = (1 << (16 - self.n)) - 1
                mask[1] = 255 >> (16 - self.n) << (16 - self.n)
            elif self.n < 24:
                mask[1] = 255
                address[1] = 0
                address[2] = (1 << (24 - self.n)) - 1
                mask[2] = 255 >> (24 - self.n) << (24 - self.n)
            else:
                mask[1] = 255
                mask[2] = 255
                address[1] = 0
                address[2] = 0
                address[3] = (1 << (32 - self.n)) - 1
                mask[3] = 255 >> (32 - self.n) << (32 - self.n)

        # Simple and to calculate network address
        network_address = [self.ipv4[0] & mask[0], self.ipv4[1] & mask[1], self.ipv4[2] & mask[2],
                           self.ipv4[3] & mask[3]]

        # First address will be one after network address.
        first_address = [network_address[0], network_address[1], network_address[2], network_address[3] + 1]
        # Last address will be one before network address + hosts
        last_address = [network_address[0] + address[0], network_address[1] + address[1],
                        network_address[2] + address[2], network_address[3] + address[3] - 1]

        return ".".join([str(x) for x in first_address]), ".".join([str(x) for x in last_address])

    def valid_address(self, ip_address):
        """
        Simple validation of IPv4 address, first octet should be [1..224], others octet should be [0..255]
        :param ip_address: a ipv4 address string
        :return: true if given string is a valid ipv4 address, false otherwise.
        """
        try:
            ipv4 = [int(x) for x in ip_address.split(".")]
            if len(ipv4) != 4:
                raise ValueError("Invalid IP address")
            if ipv4[0] <= 1 or ipv4[0] >= 224:
                raise ValueError("Invalid IP address")

            for index in range(1, 4):
                if ipv4[index] < 0 or ipv4[index] > 255:
                    raise ValueError("Invalid IP address")
            return ipv4
        except ValueError:
            raise ValueError("Invalid IP address")

    def number_of_block(self):
        """
        :return: number of usable hosts in the subnet.
        """
        return (1 << (32 - self.n)) - 2


def main(cidr_str):
    cidr = CIDR(cidr_str)

    addresses = cidr.first_last_address()
    print(f"first_address = {addresses[0]}, last_address = {addresses[1]}")


if __name__ == "__main__":
    """
    Format:
    python ipaddress/cidr.py {cidr address string}
    Example:
    python ipaddress/cidr.py "198.51.100.39/28"
    """
    main(sys.argv[1])
