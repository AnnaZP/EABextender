# EAB Extender#

forked from:  golden cursor

* Author: LUMEN PL
* NVDA compatibility: 2019.3 and beyond

#Description#
This add-on allows users to assign custom keyboard shortcuts to the Easy-Access Bar (EAB) on Papenmeier braille devices. The add-on automatically recognizes the active application, allowing multiple EAB configurations to be created for each application.  It is possible to quickly switch between multiple configurations for a given application, thereby greatly expanding the functionality of the EAB. For example one configuration can be used to move the Braille display in a text document, while another configuration can be configured for navigating the applications menu.

#Compatible devices#
The following is a list of compatible Papenmeier devices:

* BRAILLEX Live / Live + / Live 20
* BRAILLEX Trio
* BRAILLEX EL 40c/60c/80c
* BRAILLEX 40s/66s/80s

#Definitions#
For definitions of the keys listed in this document, please consult the device’s instruction manual.

#Default settings#
By default, the Papenmeier device uses the standard NVDA settings for the EAB, which are applied when a new configuration is created. Below a list of the EAB settings in a default configuration.

* EAB left: moves the display to the left
* EAB right: moves the braille display to the right
* EAB up: moves the braille display one column up
* EAB down: moves the braille display one column down
* Routing + EAB left: Moves the navigator object to the previous object
* Routing + EAB right: Moves the navigator object to the next object
* Routing + EAB up: Moves the navigator object to the parent object
* Routing + EAB down: Moves the navigator object to the first child object

#Main menu window#
In order to bring up the main menu press the R1 button located on the Papenmeier Braille device. This menu can be easily navigated by using the EAB. While in the EAB Extender menu the eab behaves in the following way:

* Pressing the EAB up, down, left or right emulates the up and down arrows, which allows scrolling through the available configurations.
* Routing key + EAB right emulates the Tab key which scrolls through the various buttons of the window.
* Routing key + EAB left: emulates the pressing of Shift+Tab which scrolls through the various buttons of the window in the reverse order.
* Routing key + EAB down: Emulates the enter key
* Routing key + EAB up: Emulates the Esc key

#Main menu buttons#
* OK: Pressing this key activates the selected configuration and closes the window.
* Define: Allows to define the keyboard shortcuts in a configuration.
* Change name: Changes the name of the selected configuration
* Delete: Deletes the selected configuration
* New: Creates a new configuration and opens a dialog box for naming the new configuration.
* Close: Exits the menu without changes

#Configuration window#
This window displays the eight EAB positions that can have custom keyboard shortcuts assigned to them.

* Use the arrow keys to select a EAB position.
* Press Enter on a position to activate key capture mode, then press the desired keyboard shortcut to assign it to the selected position.
* Once done, select OK to save or Close to exit without saving.

#Braille settings#
Pressing the L2 button brings up a NVDA menu containing the Braille settings.