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

	# Create the directory for all repos
	if not os.path.isdir('repos'):
		path = os.path.join(base_dir, 'repos')
		os.mkdir(path)

	# process to check if object in directory is a git repo and if it's still in use
	for dir in dir_list:
		repo_path = base_dir + "/" + dir
		print(repo_path)
		if check_is_repo(repo_path):
			print("im a repo")
			if not check_if_in_use(dir, file):
				shutil.rmtree(base_dir + "/" + dir)
				print("removed " + dir)
		else:
			print("im not a repo")  # can be deleted

	# clone / pull process
	with open(file, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=' ')

		for row in reader:
			try:
				if os.path.isdir('repos/' + row[1]):
					pull_repo('repos/' + row[1])
					print('pulled ' + row[1])
				else:
					clone_repo(row[0], row[1])
					print('cloned ' + row[1])
			except Exception:
				print("Error: No Access")


def check_if_in_use(dir, file):
	with open(file, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=' ')

		for row in reader:
			if dir == row[1]:
				is_in_use = True
				return is_in_use


def check_is_repo(path):
	try:
		x = git.Repo(path).git_dir
		return True
	except git.exc.InvalidGitRepositoryError:
		return False


def clone_repo(git_url, dirname):
	repo = git.Repo.clone_from(git_url, 'repos/' + dirname)


def pull_repo(reponame):
	repo = git.Repo(reponame)
	o = repo.remotes.origin
	o.pull()


if __name__ == '__main__':
	start()
