import argparse
import git
import os

base_dir = ""
output_file = ""
repos = []


def start():
	global base_dir, output_file
	parser = argparse.ArgumentParser()
	parser.add_argument("-b", "--base-dir", type=str, help="display a square of a given number", required=True)
	parser.add_argument("-o", "--output-file", type=str, help="display a square of a given number", required=True)
	parser.add_argument("-d", "--debug", help="enable debug mode", action="store_true")
	args = parser.parse_args()

	base_dir = args.base_dir
	output_file = args.output_file

	if args.debug:
		print("Debug mode on")

	load_repos_from_base_dir()


def get_immediate_subdirectories(a_dir):
	return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]


def load_repos_from_base_dir():
	global base_dir, repos

	folders = get_immediate_subdirectories(base_dir)

	for folder in folders:
		# check if folder is a git repo
		try:
			repo = git.Repo(os.path.join(base_dir, folder))
			repos.append(repo)
		except Exception as e:
			print(f"Folder {folder} is not a repo: {e}")

	if len(repos) == 0:
		print("No git repos found")
		return

	create_output_file()


def create_output_file():
	global output_file

	with open(output_file, "w") as f:
		f.write("")


if __name__ == '__main__':
	start()
