**[A]**

**[B]**

**[C]**
- [`Cython and CPython`](https://www.tutorialspoint.com/what-is-the-difference-between-cython-and-cpython) \
  CPython is the implementation of the language called “Python” in C. not only Cpython,some more are implemented like IronPython and Jython (Python implemented in Java).
  Python is an interpreted programming language. Hence, Python programmers need interpreters to convert Python code into machine code. Where as Cython is a compiled programming language. The Cython programs can be executed directly by the CPU of the underlying computer without using any interpreter.
  Cython is much faster than Python. many programmers to opt for Cython to write concise and readable code in Python that perform as faster as C code.
  Cython is designed as a C-extension for Python. The developers can use Cython to speed up Python code execution. But they can still write and run Python programs without using Cython. But the programmers have to install both Python and C-compiler as a pre-requisite to run Cython programs.

**[D]**
- [delete](https://www.cyberciti.biz/faq/how-to-find-and-delete-directory-recursively-on-linux-or-unix-like-system/) \
  ```aidl
  
  find /path/to/dir/ -type d -empty -print0 | xargs -0 -I {} /bin/rm -rf "{}"
  find /backups/ -type d -name "foo*" -print0 | xargs -0 -I {} /bin/rm -rf "{}"
  ```

**[E]**

**[F]**

**[G]** \
- [`glances`](html#:~:text=Glances%20is%20a%20cross%2Dplatform,curses%20or%20web%2Dbased%20interface.) \
Glances is a cross-platform monitoring tool written in Python.  It’ll run on almost any platform, including Microsoft, macOS, and Linux/GNU. This tool makes it easier for developers to view a large amount of monitoring information through a curses or web-based interface.     
  https://jaxenter.com/glances-monitoring-tool-147359.

- [GNU](https://gcc.gnu.org/) \
  The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as libraries for these languages (libstdc++,...). GCC was originally written as the compiler for the GNU operating system. The GNU system was developed to be 100% free software, free in the sense that it respects the user's freedom. \
  
**[H]** \
`head -7 ho.py`

**[I]**

**[J]**

**[K]**

**[L]**

**[M]**

**[N]** \
Get ex IP\
``sh
curl -4 icanhazip.com
``

**[O]**

**[P]**
- [Python version set](https://unix.stackexchange.com/questions/410579/change-the-python3-default-version-in-ubuntu) 
`sudo update-alternatives  --set python /usr/bin/python3.6`

> Packet Managers 
 
https://brew.sh/ \
Homebrew installs the stuff you need that Apple (or your Linux system) didn’t. Homebrew installs packages to their own directory and then symlinks their files into /usr/local.

https://docs.conda.io/en/latest/ \
Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN, and more.

https://spack.io/ \
Spack is a package manager for supercomputers, Linux, and macOS. It makes installing scientific software easy. Spack isn’t tied to a particular language; you can build a software stack in Python or R, link to libraries written in C, C++, or Fortran, and easily swap compilers or target specific microarchitectures. Learn more here. \

https://snapcraft.io/ \
Snaps are app packages for desktop, cloud and IoT that are easy to install, secure, cross‐platform and dependency‐free. Snaps are discoverable and installable from the Snap Store, the app store for Linux with an audience of millions. \

**[Q]**

**[R]**
- [rename](https://stackoverflow.com/questions/15012631/rename-files-and-directories-recursively-under-ubuntu-bash) \
  Rename files and directories recursively under ubuntu /bash
  ```
  e.g. rename all files and directories that contain the word "special" to "regular"
  
  To rename files only:
  
  find /your/target/path/ -type f -exec rename 's/special/regular/' '{}' \;
  To rename directories only:
  
  find /your/target/path/ -type d -execdir rename 's/special/regular/' '{}' \+
  To rename both files and directories:
  
  find /your/target/path/ -execdir rename 's/special/regular/' '{}' \+
  ```
  ```aidl
  rnm -rs '/.git/___git/g' -dp -1 *
  rnm -rs '/___git/.git/g' -dp -1 *
  ```
**[S]**

**[T]** \
`tail -10 go.py` \
`thunar .` - open file manager

**[U]**

**[V]**
- [variable environments](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/) 

- https://askubuntu.com/questions/866161/setting-path-variable-in-etc-environment-vs-profile

- /etc/environment is a system-wide configuration file, which means it is used by all users. It is owned by root though, so you need to be an admin user and use sudo to modify it. \
 ~/.profile is one of your own user's personal shell initialization scripts. Every user has one and can edit their file without affecting others. \
 /etc/profile and /etc/profile.d/*.sh are the global initialization scripts that are equivalent to ~/.profile for each user. The global scripts get executed before the user-specific scripts though; and the main /etc/profile executes all the *.sh scripts in /etc/profile.d/ just before it exits. \


- a) The export command will export the modified variable to the shell child process environments. \
`export PATH="$HOME/bin:$PATH"` \
b) Global shell specific configuration files such as /etc/environment and /etc/profile. Use this file if you want the new directory to be added to all system users $PATH. \
`nano /etc/environment` or `nano /etc/profile`\
  If you want to add a path (e.g. /your/additional/path) to your PATH variable for your current user only and not for all users of your computer, you normally put it at the end of ~/.profile like in one of those two examples. However, if you need to set that environment variable for all users, I would still not recommend touching /etc/environment but creating a file with the file name ending in .sh in /etc/profile.d/. The /etc/profile script and all scripts in /etc/profile.d are the global equivalent of each user's personal ~/.profile and executed as regular shell scripts by all shells during their initialization.
  ```
  PATH="/your/additional/path:$PATH"
  PATH="$PATH:/your/additional/path"
  ``` 
c) Per-user shell specific configuration files. For example, if you are using Bash, you can set the $PATH variable in the ~/.bashrc file. If you are using Zsh the file name is ~/.zshrc. \
  `nano ~/.bashrc` and `source ~/.bashrc`

`echo $PATH`

**[W]**

**[X]**
- [xdg-open .](https://www.geeksforgeeks.org/xdg-open-command-in-linux-with-examples/) \

**[Y]**

**[Z]**