A Convenient Command-line Dicebag
===

Haven't you always wished that you could roll dice in the command line? Don't you hate those GUI dice rollers, with their fancy-shmancy rolling animations, and dice that you have to *click* on to roll? Haven't you always wished you could just type `1d10 14d4 +23` and have it just WORK?

Well then this is the dicebag for you. It even allows you to define custom dice, so you can type in `dagger sneak-attack` and have it roll `1d4 3d6 +2`, or for those of us who like to be concise, `d sa`.

Usage
===

To start the program, run `python dicebag.py [filename]` where filename is the optional name of the file that contains custom dice definitions.

For basic usage, just type out whatever dice you want to roll. Dice are seperated by spaces, and in the format `xdy`, where x is the number of dice you wish to roll, and y is the number of sides each dice has. Modifiers start with a `+` or `-`, and are just integers that are added to the final result. To roll a custom die, just type its name, for instance `dagger`.

The commands available are `new`, `del`, `open`, `list`, `roll`, and `exit`.

`new` creates or modifies a custom die. Example usage: `new dagger 1d4 +2`.

`del` deletes a custom die. Example usage: `del dagger`.

`open` reads a file containing descriptions for custom dice. Example usage: `open leo.dice`.

`list` prints out all the custom dice you have defined. Example usage: `list`.

`roll` rolls dice. Typing in `roll dagger` is the same as typing in `dagger`, so this is fairly superfluous. Example usage: `roll dagger 1d6 +10`, or `dagger 1d6 +10`.

`exit` exits the program, automatically saving if you have already opened a file or prompting to save if you haven't. Example usage: `exit`.

Forking
===

Feel free to fork this, and if you do anything interesting with it send me a pull request.
