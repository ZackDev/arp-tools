from argparse import ArgumentParser
from base import RAW

if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('-i', type=str)
    ap.add_argument('-d', type=str)
    args = ap.parse_args()

    if args.i and args.d:
        p = bytes.fromhex('ff' * 6 + args.d * 16)
        try:
            s = RAW(args.i)
        except Exception as e:
            print('error creating socket for interface: {i}')
            print(e)
        try:
            s.send([p])
        except Exception as e:
            print('error sending packet')
            print(e)
    else:
        ap.print_help()
