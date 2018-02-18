import os
import argparse

git_prefix = "git clone"
hostname = "hostname"
clone_dir = "."
mr_register = True

git_dir = "/gitthings/"


def find_all_git_repos(directory):
    for d in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, d, "info")):
            print_git(os.path.join(directory, d))
        else:
            find_all_git_repos(os.path.join(directory, d))


def is_git_bare_repo(directory):
    dirs_to_check = ["branches", "hooks", "info", "objects", "refs"]
    files_to_check = ["config", "description", "HEAD"]

    for dir in dirs_to_check:
        if not os.path.isdir(os.path.join(directory, dir)):
            return False

    for filename in files_to_check:
        if not os.path.isfile(os.path.join(directory, filename)):
            return False

    return True


def print_git(directory):
    print git_prefix + " " + hostname + ":" + directory + " " + directory[len(git_dir):]
    if mr_register:
        print "mr register " + directory[len(git_dir):]


find_all_git_repos(git_dir)

