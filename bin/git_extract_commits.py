import logging
import argparse
import time

import git
import os

from utils import Utils

class GitExtractCommits:
	logger = logging.getLogger(__name__)

	def __init__(self):
		config = Utils.load_config()
		print(config.get("loglevel"))
		print(config.get("logpath"))

		Utils.register_handlers(config.get("loglevel"), config.get("logpath"))

		self.base_dir = ""
		self.output_file = ""
		self.repos = []

	def start(self):
		self.logger.debug('Git Extract Commits started')

		self.check_args()

		try:
			self.load_repos_from_base_dir()
			self.create_output_file()
		except LoadReposError as e:
			self.logger.error(f'Failed to load repos: {e}')
		except CreateOutputFileError as e:
			self.logger.error(f'Failed to create output file: {e}')
		except Exception as e:
			self.logger.error(f"Unexpected error: {e}")

	def check_args(self):
		self.logger.debug('Checking arguments')

		parser = argparse.ArgumentParser()
		parser.add_argument("-b", "--base-dir", type=str, help="display a square of a given number", required=True)
		parser.add_argument("-o", "--output-file", type=str, help="display a square of a given number", required=True)
		parser.add_argument("-d", "--debug", help="enable debug mode", action="store_true")
		args = parser.parse_args()

		self.base_dir = args.base_dir
		self.output_file = args.output_file

		if args.debug:
			print("Debug mode on")
			Utils.enable_debug_flag()

	def load_repos_from_base_dir(self):
		self.logger.info(f'Loading repos from base dir: {self.base_dir}')
		folders = Utils.get_immediate_subdirectories(self.base_dir)
		self.logger.debug(f'Found sub folders in base dir: {folders}. Loading repos...')

		for folder in folders:
			# check if folder is a git repo
			try:
				repo = git.Repo(os.path.join(self.base_dir, folder))
				self.repos.append(repo)
			except Exception as e:
				self.logger.debug(f'Folder {folder} is not a repo: {e}')

		if len(self.repos) == 0:
			raise LoadReposError(f'no git repos found in base dir: {self.base_dir}')

	def create_output_file(self):
		self.logger.info(f'Creating output file: {self.output_file}')
		try:
			output_file = open(self.output_file, "w+")
			# write header
			output_file.write("Zielverzeichnis,Datum,Commit-Hash,Author")
		except Exception as e:
			raise CreateOutputFileError(f'unable to write to output file: {e}')

		for repo in self.repos:
			try:
				for commit in repo.iter_commits():
					output_file.write(f"{os.path.dirname(repo)},"
									  f"{time.strftime('%Y%m%d', time.localtime(commit.committed_date))},"
									  f"{commit.hexsha},"
									  f"{commit.committer.name}\n")
			except Exception as e:
				raise CreateOutputFileError(f'unable to parse commits to output file: {e}')
		output_file.close()

if __name__ == '__main__':
	script = GitExtractCommits()
	script.start()

class LoadReposError(Exception):
	pass

class CreateOutputFileError(Exception):
	pass