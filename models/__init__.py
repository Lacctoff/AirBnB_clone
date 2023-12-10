#!/usr/bin/python3
"""
Package initializer
"""


from models.engine.file_storage import storage

# Call reload() method on the storage variable
storage.reload()
