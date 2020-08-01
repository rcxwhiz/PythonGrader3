import termwrap

REPOTAG = "python:3.8-slim"
CONTAINER_NAME = "python-grader3"
IMAGE_NAME = "python-grader"


def start_container():
	print("Creating a docker container...")
	args = ["docker", "run", "-it", "-d", "--name", CONTAINER_NAME, IMAGE_NAME]
	if "Unabled to find image" in termwrap.run(args):
		termwrap.run(["docker", "build", "--tag", IMAGE_NAME, "."])
		termwrap.run(args)


def end_container():
	print("Stopping a docker container...")
	termwrap.run(["docker", "stop", CONTAINER_NAME])


def del_container():
	print("Deleting a docker container...")
	termwrap.run(["docker", "rm", CONTAINER_NAME])


class DockerWrap:
	def __init__(self, cls):
		self._cls = cls
		start_container()
		self.del_container = False

	def __del__(self):
		end_container()
		if self.del_container:
			del_container()

	def get_instance(self):
		try:
			return self._instance
		except AttributeError:
			self._instance = self._cls()
			return self._instance

	def __call__(self):
		raise TypeError("Singleton accessed through get_instance()")

	def __instancecheck__(self, instance):
		return isinstance(instance, self._cls)

	def run_py_script(self, script_name):
		termwrap.run(["docker", "cp", script_name, f"{CONTAINER_NAME}:/{script_name}"])
		return termwrap.run(["docker", "exec", "-it", CONTAINER_NAME, "python", script_name])

