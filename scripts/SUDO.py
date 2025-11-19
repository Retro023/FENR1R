import subprocess


def scan_sudo_privs():
    sudo_stuff = {}
    try:
        # run sudo -l -n to see if user needs a password for sudo
        result = subprocess.run(
            ["sudo", "-l", "-n"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        # if the user can run sudo with out a password then retur they can run sudo and dont need a password
        if result.returncode == 0:
            sudo_suff = {
                "sudo_privs": True,
                "password_required": False,
                "output": result.stdout,
            }

        # if password is needed return they need a password for sudo
        if "sudo: a password is required\n" in result.stderr.lower():
            sudo_stuff = {
                "sudo_privs": True,
                "password_required": True,
                "output": result.stdout,
            }

    except Exception as e:
        print(f"Error occured\nDetails:{e}")
    return sudo_stuff
