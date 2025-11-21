# FENR1R
<img width="500" height="500" alt="FENR1R(1)" src="https://github.com/user-attachments/assets/379ab85c-40b8-480c-98a7-fc143801bc25" />


## What is FENR1R?
  FENR1R is a Linux PrivEsc enum tool.
  FENR1R Scans a target system for PrivEsc Vectors and then outputs its findings to a file following a,
  easy to understand format.
  
  #### [Note FENR1R can be run as a background, job all of its findings will be in its "Report" for you to check]

  
## Why FENR1R?
  FENR1R stands out as a simple to use, simple to read PrivEsc Tool. 
  FENR1R auto outputs the findings to a file following a set format which was designed with ease to read and ease to implement into your existing workflow


## Pros
Ease of use
easy to read and understand output file
Written by a CTF player for CTF players
Links to known privEsc Vectors

## Cons
Written in python (slowish)
Import errors may occurred (Care was taken to make sure all imports are apart of pythons standard lib)
All files need to be transferred to target system (could cause issue in locked down environments) 

## How to use
  FENR1R is super easy to use!
  The only hurdle is getting FENR1R onto the host, First zip the FENR1R files:

```sh

  zip FENR1R.zip FENR1R/*
```

  Then copy the zip file over to the target system however you like in this example we will use nc 

```sh

Target
nc -l -p 1234 > FENR1R.zip

host
nc <reciver_IP>  1234 < FENR1R.zip 
```



Once the FEN files are on the target you then run main.py to start the tool (TIP create  a folder in a dir your user has R&W perms in to save FENs files too i,e /tmp/FENR1R)

```sh
python3 main.py or ./main.py  (if main is executable and python3 is in user env) 
```

## EXAMPLE OUTPUT FILE 

```
        +===============================================+
        |                                               |
        |                                               |
        | ███████╗███████╗███╗   ██╗██████╗  ██╗██████╗ |
        | ██╔════╝██╔════╝████╗  ██║██╔══██╗███║██╔══██╗|
        | █████╗  █████╗  ██╔██╗ ██║██████╔╝╚██║██████╔╝|
        | ██╔══╝  ██╔══╝  ██║╚██╗██║██╔══██╗ ██║██╔══██╗|
        | ██║     ███████╗██║ ╚████║██║  ██║ ██║██║  ██║|
        | ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═╝╚═╝  ╚═╝|
        |  Version: 0.5                                 |
        |                                               |                                               
        | Author: MuteAvery                             |
        |                                               |
        +===============================================+    
        

OS INFO
============================================================|
OS: ubuntu
kernel: 4.15.0-112-generic
Arch: x86_64
============================================================|


USERS
============================================================|
Name: root,  Gid: 0, Home: /root, Shell: /bin/bash
Name: sync,  Gid: 65534, Home: /bin, Shell: /bin/sync
Name: lxd,  Gid: 65534, Home: /var/lib/lxd/, Shell: /bin/false
Name: pollinate,  Gid: 1, Home: /var/cache/pollinate, Shell: /bin/false
Name: mysql,  Gid: 113, Home: /nonexistent, Shell: /bin/false
Name: server-admin,  Gid: 1001, Home: /home/server-admin, Shell: /bin/bash
============================================================|

Self user
============================================================|
Is a root user: False
Name: server-admin
UID: 1001
Shell: /bin/bash
User info: pwd.struct_passwd(pw_name='server-admin', pw_passwd='x', pw_uid=1001, pw_gid=1001, pw_gecos=',,,', pw_dir='/home/server-admin', pw_shell='/bin/bash')
ENV: {'HOME': '/home/server-admin',
 'LANG': 'en_US.UTF-8',
 'LESSCLOSE': '/usr/bin/lesspipe %s %s',
 'LESSOPEN': '| /usr/bin/lesspipe %s',
 'LOGNAME': 'server-admin',
 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:',
 'MAIL': '/var/mail/server-admin',
 'OLDPWD': '/home/server-admin/FENR1R/scripts',
 'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin',
 'PWD': '/home/server-admin/FENR1R',
 'SHELL': '/bin/bash',
 'SHLVL': '1',
 'SSH_TTY': '/dev/pts/0',
 'TERM': 'xterm-256color',
 'USER': 'server-admin',
 'XDG_DATA_DIRS': '/usr/local/share:/usr/share:/var/lib/snapd/desktop',
 'XDG_RUNTIME_DIR': '/run/user/1001',
 'XDG_SESSION_ID': '2',
 '_': './main.py'}
SUDO: Privs:True
SUDO Requires password: True
============================================================|


Services
============================================================|
Name: daemon,  Gid: 1, Home: /usr/sbin
Name: bin,  Gid: 2, Home: /bin
Name: sys,  Gid: 3, Home: /dev
Name: games,  Gid: 60, Home: /usr/games
Name: man,  Gid: 12, Home: /var/cache/man
Name: lp,  Gid: 7, Home: /var/spool/lpd
Name: mail,  Gid: 8, Home: /var/mail
Name: news,  Gid: 9, Home: /var/spool/news
Name: uucp,  Gid: 10, Home: /var/spool/uucp
Name: proxy,  Gid: 13, Home: /bin
Name: www-data,  Gid: 33, Home: /var/www
Name: backup,  Gid: 34, Home: /var/backups
Name: list,  Gid: 38, Home: /var/list
Name: irc,  Gid: 39, Home: /var/run/ircd
Name: gnats,  Gid: 41, Home: /var/lib/gnats
Name: nobody,  Gid: 65534, Home: /nonexistent
Name: systemd-network,  Gid: 102, Home: /run/systemd/netif
Name: systemd-resolve,  Gid: 103, Home: /run/systemd/resolve
Name: syslog,  Gid: 106, Home: /home/syslog
Name: messagebus,  Gid: 107, Home: /nonexistent
Name: _apt,  Gid: 65534, Home: /nonexistent
Name: uuidd,  Gid: 110, Home: /run/uuidd
Name: dnsmasq,  Gid: 65534, Home: /var/lib/misc
Name: landscape,  Gid: 112, Home: /var/lib/landscape
Name: sshd,  Gid: 65534, Home: /run/sshd
============================================================|


Network interfaces
============================================================|
Name: lo, IP: ['127.0.0.1'], MAC: 00:00:00:00:00:00, isUP: False
Name: eth0, IP: ['192.168.0.12'], MAC: 06:cd:19:2d:b8:e3, isUP: True
============================================================|

SUIDs(ALL)
============================================================|
SUID:/snap/core/9804/bin/ping6
SUID:/snap/core/9804/bin/su
SUID:/snap/core/9804/bin/umount
SUID:/snap/core/9804/usr/bin/chfn
SUID:/snap/core/9804/usr/bin/chsh
SUID:/snap/core/9804/usr/bin/gpasswd
SUID:/snap/core/9804/usr/bin/newgrp
SUID:/snap/core/9804/usr/bin/passwd
SUID:/snap/core/9804/usr/bin/sg
SUID:/snap/core/9804/usr/bin/sudo
SUID:/snap/core/9804/usr/bin/sudoedit
SUID:/snap/core/9804/usr/bin/ubuntu-core-launcher
SUID:/snap/core/9804/usr/lib/dbus-1.0/dbus-daemon-launch-helper
SUID:/snap/core/9804/usr/lib/openssh/ssh-keysign
SUID:/snap/core/9804/usr/lib/snapd/snap-confine
SUID:/snap/core/9804/usr/sbin/pppd
SUID:/etc/alternatives/traceroute6
SUID:/bin/umount
SUID:/bin/mount
SUID:/bin/ping6
SUID:/bin/ping4
SUID:/bin/su
SUID:/bin/fusermount
SUID:/bin/ping
SUID:/usr/bin/atq
SUID:/usr/bin/newgidmap
SUID:/usr/bin/newuidmap
SUID:/usr/bin/sudoedit
SUID:/usr/bin/sudo
SUID:/usr/bin/pkexec
SUID:/usr/bin/chsh
============================================================|

SUID privesc_vectors
============================================================|
============================================================|

CAPs(ALL)
============================================================|
CAP: /usr/bin/mtr-packet
============================================================|

CAPs(privesc)
============================================================|
============================================================|

CronJobs(crontab)
============================================================|
Cron_job: SHELL=/bin/sh
Cron_job: PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
Cron_job: 17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
Cron_job: 25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
Cron_job: 47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
Cron_job: 52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
Cron_job: 57 0 * * 0 root if [ -x /usr/share/mdadm/checkarray ] && [ $(date +\%d) -le 7 ]; then /usr/share/mdadm/checkarray --cron --all --idle --quiet; fi
Cron_job: SHELL=/bin/sh
Cron_job: PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
Cron_job: 23 10 * * *   root    test -x /etc/cron.daily/popularity-contest && /etc/cron.daily/popularity-contest --crond
============================================================|

CronJobs(folders)
============================================================|
Cron_Jobs: SHELL=/bin/sh
Cron_Jobs: PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
Cron_Jobs: 17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
Cron_Jobs: 25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
Cron_Jobs: 47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
Cron_Jobs: 52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
Cron_Jobs: 57 0 * * 0 root if [ -x /usr/share/mdadm/checkarray ] && [ $(date +\%d) -le 7 ]; then /usr/share/mdadm/checkarray --cron --all --idle --quiet; fi
Cron_Jobs: SHELL=/bin/sh
Cron_Jobs: PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
Cron_Jobs: 23 10 * * *   root    test -x /etc/cron.daily/popularity-contest && /etc/cron.daily/popularity-contest --crond
============================================================|

 Interesting_files
============================================================|
/var/www/wordpress/wp_config.php
/opt/.../secret/setup.conf
============================================================|

 Interesting_files
============================================================|
Could not find interesting files extenstions
============================================================|
```






## Future Plans

FENR1R will be updated with new enum techniques and functionality.

FENR1R_W, This is the windows version of FENR1R
