import os


# interesting files and extenstions to look for
interesting_files = [
    "wp_config.php",
    "config.php",
    "database.php",
    "settings.py",
    "config.yaml",
    "credentials.json",
    "id_rsa",
    "authorized_keys",
    "startup.sh",
    "deploy.sh",
    "Dockerfile",
    "docker-compose.yml",
    "Makefile",
    "env.sh",
    ".env",
    "app.conf",
    "service.conf",
    "nginx.conf",
    "httpd.conf",
    "logging.conf",
]

interesting_fileExt = [
    ".conf",
    ".service",
    ".rules",
    ".env",
    ".sh",
    ".py",
    ".pl",
    ".cgi",
    ".deb",
    ".rpm",
    ".log",
    ".key",
    ".pem",
    ".kdbx",
    ".socket",
    ".timer",
]


# scan file system for interesting files
def scan_files():
    interesting_files_found = []
    total = 0
    # walk thru the system file and gather files
    for root, dirs, files in os.walk("/", topdown=True, followlinks=False):
        for name in files:
            # give user update on scan so they do not think it crashed
            total += 1
            print(f"Scanning files for files of interest... Checked: {total}", end="\r")
            path = os.path.join(root, name)

            # check if file is interesting
            try:
                file_name = path
            except (PermissionError, FileNotFoundError, OSError):
                continue
            if file_name in interesting_files:
                interesting_files_found.append(file_name)
    return interesting_files_found


# scan system for interesting file extenstions
def scan_files_ext():
    interesting_fileExt_found = []
    total = 0
    # walk thru the system file and gather files
    for root, dirs, files in os.walk("/", topdown=True, followlinks=False):
        for name in files:
            # give user update on scan so they do not think it crashed
            total += 1
            print(f"Scanning files for files of interest... Checked: {total}", end="\r")
            path = os.path.join(root, name)

            # check if file has an interesting extenstion
            try:
                file_name = path
            except (PermissionError, FileNotFoundError, OSError):
                continue
            if file_name in interesting_files:
                interesting_fileExt_found.append(file_name)
    return interesting_fileExt_found
