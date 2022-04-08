import argparse
import os
import csv

import git

base_dir = ""
file = ""
dir_list = ""


def start():
	parser = argparse.ArgumentParser(description='get arguments')
	parser.add_argument("-d", "--debug", help="enable debug mode", action="store_true")
	parser.add_argument("-b", "--basedir", type=str, help="set basedir", required=True)
	parser.add_argument("-f", "--file", type=str, help="get filepath", required=True)
	args = parser.parse_args()
	base_dir = args.basedir
	file = args.file
	dir_list = os.listdir(base_dir)
	print(dir_list)

	for dir in dir_list:
		if check_is_repo(base_dir + "\\" + dir) == True
			csv_file = csv.reader(open(file, "r"), delimiter=",")

def read_input_file():
	with open(file, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			print(row)


def check_if_in_use():
	with open(file, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=' ')
		is_in_use = False
		for row in reader:
			if dir == row[1]:
				is_in_use = True
				return is_in_use


def check_is_repo(path):
	try:
		_ = git.Repo(path).git_dir
		return True
	except git.exc.InvalidGitRepositoryError:
		return False


def clone_repo(git_url):
	repo = git.Repo.clone_from(git_url)


if __name__ == '__main__':
	start()
