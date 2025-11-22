import re
import subprocess
import os
import stat
from time import sleep

# Known cap privEscs
known_cap_privEscs = {
    "gbd": "https://gtfobins.github.io/gtfobins/gdb/#capabilities",
    "node": "https://gtfobins.github.io/gtfobins/node/#capabilities",
    "perl": "https://gtfobins.github.io/gtfobins/perl/#capabilities",
    "php": "https://gtfobins.github.io/gtfobins/php/#capabilities",
    "python": "https://gtfobins.github.io/gtfobins/python/#capabilities",
    "ruby": "https://gtfobins.github.io/gtfobins/ruby/#capabilities",
    "rview": "https://gtfobins.github.io/gtfobins/rview/#capabilities",
    "rvim": "https://gtfobins.github.io/gtfobins/rvim/#capabilities",
    "view": "https://gtfobins.github.io/gtfobins/gdb/#capabilities",
    "vim": "https://gtfobins.github.io/gtfobins/gdb/#capabilities",
    "vimdiff": "https://gtfobins.github.io/gtfobins/vimdiff/#capabilities",
}
# add more


def scan_caps():
    print("")  # new line
    # cap file list
    cap_files = []

    # total ammount of files Scanned
    total = 0
    cap_vectors = []
    # walk thru the system file and gather files
    for root, dirs, files in os.walk("/", topdown=True, followlinks=False):
        for name in files:
            # give user update on scan so they do not think it crashed
            total += 1
            print(f"Scanning files for Caps... Checked: {total}", end="\r")
            path = os.path.join(root, name)

            # check if file is cap (simple error check to see if user has perms and file exists)
            try:
                xattrs = os.listxattr(path)
            except (PermissionError, FileNotFoundError, OSError):
                continue
            if "security.capability" in xattrs:
                cap_files.append(path)

    try:
        # if suids are found then print them in a easy to follow neat format
        if cap_files:
            print("\nCAPs FOUND!!")
            print("=" * 30 + "|")
            sleep(0.1)
            for i in cap_files:
                # if the binary is in the known_privEscs then print the bianry with the link
                filename = os.path.basename(i)
                if filename in known_cap_privEscs:
                    print("Known Privesc vector found!")
                    print(">", filename, ":", known_cap_privEscs[filename])

                    # save the privesc vector to the vectors list for output file
                    cap_vectors.append(known_cap_privEscs[filename])
                    sleep(0.2)

                # print Suids every 0.2 seconds
                print(i)
                sleep(0.2)
            print("=" * 30 + "|")

        return cap_files, cap_vectors

    # IF error return that checking for vectors ran into an issue
    except Exception as e:
        print(f"Looking for Checking for cap_vectors\n error: {e}")
        cap_vectors = "Error occured"
        return cap_vectors, cap_files
