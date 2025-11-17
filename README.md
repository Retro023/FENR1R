# FENR1R

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


## Future Plans

FENR1R will be updated with new enum techniques and functionality.

FENR1R_W, This is the windows version of FENR1R

Speed, FENR1R will get faster as its improved 
