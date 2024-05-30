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


  smeftatnlo = {
      "DIM6": [
          [1, "Lambda"],
          [2, "cpDC"],
          [3, "cpWB"],
          [4, "cdp"],
          [5, "cp"],
          [6, "cWWW"],
          [7, "cG"],
          [8, "cpG"],
          [9, "cpW"],
          [10, "cpBB"]
      ],
      "DIM62F": [
          [1, "cpl1"],
          [2, "cpl2"],
          [3, "cpl3"],
          [4, "c3pl1"],
          [5, "c3pl2"],
          [6, "c3pl3"],
          [7, "cpe"],
          [8, "cpmu"],
          [9, "cpta"],
          [10, "cpqMi"],
          [11, "cpq3i"],
          [12, "cpQ3"],
          [13, "cpQM"],
          [14, "cpu"],
          [15, "cpt"],
          [16, "cpd"],
          [19, "ctp"],
          [22, "ctZ"],
          [23, "ctW"],
          [24, "ctG"]
      ],
      "DIM64F": [
          [1, "cQq83"],
          [2, "cQq81"],
          [3, "cQu8"],
          [4, "ctq8"],
          [6, "cQd8"],
          [7, "ctu8"],
          [8, "ctd8"],
          [10, "cQq13"],
          [11, "cQq11"],
          [12, "cQu1"],
          [13, "ctq1"],
          [14, "cQd1"],
          [16, "ctu1"],
          [17, "ctd1"],
          [19, "cQQ8"],
          [20, "cQQ1"],
          [21, "cQt1"],
          [23, "ctt1"],
          [25, "cQt8"]
      ],
      "DIM64F2L": [
          [1, "cQlM1"],
          [2, "cQlM2"],
          [3, "cQl31"],
          [4, "cQl32"],
          [5, "cQe1"],
          [6, "cQe2"],
          [7, "ctl1"],
          [8, "ctl2"],
          [9, "cte1"],
          [10, "cte2"],
          [13, "cQlM3"],
          [14, "cQl33"],
          [15, "cQe3"],
          [16, "ctl3"],
          [17, "cte3"],
          [19, "ctlS3"],
          [20, "ctlT3"],
          [21, "cblS3"]
      ],
      "DIM64F4L": [
          [1, "cll1111"],
          [2, "cll2222"],
          [3, "cll3333"],
          [4, "cll1122"],
          [5, "cll1133"],
          [6, "cll2233"],
          [7, "cll1221"],
          [8, "cll1331"],
          [9, "cll2332"]
      ]
  }

  fullOps = [i[1] for key in smeftatnlo.keys()
           for i in smeftatnlo[key]]

  # Lambda is a special parameter and should always specified at 1 TeV
  # in all restriction cards

  fullOps.remove("Lambda")
  proc_ID = 'lnuw_SMEFTatNLO'

  print(fullOps)
  # # generate the linear component folders
  # for param in params:
  #   if param[0] not in switchOn : continue   
  #   f_launchfile = open ('launch_' + proc_ID + '_' + param[1] + '_LI.txt', 'w')
  #   f_launchfile.write ('import model SMEFTsim_A_U35_MwScheme_UFO_v3_1-' + param[1] + '_massless\n')
  #   f_launchfile.write ('generate    p p > e+ e- mu+ vm  j j QCD=0 NP=1 NP^2==1 SMHLOOP=0\n')
  #   f_launchfile.write ('add process p p > e+ e- mu- vm~ j j QCD=0 NP=1 NP^2==1 SMHLOOP=0\n')
  #   # f_launchfile.write ('add process p p > e+ e- e- ve~  j j QCD=0 NP=1 NP^2==1 SMHLOOP=0\n')
  #   # f_launchfile.write ('add process p p > e+ e- e+ ve   j j QCD=0 NP=1 NP^2==1 SMHLOOP=0\n')
  #   f_launchfile.write ('output ' + proc_ID + '_' + param[1] + '_LI')
  #   f_launchfile.close ()


  # generate the quadratic component folders
  for param in fullOps:
    f_launchfile = open ('launch_' + proc_ID + '_' + param + '_QU.txt', 'w')
    f_launchfile.write ('import model SMEFTatNLO-' + param + '_massless\n')
    f_launchfile.write ('define l+ = e+ mu+ ta+\n')
    f_launchfile.write ('define l- = e- mu- ta-\n')
    f_launchfile.write ('define vl = ve vm vt\n')
    f_launchfile.write ('define vl~ = ve~ vm~ vt~\n')
    f_launchfile.write ('generate p p > ell+ vl w- $$ t t~ h QED=3 QCD=0 NP=2 [QCD]\n')
    f_launchfile.write ('output ' + proc_ID + '_' + param + '_QU')
    f_launchfile.close ()

  # # generate the SM component
  # if (len (sys.argv) > 1):
  #   f_launchfile = open ('launch_' + proc_ID + '_SM.txt', 'w')
  #   f_launchfile.write ('import model SMEFTsim_A_U35_MwScheme_UFO_v3_1-SMlimit_massless\n')
  #   f_launchfile.write ('generate    p p > e+ e- mu+ vm  j j QCD=0 SMHLOOP=0\n')
  #   f_launchfile.write ('add process p p > e+ e- mu- vm~ j j QCD=0 SMHLOOP=0\n')
  #   # f_launchfile.write ('add process p p > e+ e- e- ve~  j j QCD=0 SMHLOOP=0\n')
  #   # f_launchfile.write ('add process p p > e+ e- e+ ve   j j QCD=0 SMHLOOP=0\n')
  #   f_launchfile.write ('output ' + proc_ID + '_SM')
  #   f_launchfile.close ()
