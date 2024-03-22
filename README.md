# checkOperators
check the dimension-6 SMEFT operators an analysis is sensitive to
The code submits on condor the creation of folders from MG5 for the quadratic term. If the quadratic term exists then the condor job will output a tarred folder


# Procedure

Copy a ```create_llj.py, submit_llj.sh, submit_llj.sub``` and change the name to something like ```create_<procname>.py, submit_<procname>.sh, submit_<procname>.sub```

inside ```create_<procname>.py``` change the ```proc_ID``` line (line 152) to ```<procname>```. In line 171 change the process definition to the one you want

Inside ```submit_<procname>.sh``` change ```llj``` everywhere to ```<procname>```

Inside ```submit_<procname>.sub```, line 4 change the executable name ```submit_llj.sh``` to ```submit_<procname>.sh```, in line 11 change ```launch_llj.tar.xz``` to ```launch_<procname>.tar.xz```

Now run ```python create_<procname>.py```, you will see that a lot of txt files will be created namely ```launch_<procname>_<op>_QU.txt```. inspect one of them (like using cat) and check that the process definition is the one you want.
Then create a tarball with all the txt files: ```tar -zcvf launch_<procname>.tar.xz launch_<procname>_*_QU.txt```


Now you are ready to submit the jobs:

```condor_submit submit_<procname>.sub```

If an operator exist for given process, the condor job will return a tarred folder such as ```ll_clj1_QU.tar.xz```. If that happens it means that MG5 found at least one diagram for your topology for the given operator.

Cheers
