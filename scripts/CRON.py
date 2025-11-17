import os
import subprocess

# Cron job list 
cron_jobs = []


# scan cronjobs using crontab
def scan_cronJobs():
    
    # get list of users cron jobs (crontab)
    user_cron = []
    #Get a list of cron jobs via crontab -l 
    try:
        result = subprocess.run(
        ["crontab", "-l"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # save correct results to seperate list to handle crontab and cron files seperately 
        if result.returncode == 0:
            result = result.stdout.splitlines()
            user_cron.append(result)
        # go thru crontab crons and only append real ones and not ones commented out
        for line in result:
            if line.strip() and not line.strip().startswith("#"):
                cron_jobs.append(("crontab", line.strip()))
        
    except Exception  as e :
        if "Exception Error!: name 'scan_cronjobs' is not defined" in str(e):
            print("Target doesn't seem to have a crontab... moving on")
            pass
        print(f"Error Exception {e}.... Moving on (crontab is probably not avalible for this user or installed!)")
        pass
    return cron_jobs 




def scan_cron_folders():
# cron file paths
    cron_paths = [
    "/etc/crontab",
    "/etc/cron.d",
    "/etc/cron.hourly", 
    "/var/spool/cron"
    ]
# Loop  thru all cron folders for files that contains cron jobs 
    try:
# total files scanned
        total = 0
        for path in cron_paths:
            # check if path is file
            if os .path.isfile(path):
                # for every file read it and only appened files that are not commented out
                with open(path, "r") as file:
                    for line in file:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            cron_jobs.append(line)

                        #Keep user updated with amount of files scanned
                            total += 1
                            print(f"Scanning Cron Files... Checked: {total}", end="\r")
                
            # Check if path is dir 
            elif os.path.isdir(path):
                # go thru dirs and find files 
                for filename in os.listdir(path):
                    file_path = os.path.join(path, filename)
                    if os.path.isfile(file_path):
                        with open(file_path) as file:
                            for line in file:
                                line = line.strip()
                                if line and not  line.startswith("#"):
                                    cron_jobs.append(line)
                        
                                    #Keep user updated with amount of files scanned
                                    total += 1
                                    print(f"Scanning Cron Files (extras)... Checked: {total}", end="\r")
# If errors raise then just pass and let program keep running but print debug lines 
    except FileNotFoundError as e:
        raise
        print(f"File not found error : {e}")
    except OSError as e :
        print(f"Os Error:   {e}")
        raise
    except Exception as e :
        print(f"Exception error:    {e}")
        raise
#Return cron_jobs list so main can print it to the output file, if no cron jobs found return no jobs found
    if not cron_jobs:
        return []
    return cron_jobs



