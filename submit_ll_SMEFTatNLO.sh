#!/bin/bash
ls 
tar -axf MG5_aMC_v2_6_5.tar.gz
tar -axf launch_ll_SMEFTatNLO.tar.xz

./MG5_aMC_v2_6_5/bin/mg5_aMC launch_ll_SMEFTatNLO_"$1"_QU.txt
if [ -d ll_SMEFTatNLO_"$1"_QU ]; then 
   tar -zcvf ll_SMEFTatNLO_"$1"_QU.tar.xz ll_SMEFTatNLO_"$1"_QU
fi
#rm launch_* MG5_aMC_v2_6_5.tar.gz
#rm -rf MG5_aMC_v2_6_5
#ls 
