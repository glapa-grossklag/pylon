# `pylon`

Python is an excellent language for writing one-off scripts.

However, sometimes your one-off scripts have a dependency or two.

Python is (on it's own) a slightly less-than-excellent language for managing a dependency or two.

`pylon` allows you to quickly and effortlessly run one-off Python scripts with dependencies.

# Usage

A code snippet is worth one thousand words.

    #!/usr/bin/env pylon
    """
    hello.py

    Say hello to the world or to someone you love.

    ```requirements
    rich
    ```
    """
    import rich
    import sys

    name = "world" if len(sys.argv) < 2 else sys.argv[1]
    rich.print(f"Hello, [blue]{name}[/]!")

The first time you run `hello.py`, `pylon` will install the requirements given and run the script.
The next time, you won't have to wait for an installation.
Until, of course, you add another!

