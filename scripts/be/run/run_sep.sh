# You can combine two commands by grouping it with { } :

{ command1 & command2; }
# so far, you can redirect the group to a file (last ; before } is mandatory), and the space between the open and closing bracket too.

{ command1 & command2; } > new_file
# if you want to separate STDOUT and STDERRin two files :

{ command1 & command2; } > STDOUT_file 2> STDERR_file
#If you don't want to run the first command in the background, use this form :

{ command1; command2; }
#or

{ command1 && command2; }
#to run the second command only if the first is a success


# run and deattach
# subl ~/.zshrc </dev/null &>/dev/null &"