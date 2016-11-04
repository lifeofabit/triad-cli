"""
triad

Usage:
  triad hello
  triad -h | --help
  triad --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  triad hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/rdegges/skele-cli
"""

from inspect import getmembers, isclass
from docopt import docopt

from . import __version__ as VERSION

def main():
	import commands
	options = docopt(__doc__, version=VERSION)

	for k,v in options.iteritems():
		if hasattr(commands, k):
			module = getattr(commands, k)
			commands = getmembers(module, isclass)
			command = [command[1] for command in commands if command[0] != 'Base'][0]
			command = command(options)
			command.run()

