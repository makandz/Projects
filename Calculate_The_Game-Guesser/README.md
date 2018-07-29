# Calculator: The Game - Guesser
This is a small program I made because I was getting way too lazy guessing and checking the results myself. Calculator: The Game is a game you can download from the [Play Store](https://play.google.com/store/apps/details?id=com.sm.calculateme&hl=en) or the [App Store](https://itunes.apple.com/us/app/calculator-the-game/id1243055750?mt=8).

## What does this do?
You give it a start, stop, and the buttons it's allowed to use and it'll go through all the possibilities is can and give you a proper answer that uses the shortest path it can. It isn't the most efficient of code and will get very ram hungry as it grows since there is no garbage cleanup, but for the levels I'm currently on it works very well and fast on an IDE such as Repl.it.

## How do I use it?
Run the script and you'll be prompted for inputs. The inputs go as following:

```
[Start number]
[Goal number]
[Number of functions]
[Functions type] [Function values]
```

Different functions require a different number of inputs. So if you have a function to add you'd put in `a 10` which would add the function of +10 to the system. Functions such as the swap which require 2 values would be used such as `c 2 4`, this would change all 2s to 4s in that case with the function. Below are all the working functions.

```
f       # Flips the negative/positive sign (Multiply by -1)
r       # Removes the last digit
n       # Flip the number
a 1     # Adds 1
s 1     # Subtracts 1
d 2     # Divides by 2
m 2     # Multiplies by 2
e 2     # To the exponent of 2
i 2     # Inserts 2 to the end of the value.
c 2 4   # Changes all 2s to 4s. (Swap function)
```

Below is a working example that can be solved in 2 steps.

```
1
4
2
a 2
a 1
```

## Debugging

Found an issue that you want to fix yourself or provide me with some info so I can check it out as well? Set the DEBUG variable at the top to true and it'll print everything that the program is going through. This will cause the program to slow down, sometimes to a halt and freeze if the process requires a very large queue. So be careful when using it!

Enjoy the program!
