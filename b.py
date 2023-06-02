import pyson

# Define a pyson string that contains arbitrary code
pyson_string = "print('Hello world!'); os.system('ls')"

# Parse the pyson string into a pyson object
pyson_object = pyson.parse(pyson_string)

# Evaluate the pyson object using the eval function
pyson.eval(pyson_object)
