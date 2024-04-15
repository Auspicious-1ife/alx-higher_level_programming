#!/usr/bin/python3
def lookup(obj):
# Get the list of all attributes and methods of the object
all_attrs = dir(obj)
# Initialize an empty list to store public attributes and methods
public_attrs = []
# Iterate through all attributes/methods
for attr in all_attrs:
# Check if the attribute/method is not private (doesn't start with double underscore)
if not attr.startswith("__"):
# Add the attribute/method to the list of public attributes/methods
public_attrs.append(attr)
# Return the list of public attributes/methods
return (public_attrs)
