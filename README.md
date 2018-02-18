Clone All Repos
===============

This repository allows you to create a file which will
clone all bare repositories from a filesystem.

This trawls the filesystem given a root directory to find
bare git repositories.

Once it has found them it creates a list of git repositories
and then creates a shell file to run git clone on them.

If the `--my-repos` flag is provided the shell script created
will also have the my repos register command for each
repository

## Examples

```
Command:
python get_clone_script.py ~/Documents/git/ hostname --mr-register

Output:
git clone foobar:~/Documents/git/repo1.git repo1.git
mr register repo1.git
git clone foobar:~/Documents/git/subdir/repo2.git subdir/repo2.git
mr register subdir/repo2.git
```

Here we print out the commands to stdout which can be piped to a file to run on a remote host.

## Future Improvements

One of the improvements I am going to add in the future is
to add some better logic for finding and checking repositories.

The current logic for finding repositories is probably sufficient
but I could add further logic to run a git command and check
to see if it identifies it as a git repository.

### Logic for Checking if something is a bare git repository

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

 