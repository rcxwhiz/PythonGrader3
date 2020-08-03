import re

name_re = re.compile(r"([^_]+)_([^_]+)_([^_]+)([^.]*).(.*)")


def file_re(file_name):
	result = re.search(name_re, file_name)
	if result is None:
		return None
	return {"last_name": result[0],
	        "first_name": result[1],
	        "net_id": result[2],
	        "file_name": result[3],
	        "file_extenstion": result[4]}
