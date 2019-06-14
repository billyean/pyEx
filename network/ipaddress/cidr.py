import sys


class CIDR:
    def __init__(self, cidr):
        try:
            list = cidr.split("/")
            if len(list) != 2:
                raise ValueError("Invalid CIDR address")
            self.ipv4 = self.valid_address(list[0].strip())
            self.n = int(list[1].strip())
            if self.ipv4[0] < 128:
                if self.n < 8 or self.n > 30:
                    raise ValueError("Invalid CIDR address")

            elif self.ipv4[0] < 192:
                if self.n < 16 or self.n > 30:
                    raise ValueError("Invalid CIDR address")

            elif self.ipv4[0] < 224:
                if self.n < 24 or self.n > 30:
                    raise ValueError("Invalid CIDR address")
        except:
            raise ValueError("Invalid CIDR address")

    def first_last_address(self):
        mask = [255, 255, 255, 255]
        last_address = [0, 255, 255, 254]

        if self.n > 8:
            if self.n < 16:
                last_address[1] = (1 << (16 - self.n)) - 1
                mask[1] = 255 >> (16 - self.n) << (16 - self.n)
            elif self.n < 24:
                last_address[2] = (1 << (24 - self.n)) - 1
                mask[2] = 255 >> (24 - self.n) << (24 - self.n)
            else:
                last_address[3] = (1 << (32 - self.n)) - 1
                mask[3] = 255 >> (32 - self.n) << (32 - self.n)

        print(mask)

        network_address = [self.ipv4[0] & mask[0], self.ipv4[1] & mask[1], self.ipv4[2] & mask[2], self.ipv4[3] & mask[3]]

        first_address = [network_address[0], network_address[1], network_address[2], network_address[3] + 1]
        last_address = [network_address[0] + last_address[0], network_address[1] + last_address[1], network_address[2]
                         + last_address[2], network_address[3] + last_address[3]]

        return ".".join([str(x) for x in first_address]), ".".join([str(x) for x in last_address])

    def valid_address(self, ip_address):
        try:
            ipv4 = [int(x) for x in ip_address.split(".")]
            if len(ipv4) != 4:
                raise ValueError("Invalid IP address")
            if ipv4[0] <= 1 or ipv4[0] >= 224:
                raise ValueError("Invalid IP address")

            return ipv4
        except:
            raise ValueError("Invalid IP address")


def main(cidr_str):
    cidr = CIDR(cidr_str)

    addresses = cidr.first_last_address()
    print(f"first_address = {addresses[0]}, last_address = {addresses[1]}")


if __name__ == "__main__":
    main(sys.argv[1])
