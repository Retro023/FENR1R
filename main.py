#!/usr/bin/env python3

# FENR1R
# A linux privEsc Enum tool


# Standard lib import (only use standlib incase other modules are not avalible)
import os
import subprocess
import getpass
import pwd
import pprint
import platform
from sys import exit
import sys
import time


# FENR1R scripts
from scripts.SUID import scan_suids
from scripts.CAP import scan_caps
from scripts.CRON import scan_cron_folders, scan_cronJobs
from scripts.Network import scan_network_interfaces
from scripts.SUDO import scan_sudo_privs


# banner for tool
def banner_custom():
    # colours for banner
    blue = "\033[0;34m"
    cyan = "\033[0;36m"
    purp = "\033[0;35m"
    END = "\033[0m"
    try:
        # Banner
        Version = 0.3
        banner = f""" 
        +===============================================+
        |                                               |
        |                                               |
        |{cyan} ███████╗███████╗███╗   ██╗██████╗  ██╗██████╗ {END}|
        |{cyan} ██╔════╝██╔════╝████╗  ██║██╔══██╗███║██╔══██╗{END}|
        |{cyan} █████╗  █████╗  ██╔██╗ ██║██████╔╝╚██║██████╔╝{END}|
        |{purp} ██╔══╝  ██╔══╝  ██║╚██╗██║██╔══██╗ ██║██╔══██╗{END}|
        |{purp} ██║     ███████╗██║ ╚████║██║  ██║ ██║██║  ██║{END}|
        |{purp} ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═╝╚═╝  ╚═╝{END}|
        |  {blue}Version: {str(Version)} {END}                                |
        |                                               |                                               
        | Author: MuteAvery                             |
        |                                               |
        +===============================================+    
        """
    # incase this ascii art throws a syntax error make banner a simple string
    except SyntaxError:
        banner = "FENR1R"

    return banner


# Detect the OS
def detect_OS():
    os_name = "Linux"  # default
    try:
        with open("/etc/os-release", "r") as file:
            for line in file:
                if line.startswith("ID="):
                    os_name = line.split("=")[1].strip().strip('"')
                    break
    except FileNotFoundError:
        pass
    return os_name


# Detect the kernel info
def detect_kernel():
    # check if platform is avalible if it is get kernel via that if not run uname -r
    if "platform" in globals():
        try:
            kernel = platform.release()
        except Exception as e:
            print(f"Kernel detect error:{e}")
    else:
        try:
            kernel = subprocess.check_output(["uname", "-r"], text=True).strip()
        except ImportError:
            print("Import error")
            pass
    return kernel


# detect system architecture
def detect_arch():
    try:
        # use platfrom to detect arch
        arch = platform.machine()
    # if platform is not avalible pass on
    except ImportError as e:
        print(f"Arch detect error {e}")
        pass
    return arch


# find info on the users user
def self_user_info():
    # user info
    current_user = getpass.getuser()
    uid = os.getuid()
    user_info = pwd.getpwuid(uid)
    # users shell
    user_shell = os.environ.get("SHELL", user_info.pw_shell)
    # users env vars
    env_vars = dict(os.environ)
    # check if user is a root user
    isroot = False
    if os.getuid() == 0:
        isroot == True
    # format return for output file
    return {
        "uid": uid,
        "username": current_user,
        "shell": user_shell,
        "user_info": user_info,
        "ENV": env_vars,
        "isRoot": isroot,
    }


# Find human users
def get_users():
    users = []
    try:
        with open("/etc/passwd") as file:
            for line in file:
                if "nologin" not in line:
                    fields = line.strip().split(":")
                    if len(fields) >= 7:
                        users.append(
                            {
                                "name": fields[0],
                                "gid": fields[3],
                                "home": fields[5],
                                "shell": fields[6],
                            }
                        )
    except FileNotFoundError:
        print("No passwd file found")
    return users


# Find system services
def get_services():
    services = []
    try:
        with open("/etc/passwd") as file:
            for line in file:
                if "nologin" in line:  # system/service accounts
                    fields = line.strip().split(":")
                    if len(fields) >= 6:
                        services.append(
                            {"name": fields[0], "gid": fields[3], "home": fields[5]}
                        )
    except FileNotFoundError:
        print("No passwd file found")
    return services


# create a unique file name for each output file

# inital seed
seed = int(time.time() * 1000) % (2**31)


# Generate filename
def Rfilename():
    # randomise the seed
    def rand():
        # Generate seed
        global seed
        seed = (1103515246 * seed + 4454) % 2**31
        return seed / 2**31

    # craft file name
    length = 8
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    res = ""
    for i in range(length):
        index = int(rand() * len(chars))
        res += chars[index]
    return res


def main():
    # check python verison is compatible
    Required_version = 3.6
    if sys.version_info[0] < 3:
        print("Fatal ERROR: FENR1R Requires python3 version 3.6 or higher")
        sys.exit(1)
    if sys.version_info[1] < Required_version:
        print("Fatal ERROR: FENR1R Requires python3 version 3.6 or higher")
        sys.exit(1)

    # get the banner and print it
    banner = banner_custom()
    print(banner)

    # get user info here so if user is root it prints under the banner while the other scripts run
    user_info = self_user_info()

    if user_info["username"] == "root":
        print("YOU ARE ROOT")

    try:
        # system scripts to enum the system
        os_name = detect_OS()
        kernel = detect_kernel()
        arch = detect_arch()
        sudo_privs = scan_sudo_privs()
        users = get_users()
        services = get_services()
        interfaces = scan_network_interfaces()
        suid_list, privesc_vectors = scan_suids()
        res = Rfilename()
        cap_list, privesc_vectors_cap = scan_caps()
        crontabs = scan_cronJobs()
        cron_folders = scan_cron_folders()

        # break line length
        break_line = 60

        # Print results to a file in nice format by breaking each result into columns
        output = banner + "\n\n"

        # OS info
        output += "OS INFO\n"
        output += "=" * break_line + "|\n"
        output += f"OS: {os_name}\n"
        output += f"kernel: {kernel}\n"
        output += f"Arch: {arch}\n"
        output += "=" * break_line + "|\n\n"

        # USERS
        output += "\nUSERS\n"
        output += "=" * break_line + "|\n"
        for u in users:
            output += f"Name: {u['name']},  Gid: {u['gid']}, Home: {u['home']}, Shell: {u['shell']}\n"
        output += "=" * break_line + "|\n\n"

        # USER (self)
        output += "Self user\n"
        output += "=" * break_line + "|\n"
        user_info = self_user_info()
        sudo_info = scan_sudo_privs()
        # print env vars in pretty format
        env_str = pprint.pformat(user_info["ENV"], width=90)

        # output the user info to file in correct format
        output += (
            f"Is a root user:{user_info['isRoot']}\n"
            f"Name: {user_info['username']}\n"
            f"UID: {user_info['uid']}\n"
            f"Shell: {user_info['shell']}\n"
            f"User info: {user_info['user_info']}\n"
            f"ENV: {env_str}\n"
            f"SUDO: Privs:{sudo_info['sudo_privs']}\n"
            f"SUDO Requires password: {sudo_info['password_required']}\n"
        )
        output += "=" * break_line + "|\n\n"

        # SERVICES
        output += "\nServices\n"
        output += "=" * break_line + "|\n"
        for s in services:
            output += f"Name: {s['name']},  Gid: {s['gid']}, Home: {s['home']}\n"
        output += "=" * break_line + "|\n\n"

        # Network interface
        output += "\nNetwork interfaces\n"
        output += "=" * break_line + "|\n"
        for i in interfaces:
            output += (
                f"Name: {i['Name']}, IP: {i['IP']}, MAC: {i['MAC']}, isUP: {i['Up']}\n"
            )
        output += "=" * break_line + "|\n\n"

        # SUIDS (all)
        output += "SUIDs(ALL)\n"
        output += "=" * break_line + "|\n"
        for s in suid_list:
            output += f"SUID:{s}\n"
        output += "=" * break_line + "|\n\n"

        # SUIDs (privesc_vectors)
        output += "SUID privesc_vectors\n"
        output += "=" * break_line + "|\n"
        for s in privesc_vectors:
            output += f"SUID: {s}\n"
        output += "=" * break_line + "|\n\n"

        # CAPs (all)
        output += "CAPs(ALL)\n"
        output += "=" * break_line + "|\n"
        for c in cap_list:
            output += f"CAP: {c}\n"
        output += "=" * break_line + "|\n\n"

        # CAPs (privesc_vectors)
        output += "CAPs(privesc)\n"
        output += "=" * break_line + "|\n"
        for c in privesc_vectors_cap:
            output += f"CAPs:{c}\n"
        output += "=" * break_line + "|\n\n"

        # Cron Jobs (crontab)
        output += "CronJobs(crontab)\n"
        output += "=" * break_line + "|\n"
        if not crontabs:
            output += "No crontabs found (manual check may be needed)\n"  # Add this to all  outputs to remove confusion
        else:
            for cr in crontabs:
                output += f"Cron_job: {cr}\n"
        output += "=" * break_line + "|\n\n"

        # Cron Jobs (folders)
        output += "CronJobs(folders)\n"
        output += "=" * break_line + "|\n"
        if not cron_folders:
            output += "No Cron jobs found (manual check may be needed)\n"
        else:
            for cr in cron_folders:
                output += f"Cron_Jobs: {cr}\n"
        output += "=" * break_line + "|\n\n"

        # write to file
        os.makedirs("Reports", exist_ok=True)
        file_path = f"Reports/{res}.txt"
        with open(file_path, "w") as f:
            f.write(f"{output}")

            print(f"Report written to {file_path}")

    # Error  Handling

    # User exits
    except KeyboardInterrupt:
        print("\n\nUser exited!\n")
        exit(1)

        # if system doesnt have one of the standard libarys program will fail so exit cleanly
    except ImportError as e:
        print(f"Import Error!: {e} ")
        exit(1)

    # Catch any other error print it and continue
    except Exception as e:
        print(f"Exception Error!: {e}")
        pass


if __name__ == "__main__":
    main()

# Copyright (c) 2025 MuteAvery. All Rights Reserved.
