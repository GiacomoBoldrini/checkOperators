#!/bin/bash
ls 
tar -axf MG5_aMC_v2_6_5.tar.gz
tar -axf launch_llj.tar.xz

./MG5_aMC_v2_6_5/bin/mg5_aMC launch_llj_"$1"_QU.txt
if [ -d llj_"$1"_QU ]; then 
   tar -zcvf llj_"$1"_QU.tar.xz llj_"$1"_QU
fi
#rm launch_* MG5_aMC_v2_6_5.tar.gz
#rm -rf MG5_aMC_v2_6_5
#ls 
