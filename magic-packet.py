from argparse import ArgumentParser
from base import RAW

if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('-i', type=str)
    ap.add_argument('-d', type=str)
    args = ap.parse_args()

    if args.i and args.d:
        s = RAW(args.i)
        p = bytes.fromhex('ff' * 6 + args.d * 16)
        s.send([p])
    else:
        ap.print_help()
