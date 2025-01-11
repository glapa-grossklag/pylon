# `pylon`

Python is an excellent language for writing one-off scripts.

However, sometimes your one-off scripts have a dependency or two.

Python is a less-than-excellent language for managing dependencies.

`pylon` allows you to quickly and effortlessly run one-off Python scripts with dependencies.

# Usage

A code snippet is worth one thousand words.

````python
#!/usr/bin/env pylon
"""
Notice the shebang (#!) above, to run with a dot slash.

Notice the requirements below, to feel okay when depending on others.

```requirements
rich
```
"""
import rich
import sys

name = "world" if len(sys.argv) < 2 else sys.argv[1]
rich.print(f"Hello, [blue]{name}[/]!")
````

The first time you run the script above, `pylon` will install the requirements given to a virtual environment.
The next time, you won't have to wait for an installation.
Until, of course, you add another!

