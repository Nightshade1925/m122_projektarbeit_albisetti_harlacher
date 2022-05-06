import logging
import argparse
import time

import git
import os

from utils import Utils


# Exception classes
class LoadReposError(Exception):
	pass


class CreateOutputFileError(Exception):
	pass


logger = logging.getLogger(__name__)
base_dir = ''
output_file = ''
repos = []


def initialize():
	config = Utils.load_config()
	Utils.register_handlers(config.get('loglevel'), config.get('logpath'))


def start():
	logger.info('Extracting commits...')
	check_args()

	try:
		load_repos_from_base_dir()
		create_output_file()
		logger.info('Successfully finished extracting commits')
	except LoadReposError as e:
		logger.error(f'WARNING: Failed to load repos because {e}')
	except CreateOutputFileError as e:
		logger.error(f'WARNING: Failed to create output file because {e}')
	except Exception as e:
		logger.critical(f'ERROR: Unexpected error {e}')


def check_args():
	global base_dir, output_file
	logger.debug('Checking arguments')

	parser = argparse.ArgumentParser()
	parser.add_argument("-b", "--base-dir", type=str, help="display a square of a given number", required=True)
	parser.add_argument("-o", "--output-file", type=str, help="display a square of a given number", required=True)
	parser.add_argument("-d", "--debug", help="enable debug mode", action="store_true")
	args = parser.parse_args()

	base_dir = args.base_dir
	output_file = args.output_file

	if args.debug:
		Utils.enable_debug_flag()
		logger.debug('Debug mode enabled')

	logger.debug('Arguments check finished successfully')


def load_repos_from_base_dir():
	logger.info(f'Loading repos from base dir: {base_dir}')

	folders = Utils.get_immediate_subdirectories(base_dir)
	logger.debug(f'Found sub folders in base dir: {folders}. Loading repos...')

	for folder in folders:
		# check if folder is a git repo
		try:
			repo = git.Repo(os.path.join(base_dir, folder))
			repos.append(repo)
		except Exception as e:
			logger.debug(f'Folder {folder} is not a repo: {e}')
	# if no repos found, raise error
	if len(repos) == 0:
		raise LoadReposError(f'no git repos found in base dir: {base_dir}')


def create_output_file():
	global output_file
	logger.info(f'Creating output file: {output_file}')
	try:
		output_file = open(output_file, 'w+')
		# write header
		logger.debug('Writing header to output file')
		output_file.write('Zielverzeichnis,Datum,Commit-Hash,Author\n')
	except Exception as e:
		raise CreateOutputFileError(f'unable to write to output file: {e}')

	for repo in repos:
		repo_dir_name = os.path.basename(repo.working_tree_dir)
		logger.debug(f"Extracting commits from repo: {repo_dir_name}")
		try:
			for commit in repo.iter_commits():
				# parse commits in format:
				# name of repo, date, commit hash, author
				output_file.write(f"{repo_dir_name},"
								  f"{time.strftime('%Y%m%d', time.localtime(commit.committed_date))},"
								  f"{commit.hexsha},"
								  f"{commit.committer.name}\n")
		except Exception as e:
			output_file.close()
			raise CreateOutputFileError(f'unable to parse commits to output file for repo {repo_dir_name}: {e}')
		logger.debug(f"Finished extracting commits from repo: {repo_dir_name}")
	output_file.close()


if __name__ == '__main__':
	initialize()
	start()

