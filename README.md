# Mkdocs RCE PoC

This PoC shows how to trigger an issue on MKdocs templates.

To trigger it:

1. Go in the `themename` directory
1. Do a `pip install .`
1. Go in the `my-project` directory and do `mkdocs serve`
1. See that a file called `pwned` has been created in `/tmp/`