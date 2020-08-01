"""
1) open a zip of student files
- unzip the files and use regex to get names

2) run them
- run each file in docker with the name
- make a list of packages that will be installed with docker
- have something nice print while the docker stuff runs
- figure out if docker will be restarted between each student

3) get the outputs
- echo the output or capture it somehow
- could maybe compare graph images?

4) optional - compare those outputs to a key
- would need to figure out the policy on inputs and outputs..?
- ideally you would be able to do multiple files with multiple inputs
- if you were going to automatically grade parts it would be easiest
- if it was going to automatically grade it should generate the csv to upload to LS

5) display the outputs
- need some way to page through them... maybe through a webpage?
- it could automatically bring up a diffchecker with the results?

QUICK AND DIRTY FOR MY NEEDS:
I just need something that can run notebook files top to bottom
"""


def run_scripts(docker_wrap, scripts):
	responses = []
	for script in scripts:
		responses.append(docker_wrap.run_py_script(script))
	return responses


if __name__ == "__main__":
	print("test")
