######################################################################
#                               INSTALL                              #
######################################################################
from Classes.Metadata import Metadata

class Install:
    def __init__(self, display_name: str, path: str, install_switches, download_type: str, directory: str, custom_install_switch, metadata: Metadata):
        self.display_name = display_name
        self.path = path
        self.install_switches = install_switches
        self.download_type = download_type
        self.directory = directory
        self.custom_install_switch = custom_install_switch
        self.metadata = metadata
