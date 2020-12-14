# PFLOTRAN-SIP Framework
The source code is available at the following:
<https://bitbucket.org/satkarra/pflotran-e4d-sip/src/master/>
# Installation of the code
- Dowload PETSC: git clone <https://gitlab.com/petsc/petsc>
- cd petsc
- git checkout xsdk-0.2.0
- ./configure --CFLAGS='-O3' --CXXFLAGS='-O3' --FFLAGS='-O3' --with-debugging=no --download-mpich=yes --download-hdf5=yes --download-fblaslapack=yes --download metis=yes --download-parmetis=yes
- export PETSC\_DIR=/home/username/path\_to\_top\_level\_petsc
- export PETSC\_ARCH=gnu-c-debug
- cd \$PETSC\_DIR
- make all (or follow make instructions printed at the end of configuration.)
- Download PFLOTRAN: git clone <https://bitbucket.org/satkarra/pflotran-e4d-sip/src/master/>
- cd src/pflotran/
- make pflotran (for using multiple processors use -- make -j np pflotran (where np = number of processors))

