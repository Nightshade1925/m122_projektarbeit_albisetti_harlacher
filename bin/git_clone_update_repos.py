import argparse
import os
import csv
import shutil
import git
import logging
from utils import Utils

logger = logging.getLogger('__main__')
config = Utils.load_config()
print(config.get("loglevel"))
print(config.get("logpath"))
Utils.register_handlers(config.get("loglevel"), config.get("logpath"))
base_dir = ""
file = ""
dir_list = ""


def start():
	logger.debug('Checking arguments')
	parser = argparse.ArgumentParser(description='get arguments')
	parser.add_argument("-d", "--debug", help="enable debug mode", action="store_true")
	parser.add_argument("-b", "--basedir", type=str, help="set basedir", required=True)
	parser.add_argument("-f", "--file", type=str, help="get filepath", required=True)
	args = parser.parse_args()
	base_dir = args.basedir
	file = args.file

	if args.debug:
		print("Debug mode on")
		Utils.enable_debug_flag()
	# Create the directory for all repos
	# if not os.path.isdir(base_dir + '/repos'):
	# 	path = os.path.join(base_dir, 'repos')
	# 	os.mkdir(path)

	# get a list of directory
	dir_list = os.listdir(base_dir)

	# process to check if object in directory is a git repo and if it's still in use
	for dir in dir_list:
		repo_path = base_dir + '/' + dir
		logger.debug(repo_path)
		if check_is_repo(repo_path):
			logger.debug("im a repo")
			in_use = check_if_in_use(dir, file)
			if not in_use:
				try:
					shutil.rmtree(base_dir + "/" + dir)
					logger.info("removed " + dir)
				except Exception:
					logger.warning("No permission to delete " + dir)
		else:
			logger.debug("im not a repo")

	# clone / pull process
	with open(file, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=' ')

		for row in reader:
			if os.path.isdir(base_dir + '/' + row[1]):
				try:
					os.chdir(base_dir)
					pull_repo(row[1])
					logger.info('pulled ' + row[1])
				except Exception:
					logger.warning("Couldn't pull " + row[0])
			else:
				try:
					os.chdir(base_dir)
					clone_repo(row[0], row[1])
					logger.info('cloned ' + row[1])
				except Exception:
					logger.warning("Couldn't clone " + row[0])


def check_if_in_use(dir, file):
	with open(file, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=' ')
		for row in reader:
			if dir == row[1]:
				return True
		return False


def check_is_repo(path):
	try:
		x = git.Repo(path).git_dir
		return True
	except git.exc.InvalidGitRepositoryError:
		return False


def clone_repo(git_url, dirname):
	repo = git.Repo.clone_from(git_url, dirname)


def pull_repo(reponame):
	repo = git.Repo(reponame)
	o = repo.remotes.origin
	o.pull()


if __name__ == '__main__':
	start()
