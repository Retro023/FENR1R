import os
import stat
from time import sleep

# list of known suids for priv esc
# match the binary to a link to a known privesv vector: i,e   Binary1:exploit.com/binary1
known_privEscs = {
    "aa-exec": "https://gtfobins.github.io/gtfobins/aa-exec/#suid",
    "ab": "https://gtfobins.github.io/gtfobins/ab/#suid",
    "agetty": "https://gtfobins.github.io/gtfobins/agetty/#suid",
    "alpine": "https://gtfobins.github.io/gtfobins/alpine/#suid",
    "ar": "https://gtfobins.github.io/gtfobins/ar/#suid",
    "arj": "https://gtfobins.github.io/gtfobins/arj/#suid",
    "arp": "https://gtfobins.github.io/gtfobins/arp/#suid",
    "as": "https://gtfobins.github.io/gtfobins/as/#suid",
    "ascii-xfr": "https://gtfobins.github.io/gtfobins/ascii-xfr/#suid",
    "ash": "https://gtfobins.github.io/gtfobins/ash/#suid",
    "aspell": "https://gtfobins.github.io/gtfobins/aspell/#suid",
    "atobm": "https://gtfobins.github.io/gtfobins/atobm/#suid",
    "awk": "https://gtfobins.github.io/gtfobins/awk/#suid",
    "base32": "https://gtfobins.github.io/gtfobins/base32/#suid",
    "base64": "https://gtfobins.github.io/gtfobins/base64/#suid",
    "basenc": "https://gtfobins.github.io/gtfobins/basenc/#suid",
    "basez": "https://gtfobins.github.io/gtfobins/basez/#suid",
    "bash": "https://gtfobins.github.io/gtfobins/bash/#suid",
    "bc": "https://gtfobins.github.io/gtfobins/bc/#suid",
    "bind shell": "https://gtfobins.github.io/gtfobins/bind shell/#suid",
    "bridge": "https://gtfobins.github.io/gtfobins/bridge/#suid",
    "busctl": "https://gtfobins.github.io/gtfobins/busctl/#suid",
    "busybox": "https://gtfobins.github.io/gtfobins/busybox/#suid",
    "bzip2": "https://gtfobins.github.io/gtfobins/bzip2/#suid",
    "cabal": "https://gtfobins.github.io/gtfobins/cabal/#suid",
    "capabilities": "https://gtfobins.github.io/gtfobins/capabilities/#suid",
    "capsh": "https://gtfobins.github.io/gtfobins/capsh/#suid",
    "cat": "https://gtfobins.github.io/gtfobins/cat/#suid",
    "chmod": "https://gtfobins.github.io/gtfobins/chmod/#suid",
    "choom": "https://gtfobins.github.io/gtfobins/choom/#suid",
    "chown": "https://gtfobins.github.io/gtfobins/chown/#suid",
    "chroot": "https://gtfobins.github.io/gtfobins/chroot/#suid",
    "clamscan": "https://gtfobins.github.io/gtfobins/clamscan/#suid",
    "cmp": "https://gtfobins.github.io/gtfobins/cmp/#suid",
    "column": "https://gtfobins.github.io/gtfobins/column/#suid",
    "comm": "https://gtfobins.github.io/gtfobins/comm/#suid",
    "command": "https://gtfobins.github.io/gtfobins/command/#suid",
    "cp": "https://gtfobins.github.io/gtfobins/cp/#suid",
    "cpio": "https://gtfobins.github.io/gtfobins/cpio/#suid",
    "cpulimit": "https://gtfobins.github.io/gtfobins/cpulimit/#suid",
    "csh": "https://gtfobins.github.io/gtfobins/csh/#suid",
    "csplit": "https://gtfobins.github.io/gtfobins/csplit/#suid",
    "csvtool": "https://gtfobins.github.io/gtfobins/csvtool/#suid",
    "cupsfilter": "https://gtfobins.github.io/gtfobins/cupsfilter/#suid",
    "curl": "https://gtfobins.github.io/gtfobins/curl/#suid",
    "cut": "https://gtfobins.github.io/gtfobins/cut/#suid",
    "dash": "https://gtfobins.github.io/gtfobins/dash/#suid",
    "date": "https://gtfobins.github.io/gtfobins/date/#suid",
    "dd": "https://gtfobins.github.io/gtfobins/dd/#suid",
    "debugfs": "https://gtfobins.github.io/gtfobins/debugfs/#suid",
    "dialog": "https://gtfobins.github.io/gtfobins/dialog/#suid",
    "diff": "https://gtfobins.github.io/gtfobins/diff/#suid",
    "dig": "https://gtfobins.github.io/gtfobins/dig/#suid",
    "distcc": "https://gtfobins.github.io/gtfobins/distcc/#suid",
    "dmsetup": "https://gtfobins.github.io/gtfobins/dmsetup/#suid",
    "docker": "https://gtfobins.github.io/gtfobins/docker/#suid",
    "dosbox": "https://gtfobins.github.io/gtfobins/dosbox/#suid",
    "ed": "https://gtfobins.github.io/gtfobins/ed/#suid",
    "efax": "https://gtfobins.github.io/gtfobins/efax/#suid",
    "elvish": "https://gtfobins.github.io/gtfobins/elvish/#suid",
    "emacs": "https://gtfobins.github.io/gtfobins/emacs/#suid",
    "env": "https://gtfobins.github.io/gtfobins/env/#suid",
    "eqn": "https://gtfobins.github.io/gtfobins/eqn/#suid",
    "espeak": "https://gtfobins.github.io/gtfobins/espeak/#suid",
    "expand": "https://gtfobins.github.io/gtfobins/expand/#suid",
    "expect": "https://gtfobins.github.io/gtfobins/expect/#suid",
    "file": "https://gtfobins.github.io/gtfobins/file/#suid",
    "file download": "https://gtfobins.github.io/gtfobins/file download/#suid",
    "file read": "https://gtfobins.github.io/gtfobins/file read/#suid",
    "file upload": "https://gtfobins.github.io/gtfobins/file upload/#suid",
    "file write": "https://gtfobins.github.io/gtfobins/file write/#suid",
    "find": "https://gtfobins.github.io/gtfobins/find/#suid",
    "fish": "https://gtfobins.github.io/gtfobins/fish/#suid",
    "flock": "https://gtfobins.github.io/gtfobins/flock/#suid",
    "fmt": "https://gtfobins.github.io/gtfobins/fmt/#suid",
    "fold": "https://gtfobins.github.io/gtfobins/fold/#suid",
    "gawk": "https://gtfobins.github.io/gtfobins/gawk/#suid",
    "gcore": "https://gtfobins.github.io/gtfobins/gcore/#suid",
    "gdb": "https://gtfobins.github.io/gtfobins/gdb/#suid",
    "genie": "https://gtfobins.github.io/gtfobins/genie/#suid",
    "genisoimage": "https://gtfobins.github.io/gtfobins/genisoimage/#suid",
    "gimp": "https://gtfobins.github.io/gtfobins/gimp/#suid",
    "grep": "https://gtfobins.github.io/gtfobins/grep/#suid",
    "gtester": "https://gtfobins.github.io/gtfobins/gtester/#suid",
    "gzip": "https://gtfobins.github.io/gtfobins/gzip/#suid",
    "hd": "https://gtfobins.github.io/gtfobins/hd/#suid",
    "head": "https://gtfobins.github.io/gtfobins/head/#suid",
    "hexdump": "https://gtfobins.github.io/gtfobins/hexdump/#suid",
    "highlight": "https://gtfobins.github.io/gtfobins/highlight/#suid",
    "hping3": "https://gtfobins.github.io/gtfobins/hping3/#suid",
    "iconv": "https://gtfobins.github.io/gtfobins/iconv/#suid",
    "install": "https://gtfobins.github.io/gtfobins/install/#suid",
    "ionice": "https://gtfobins.github.io/gtfobins/ionice/#suid",
    "ip": "https://gtfobins.github.io/gtfobins/ip/#suid",
    "ispell": "https://gtfobins.github.io/gtfobins/ispell/#suid",
    "jjs": "https://gtfobins.github.io/gtfobins/jjs/#suid",
    "join": "https://gtfobins.github.io/gtfobins/join/#suid",
    "jq": "https://gtfobins.github.io/gtfobins/jq/#suid",
    "jrunscript": "https://gtfobins.github.io/gtfobins/jrunscript/#suid",
    "julia": "https://gtfobins.github.io/gtfobins/julia/#suid",
    "ksh": "https://gtfobins.github.io/gtfobins/ksh/#suid",
    "ksshell": "https://gtfobins.github.io/gtfobins/ksshell/#suid",
    "kubectl": "https://gtfobins.github.io/gtfobins/kubectl/#suid",
    "ld.so": "https://gtfobins.github.io/gtfobins/ld.so/#suid",
    "less": "https://gtfobins.github.io/gtfobins/less/#suid",
    "library load": "https://gtfobins.github.io/gtfobins/library load/#suid",
    "limited suid": "https://gtfobins.github.io/gtfobins/limited suid/#suid",
    "links": "https://gtfobins.github.io/gtfobins/links/#suid",
    "logsave": "https://gtfobins.github.io/gtfobins/logsave/#suid",
    "look": "https://gtfobins.github.io/gtfobins/look/#suid",
    "lua": "https://gtfobins.github.io/gtfobins/lua/#suid",
    "make": "https://gtfobins.github.io/gtfobins/make/#suid",
    "mawk": "https://gtfobins.github.io/gtfobins/mawk/#suid",
    "minicom": "https://gtfobins.github.io/gtfobins/minicom/#suid",
    "more": "https://gtfobins.github.io/gtfobins/more/#suid",
    "mosquitto": "https://gtfobins.github.io/gtfobins/mosquitto/#suid",
    "msgattrib": "https://gtfobins.github.io/gtfobins/msgattrib/#suid",
    "msgcat": "https://gtfobins.github.io/gtfobins/msgcat/#suid",
    "msgconv": "https://gtfobins.github.io/gtfobins/msgconv/#suid",
    "msgfilter": "https://gtfobins.github.io/gtfobins/msgfilter/#suid",
    "msgmerge": "https://gtfobins.github.io/gtfobins/msgmerge/#suid",
    "msguniq": "https://gtfobins.github.io/gtfobins/msguniq/#suid",
    "tar": "https://gtfobins.github.io/gtfobins/tar/#limited-suid",
}
# add more


# Colours
blue = "\033[0;34m"
cyan = "\033[0;36m"
purp = "\033[0;35m"
END = "\033[0m"


# scan for Suids then print the suids to user and tell the user if binary has a known suid privesc
# Save the suid files to a list and the known vectors another list to then print them to the output file
def scan_suids():
    # suid file list
    Suid_files = []

    # list of vectors to privesc
    vectors = []

    # total ammount of files Scanned
    total = 0

    # walk thru the system file and gather files
    for root, dirs, files in os.walk("/", topdown=True, followlinks=False):
        for name in files:
            # give user update on scan so they do not think it crashed
            total += 1
            print(
                f"{purp}Scanning files for sticky bits... Checked: {total} {END}",
                end="\r",
            )
            path = os.path.join(root, name)

            # check if file has sticky bit (simple error check to see if user has perms and file exists)
            try:
                st = os.stat(path)
            except (PermissionError, FileNotFoundError, OSError):
                continue
            if st.st_mode & stat.S_ISUID:
                Suid_files.append(path)

    try:
        # if suids are found then print them in a easy to follow neat format
        if Suid_files:
            print("\nSUIDs FOUND!!")
            print("=" * 30 + "|")
            sleep(0.1)
            for i in Suid_files:
                # if the binary is in the known_privEscs then print the bianry with the link
                filename = os.path.basename(i)
                if filename in known_privEscs:
                    print(f"{cyan}Known Privesc vector found!{END}")
                    print(">", filename, ":", known_privEscs[filename])

                    # save the privesc vector to the vectors list for output file
                    vectors.append(known_privEscs[filename])
                    sleep(0.2)

                # print Suids every 0.2 seconds
                print(i)
                sleep(0.2)
            print("=" * 30 + "|")
            return Suid_files, vectors

    except Exception as e:
        print(f"Error occured while checking for SUID vectors\nError: {e}")
        vectors = "Error occured"
        return Suid_files, vectors
