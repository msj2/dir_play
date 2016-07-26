#/usr/bin/python
from subprocess import call

import os
#Traceback (most recent call last):
  #File "mkdir.py", line 3, in <module>
    #call(["mkdir m1"])
  #File "/usr/lib/python2.7/subprocess.py", line 522, in call
    #return Popen(*popenargs, **kwargs).wait()
  #File "/usr/lib/python2.7/subprocess.py", line 710, in __init__
    #errread, errwrite)
  #File "/usr/lib/python2.7/subprocess.py", line 1327, in _execute_child
    #raise child_exception
#OSError: [Errno 2] No such file or directory

#call(["mkdir m1"])

#	works fine...
#call(["ls", "-l"])


os.system("mkdir 1")



##import subprocess

##p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
##for line in p.stdout.readlines():
    ##print line,
##retval = p.wait()

###http://stackoverflow.com/questions/89228/calling-an-external-command-in-python


##Here's a summary of the ways to call external programs and the advantages and disadvantages of each:

##os.system("some_command with args") passes the command and arguments to your system's shell. This is nice because you can actually run multiple commands at once in this manner and set up pipes and input/output redirection. For example:

##os.system("some_command < input_file | another_command > output_file")  
##However, while this is convenient, you have to manually handle the escaping of shell characters such as spaces, etc. On the other hand, this also lets you run commands which are simply shell commands and not actually external programs. See the documentation.
##stream = os.popen("some_command with args") will do the same thing as os.system except that it gives you a file-like object that you can use to access standard input/output for that process. There are 3 other variants of popen that all handle the i/o slightly differently. If you pass everything as a string, then your command is passed to the shell; if you pass them as a list then you don't need to worry about escaping anything. See the documentation.
##The Popen class of the subprocess module. This is intended as a replacement for os.popen but has the downside of being slightly more complicated by virtue of being so comprehensive. For example, you'd say:

##print subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read()
##instead of:

##print os.popen("echo Hello World").read()
##but it is nice to have all of the options there in one unified class instead of 4 different popen functions. See the documentation.
##The call function from the subprocess module. This is basically just like the Popen class and takes all of the same arguments, but it simply waits until the command completes and gives you the return code. For example:

##return_code = subprocess.call("echo Hello World", shell=True)  
##See the documentation.
##If you're on Python 3.5 or later, you can use the new subprocess.run function, which is a lot like the above but even more flexible and returns a CompletedProcess object when the command finishes executing.
##The os module also has all of the fork/exec/spawn functions that you'd have in a C program, but I don't recommend using them directly.
##The subprocess module should probably be what you use.

##Finally please be aware that for all methods where you pass the final command to be executed by the shell as a string and you are responsible for escaping it. There are serious security implications if any part of the string that you pass can not be fully trusted. For example, if a user is entering some/any part of the string. If you are unsure, only use these methods with constants. To give you a hint of the implications consider this code:

##print subprocess.Popen("echo %s " % user_input, stdout=PIPE).stdout.read()
##and imagine that the user enters "my mama didnt love me && rm -rf /".
