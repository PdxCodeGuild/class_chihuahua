# Using the CLI

CLI stands for 'command-line interface', and it was the only way to use a computer before the development of GUIs 'graphical user interface'. It's still used to perform many computer operations that go 'under the hood'.

#### Opening the CLI

In OS X, the default CLI is called `Terminal`, which you can find by typing `terminal` in search, or under `Finder -> Applications -> Utilities`.

In Windows, the default CLI is `cmd`, which you can find by typing `cmd` in search, or pressing `Windows+R`, typing `cmd`, and hitting `enter`. This will work for executing python, but there's no color differentiation, and some commands like `ls` and `rm` won't work in `cmd`. A much better CLI is [Cmder](http://cmder.net/). Another option for Windows is [Powershell](https://msdn.microsoft.com/en-us/powershell/scripting/setup/installing-windows-powershell).

In Linux, you can open a terminal with `Ctrl + Alt + T`.

#### Common CLI Commands

- `pwd` displays the path of the current directory
- `ls` lists the contents of the current directory
- `cd <directoryname>` change directory
    - `cd ..` will bring you into the parent directory
    - `cd` alone will return you to your 'home' directory
- `mkdir <foldername>` create a new folder 
- `touch <filename>` creates a new file 
- `rm -r <foldername>` removes a folder and all files
- `rm <filename>` removes a file
- `mv filename1 filename2` moves or renames a file:
- `echo <message> > file.extension` adds a message within a file you created (or creates that file if it does not exist)

Create a folder in your Desktop. Cd into that and add a file. `mkdir ~/Desktop/test && cd ~/Desktop/test && echo hello there > hello.txt`

- `cp -R hello.txt ~/Desktop` copies a file and moves into the Desktop directory
- `mv hello.txt goodbye.txt` changes the name of the file
- `mv goodbye.txt ~/Desktop` Moves the file to the Desktop directory

------

## Autocomplete

A super-handy shortcut when working with the CLI is to tab to autocomplete. Try the following (on OS X):

1. `cd ~/`
1. `ls Doc` + [tab]

The system should have autocompleted to `ls Documents/`. You can then hit [enter] to execute the command.

If the system can’t resolve the autocomplete to a single string, tab a second time to get a list of the matching options. Try the following (on OS X):

1. `cd ~/`
1. `ls D` + [tab] + [tab]

The system should have shown you `Desktop/   Documents/ Downloads/` as the possible options. Type `e` + [tab] and the system should autocomplete to `ls Desktop/`.

------

## Resources for futher reading:

1. [A very, very gentle introduction to the Linux Command Line](http://chrisyoung.net/prose/blog/posts/2009-11-28-very-very-gentle-introduction-linux-command-line/)
1. Django Girls [Introduction to the command-line interface](http://tutorial.djangogirls.org/en/intro_to_command_line/)
