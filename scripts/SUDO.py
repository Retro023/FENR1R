import subprocess

# Check if sudo asks for passwd
def Check_sudoPasswd():
    try:
        # run sudo -l -n to see if user needs a password for sudo
        result = subprocess.run(
            ["sudo", "-l", "-n"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        # if the user can run sudo with out a password then set SudoPasswd to true
        if result.returncode == 0:
            SudoPasswd = False

        else:
            SudoPasswd = True

        return SudoPasswd

    # If error tell user then set SudoPasswd to error
    except Exception as e:
        print(f"Error occured\nDetails:{e}")
        SudoPasswd = "Error occured trying to check for a sudo password"
        return SudoPasswd
