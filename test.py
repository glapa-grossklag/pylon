#!/usr/bin/env pylon
"""
Say hello to the world or to someone you love.

```requirements
rich
numpy
cobs
```
"""
import rich
import sys
import numpy as np

name = "world" if len(sys.argv) < 2 else sys.argv[1]
rich.print(f"Hello, [blue]{name}[/]!")

print(np.random.rand(3, 3))
