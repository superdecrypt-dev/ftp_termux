#!/data/data/com.termux/files/usr/bin/python

import argparse
import os
import sys

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    parser = argparse.ArgumentParser(description="FTP server untuk Termux")
    parser.add_argument("--host", default="127.0.0.1", help="Alamat host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=2121, help="Port (default: 2121)")
    parser.add_argument("--dir", default="/data/data/com.termux", help="Direktori yang di-share (default: /data/data/com.termux)")
    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        print(f"ERROR: Direktori '{args.dir}' tidak ditemukan.", file=sys.stderr)
        sys.exit(1)

    authorizer = DummyAuthorizer()
    authorizer.add_anonymous(args.dir, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((args.host, args.port), handler)

    print("\n" + "=" * 55)
    print("  PERINGATAN KEAMANAN")
    print("=" * 55)
    print("  Server FTP ini TANPA PASSWORD.")
    print("  HANYA untuk jaringan lokal pribadi.")
    print("  JANGAN dibuka ke Wi-Fi publik atau internet.\n")

    print(f"  ftp://{args.host}:{args.port}")
    print(f"  Direktori: {args.dir}\n")
    print("  Tekan Ctrl+C untuk menghentikan server.")
    print("=" * 55 + "\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nMenghentikan server...")
        server.close_all()
        sys.exit(0)


if __name__ == "__main__":
    main()
