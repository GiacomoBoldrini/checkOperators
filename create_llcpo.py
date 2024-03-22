#!/usr/bin/env python

# prepare command files to be passed to Madgraph to produce the folders
# for the event generation, for linear and quadratic BSM components
# when a single EFT operator is turned on.
# The script does not submit the folder event generation,
# since I am not sure that the right environment would be setup.
# to submit the folder generation:  for fil in `ls | grep launch_WZ` ; do ./bin/mg5_aMC $fil ;done

import os
import sys


if __name__ == "__main__":

  params = [  ( "1" ,  "cGtil"  , "SMEFTcpv", "1" ), 
   ( "2" ,  "cWtil", "SMEFTcpv", "2" ),
   ( "3" ,  "cHGtil", "SMEFTcpv", "3" ),
   ( "4" ,  "cHWtil", "SMEFTcpv", "4" ),
   ( "5" ,  "cHBtil", "SMEFTcpv", "5" ),
   ( "6" ,  "cHWBtil", "SMEFTcpv", "6" ),
   ( "7" ,  "cuGIm", "SMEFTcpv", "7" ),
   ( "8" ,  "ctGIm", "SMEFTcpv", "8" ),
   ( "9" ,  "cuWIm", "SMEFTcpv", "9" ),
   ( "10",  "ctWIm", "SMEFTcpv", "10" ),
   ( "11",  "cuBIm", "SMEFTcpv", "11" ),
   ( "12",  "ctBIm", "SMEFTcpv", "12" ),
   ( "13",  "cdGIm", "SMEFTcpv", "13" ),
   ( "14",  "cbGIm", "SMEFTcpv", "14" ),
   ( "15",  "cdWIm", "SMEFTcpv", "15" ),
   ( "16",  "cbWIm", "SMEFTcpv", "16" ),
   ( "17",  "cdBIm", "SMEFTcpv", "17" ),
   ( "18",  "cbBIm", "SMEFTcpv", "18" ),
   ( "19",  "cuHIm", "SMEFTcpv", "19" ),
   ( "20",  "ctHIm", "SMEFTcpv", "20" ),
   ( "21",  "cdHIm", "SMEFTcpv", "21" ),
   ( "22",  "cbHIm", "SMEFTcpv", "22" ),
   ( "23",  "cHudIm", "SMEFTcpv", "23" ),
   ( "24",  "cHtbIm", "SMEFTcpv",  "24" ),
   ( "25",  "cutbd1Im", "SMEFTcpv", "25" ),
   ( "26",  "cutbd8Im", "SMEFTcpv", "26" ),
   ( "27",  "cjQtu1Im", "SMEFTcpv", "27" ),
   ( "28",  "cjQtu8Im", "SMEFTcpv", "28" ),
   ( "29",  "cjQbd1Im", "SMEFTcpv", "29" ),
   ( "30",  "cjQbd8Im", "SMEFTcpv", "30" ),
   ( "31",  "cjujd1Im", "SMEFTcpv", "31" ),
   ( "32",  "cjujd8Im", "SMEFTcpv", "32" ),
   ( "33",  "cjujd11Im", "SMEFTcpv", "33" ),
   ( "34",  "cjujd81Im", "SMEFTcpv", "34" ),
   ( "35",  "cQtjd1Im", "SMEFTcpv", "35" ),
   ( "36",  "cQtjd8Im", "SMEFTcpv", "36" ),
   ( "37",  "cjuQb1Im", "SMEFTcpv", "37" ),
   ( "38",  "cjuQb8Im", "SMEFTcpv", "38" ),
   ( "39",  "cQujb1Im", "SMEFTcpv", "39" ),
   ( "40",  "cQujb8Im", "SMEFTcpv", "40" ),
   ( "41",  "cjtQd1Im", "SMEFTcpv", "41" ),
   ( "42",  "cjtQd8Im", "SMEFTcpv", "42" ),
   ( "43",  "cQtQb1Im", "SMEFTcpv", "43" ),
   ( "44",  "cQtQb8Im", "SMEFTcpv", "44" ),
   ( "45",  "ceHIm", "SMEFTcpv", "45" ),
   ( "46",  "ceWIm", "SMEFTcpv", "46" ),
   ( "47",  "ceBIm", "SMEFTcpv", "47" ),
   ( "48",  "cledjIm", "SMEFTcpv", "48" ),
   ( "49",  "clebQIm", "SMEFTcpv", "49" ),
   ( "50",  "cleju1Im", "SMEFTcpv", "50" ),
   ( "51",  "cleju3Im", "SMEFTcpv", "51" ),
   ( "52",  "cleQt1Im", "SMEFTcpv", "52" ),
   ( "53",  "cleQt3Im", "SMEFTcpv", "53" )]

  switchOn = [str(i+1) for i in range(53)]

  proc_ID = 'llcpo'

  for p in params: print(p[1])

  # generate the quadratic component folders
  for param in params:
    if param[0] not in switchOn : continue   
    f_launchfile = open ('launch_' + proc_ID + '_' + param[1] + '_QU.txt', 'w')
    f_launchfile.write ('import model SMEFTsim_topU3l_MwScheme_UFO_b_massless-' + param[1] + '_massless\n')
    f_launchfile.write ('generate    p p > l+ l-   QCD=0 NP=1 NP^2==2 SMHLOOP=0\n')
    f_launchfile.write ('output ' + proc_ID + '_' + param[1] + '_QU')
    f_launchfile.close ()

