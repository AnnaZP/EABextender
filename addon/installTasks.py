# EAB Extender installation tasks

# Provides needed routines during add-on installation and removal.
# Routines are partly based on other add-ons,
# particularly Golden Cursor (thanks add-on authors).
# File copying operation comes from StationPlaylist Studio add-on by Joseph Lee.

import os
import shutil


def onInstall():
	profiles = os.path.join(os.path.dirname(__file__), "..", "EABextender", "Profiles")
	# Without importing old positions, saved positions would be lost.
	newProfiles = os.path.join(os.path.dirname(__file__), "Profiles")
	# Migrate positions database.
	if os.path.exists(profiles):
		try:
			shutil.copytree(profiles, newProfiles)
		except (IOError, WindowsError):
			pass
