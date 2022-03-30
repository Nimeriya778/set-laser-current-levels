Set laser current levels program
================================

The program creates and sends packets to the AFS server using 
connectionless UDP over IPv4. 
The packet contains laser diode current level codes.

Configuration
-------------

The script is configured via the command line arguments as follows:

```
usage: set_laser_current_levels.py [-h] [--angld1 ANGLD1] [--angld2 ANGLD2] 
[--linld1 LINLD1] [--linld2 LINLD2] [--focld1 FOCLD1] [--focld2 FOCLD2] [ADDR]

positional arguments:
  ADDR                     Destination address

optional arguments:
  -h, --help               show this help message and exit
  --angld1 ANGLD1          Angular LD1 current level code
  --angld2 ANGLD2          Angular LD2 current level code
  --linld1 LINLD1          Linear LD1 current level code
  --linld2 LINLD2          Linear LD2 current level code
  --focld1 FOCLD1          Focal LD1 current level code
  --focld2 FOCLD2          Focal LD2 current level code
 
```
