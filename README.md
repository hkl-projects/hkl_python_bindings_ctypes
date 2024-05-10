steps to use hkl python bindings through ctypes

# Install dependencies
```bash
sudo apt install build-essential gtk-doc-tools autoconf libgsl-dev libgtkmm-3.0-dev libg3d-dev libyaml-dev gettext autopoint gobject-introspection libtool autoconf-archive debhelper gnuplot-nox libbullet-dev libg3d-plugins libgirepository1.0-dev libgl-dev libgtk-3-dev libgtkglext1-dev libhdf5-dev elpa-htmlize sphinx dvipng org-mode povray asymptote libgtkmm-3.0-dev
```

```bash
git clone git clone https://repo.or.cz/hkl.git
cd hkl
```

# Check out previous version
Checking out version 5.0.0.2080 (Newest version requires package inih version that is not available in Ubuntu 20.04
```bash
git checkout 764f78d732d5a0181902bc11029fafad80ef1bbd
```

# Compile software with exported shared library files
```bash
./autogen
./configure --disable-gui --enable-introspection
make
make install
```
shared library files (.so) are placed into /usr/local/lib/ by default, can change with compilation flag "--libexecdir=DIR", see configuration\_help.txt
check /usr/local/lib:

```bash
ls /usr/local/lib
```

# Set up conda environment
```bash
conda env create -f env.yml
conda activate ornl_hkl
```

# Run test python bindings with ctypes package
```bash
python hkl_ctypes.py
```

# Looking into the imported library
In bash, you can see the available functions in the imported library using:
```bash
nm -D /usr/local/lib/libhkl.so
```
this output has been saved in a txt file as libhkl\_functions.txt


# Need to identify inputs and outputs of each function and reproduce the bindings example in hkl documentation

