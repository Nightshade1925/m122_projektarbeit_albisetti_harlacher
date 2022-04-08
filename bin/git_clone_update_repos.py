import argparse
import os
import csv
import shutil

import git

base_dir = ""
file = ""
dir_list = ""
is_in_use = False


def start():
	parser = argparse.ArgumentParser(description='get arguments')
	parser.add_argument("-d", "--debug", help="enable debug mode", action="store_true")
	parser.add_argument("-b", "--basedir", type=str, help="set basedir", required=True)
	parser.add_argument("-f", "--file", type=str, help="get filepath", required=True)
	args = parser.parse_args()
	base_dir = args.basedir
	file = args.file
	# dirname = os.path.dirname(__file__)
	# filename = os.path.join(dirname, '../etc/'+file)
	dir_list = os.listdir(base_dir)

	for dir in dir_list:
		# with open(file, newline='') as csvfile:
		# 	opened_file = csv.reader(csvfile, delimiter=' ', quotechar=' ')
		# 	for row in opened_file:
		# 		print(row[0])

		repo_path = base_dir + "\\" + dir
		print(repo_path)
		if check_is_repo(repo_path):
			print("successfully pulled")
			# if check_if_in_use(dir, file):
				# repo = git.Repo(dir)
				# o = repo.remotes.origin
				# o.pull()

			# else:
			# 	shutil.rmtree(base_dir + "\\" + dir)
			# 	print("removed " + dir)
		else:
			print("im not a repo")


def read_input_file():
	with open(file, newline='') as csvfile:
		opened_file = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in opened_file:
			print(row[1])


def check_if_in_use(dir, file):
	with open(file, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=' ')

		for row in reader:
			if dir == row[1]:
				is_in_use = True
				return is_in_use


def check_is_repo(path):
	try:
		x = git.Repo(path)
		return True
	except Exception:
		return False


def clone_repo(git_url):
	repo = git.Repo.clone_from(git_url)


if __name__ == '__main__':
	start()
