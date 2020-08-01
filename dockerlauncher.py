import docker
import subprocess

client = docker.from_env()

print("containers:")
for i, container in enumerate(client.containers.list()):
	print(f"{i + 1}) {container}")
print("")

print("images:")
for i, image in enumerate(client.images.list()):
	print(f"{i + 1}) {image}")
print("")

print("Running docker...")
result = subprocess.run(["docker", "run", "--rm", "custompython", "python", "main.py"], stdout=subprocess.PIPE)
result = result.stdout.decode("utf-8")
print(result)
print("Done running docker")
