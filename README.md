# gimp-autosave
Script to add auto-save functionality to GIMP

GIMP is great software, and much more stable than it used to be.   But I've been working on a laptop with a bad battery for a bit now and have lost quite a bit of work due to the laptop becoming unplugged.   I have no idea why this isn't a standard feature or why there isn't already a conveniently available plug-in at least. I found an antiquated script to implement autosaving in GIMP somewhere amongst the interwebz and was able to get it updated and compatible with the latest version of GIMP, 2.10.22 as of this writing.

Put this .py file in your [user home]/GIMP/2.10/plug-ins directory, and make sure it has been set to executable.   It should register upon launching gimp, and you will find the "Activate auto-save" option in the File menu.

Credit to the original author is included in the comments of the script, I am only responsible for updating it to work with the latest version of GIMP and the latest version of python.
