import argparse
import os

import git

base_dir = ""
file_path = ""
dir_list = ""


def start():
	parser = argparse.ArgumentParser(description='get arguments')
	parser.add_argument("-d", "--debug", help="enable debug mode", action="store_true")
	parser.add_argument("-b", "--basedir", type=str, help="set basedir", required=True)
	#parser.add_argument("-f", "--file", type=str, help="get filepath", required=True)
	args = parser.parse_args()
	base_dir = args.basedir
	#file_path = args.file
	dir_list = os.listdir(base_dir)
	print(dir_list)


# def check_is_repo():


def clone_repo():
	repo = git.Repo.clone_from()


if __name__ == '__main__':
	start()
