Clone All Repos
===============

This repository allows you to create a file which will
clone all bare repositories from a filesystem.

This trawls the filesystem given a root directory to find
bare git repositories.

Once it has found them it creates a list of git repositories
and then creates a shell file to run git clone on them.

If the --my-repos flag is provided the shell script created
will also have the my repos register command for each
repository

### Checking if something is a bare git repository

For the purposes of this script I check if something
is a bare git repository by seeing if it has the following:

Folders:
* branches
* hooks
* info
* objects
* refs

Files:
* config
* description
* HEAD

If it finds these files and folders it will assume this
is a repository.

 