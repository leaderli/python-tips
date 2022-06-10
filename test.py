import tempfile

fd = tempfile.TemporaryDirectory()
print(fd)
with tempfile.TemporaryDirectory() as fd:
    print(fd)

