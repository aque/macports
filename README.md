# MacPorts - Local Portfiles Repository

This is a repository of MacPorts Portfiles I wrote. Some of them were submitted for inclusion to the main trunk.

## Installation

1. Follow the steps to [install MacPorts](https://www.macports.org/install.php) for your specific OS X version.
2. Clone this repository and create the index files. This is the quickest way to use these Portfiles.

        $ git clone https://github.com/aque/macports.git $HOME/macports
        $ cd $HOME/macports
        $ portindex

3. Edit sources.conf

        $ sudo nano -w /opt/local/etc/macports/sources.conf

4. Add "file:///Users/USERNAME/macports" **before** the "rsync://rsync.macports.org/" line. The local ports will have a higher priority if they share the same name as ones in the offical ports tree.
5. Install a port from this repository.

        $ sudo port install pythonprop

## Bugs

Please submit any issues to the [GitHub Issues tab](https://github.com/aque/macports/issues).

## Author

Allan Que