import subprocess


def run(args):
	return subprocess.run(args).stdout.decode("utf-8")
