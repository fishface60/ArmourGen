# GURPS ArmourGen

## Outline
This is a Python3 program that automates the rules from the *Eidetic Memory: Low-Tech Armour Design*, *Eidetic Memory: Cutting Edge Armour Design* and *Eidetic Memory: Ultra-Tech Armour Design* articles from **_GURPS Pyramid #3/52: Low-Tech II_**, **_GURPS Pyramid #3/85: Cutting Edge_** and **_GURPS Pyramid #3/96: Tech and Toys IV_**, respectively, by David L. Pulver. Input is via text in the terminal, command line or shell and output is a text block in the same interface. When inputting formating, please take care to spell and format input exactly as given in the prompts, as there is currently little to no error handling or correction for incorrect inputs.

## Installation and Running
1. Open your terminal or command line and navigate to the folder where you want to intall ArmourGen.
2. Clone the github repository to this folder by entering `git clone https://github.com/GURPSGen/ArmourGen`
3. Execute the ArmourGenerator.py script in Python by typing `python ArmourGenerator.py`. Python2 *will not work*; you may need to use the `python3` command instead of `python`, depending on your operating system.
4. Follow the command line prompts.

## Current Features
* All released materials and constructions from TL0 to TL12.
* Armour materials from **_GURPS Low-Tech_**: silk, jade and gem-quality jade. 
* Armour quality grades and features from **_GURPS Low-Tech_**: cheap, fine (expert tailoring), very fine (masterful tailoring), banded mail, fluted plate and mountain scale.
* Armour features from **_GURPS Dungeon Fantasy_**: elven mail, highly articulated and thieves' mail.

## Planned Features
* Armour sealing from *Cutting Edge Armour Design*.
* Radiation PF from *Ultra-Tech Armour Design*.
* Styling and cuts (e.g. "stylish" and "fashion original").
* Materials from **_GURPS Dungeon Fantasy_**: metoric iron, dragonbone and dragonhide.
* Materials from **_GURPS Magic_**: essential wood.
* Additional third-party material libraries.
* Automatic output of statistics into XML format for GURPS Character Sheet.
* Complex armour creation – distinct pieces with different constructions and materials layered or connected together.
* Random armour generation.
* Graphical user interface (GUI).
* Compilation into a standalone executable that doesn't need to be run from the terminal/command line.

## Bug Reports
A program like this has a large amount of things going on internally and although I try to do proper unit testing and integration tests when adding new features, I make mistakes. If you encounter any errors, bugs or inaccuracies in the program, please create a [new issue on the Github page](https://github.com/GURPSGen/ArmourGen/issues). If the error produced an error message or traceback, please include this. A traceback in the terminal/command line will normally begin with `Traceback (most recent call last):`. 

## Known Bugs
* Iron or steel plate is allowed for helmets before TL4 but the program cannot currently check for this, so making TL3 iron or steel helmets will fail. This can be fixed when a more sophisticated solution for tracking armour locations is implemented. In the meantime, the easiest workaround when making iron or steel helmets is to set the armour as TL4, then use TL2 or TL3 materials. Don't set the TL any higher as the cost of iron and steel is reduced at TL5 and above.
* Legality Class is not calculated for any armour. There are no concrete rules on this at TL0-TL8, so this will remain until rules for this TL range are created/found/conjured from the mind of Kromm.

## Legal Information and Credits
GURPS is a trademark of Steve Jackson Games, and its rules and art are copyrighted by Steve Jackson Games. All rights are reserved by Steve Jackson Games. This game aid is the original creation of CTA and is released for free distribution, and not for resale, under the permissions granted in the [Steve Jackson Games Online Policy](http://www.sjgames.com/general/online_policy.html).

While I don't know whether I am permitted to add a Creative Commons license to my work in addition to the required Steve Jackson Games legal notice, I would like anyone who looks at or modifies this sourcecode to act in the spirit of the [Attribution-NonCommercial-ShareAlike (BY-NC-SA)](https://creativecommons.org/licenses/by-nc-sa/4.0/) version of the Creative Commons license.

The cover image is *Portrait of a Young Bearded Man Wearing Armour* by Tintoretto, which is in the public domain.
