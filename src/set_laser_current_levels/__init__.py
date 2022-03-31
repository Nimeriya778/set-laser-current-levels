"""
Sets laser current levels via UDP
"""

from socket import socket, AF_INET, SOCK_DGRAM
from struct import pack, calcsize
from argparse import ArgumentParser, Namespace
import sys

# Send to the UDP protocol port
UDP_PORT = 21074

# Send the laser diodes current level datagrams to the address
DEFAULT_DEST_ADDR = "127.0.0.1"

# Contants
MAGIC = 0xD10D
VERSION = 0x0100


def scan_args() -> Namespace:
    """Parses command line arguments"""

    parser = ArgumentParser(description="Set laser current levels")
    parser.add_argument(
        "--angld1", default=0, type=int, help="Angular LD1 current level code"
    )
    parser.add_argument(
        "--angld2", default=0, type=int, help="Angular LD2 current level code"
    )
    parser.add_argument(
        "--linld1", default=0, type=int, help="Linear LD1 current level code"
    )
    parser.add_argument(
        "--linld2", default=0, type=int, help="Linear LD2 current level code"
    )
    parser.add_argument(
        "--focld1", default=0, type=int, help="Focal LD1 current level code"
    )
    parser.add_argument(
        "--focld2", default=0, type=int, help="Focal LD2 current level code"
    )
    parser.add_argument(
        "addr",
        nargs="?",
        default=DEFAULT_DEST_ADDR,
        type=str,
        metavar="ADDR",
        help="Destination address",
    )

    return parser.parse_args()


# The UDP diagram payload has data fields described in struct format
PAYLOAD_FMT = ">8H"
size = calcsize(PAYLOAD_FMT)


def pack_data(args: Namespace) -> bytes:
    """Returns a bytes object"""

    # Values must be representable as 'unsigned short'
    try:
        packet = pack(
            PAYLOAD_FMT,
            MAGIC,
            VERSION,
            args.angld1,
            args.angld2,
            args.linld1,
            args.linld2,
            args.focld1,
            args.focld2,
        )
    except ValueError:
        print("Negative values are not allowed", file=sys.stderr)
        sys.exit(1)

    return packet


def main() -> None:
    # Create a socket object
    s = socket(family=AF_INET, type=SOCK_DGRAM, proto=0)

    args = scan_args()

    # Sends laser diodes current level broadcast protocol datagrams
    s.sendto(pack_data(args), (args.addr, UDP_PORT))
