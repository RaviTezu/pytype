from typing import Any
# Copyright (c) 2016 Google Inc. (under http://www.apache.org/licenses/LICENSE-2.0)
def f1(a, b : int):
    pass

def f2(a, b) -> int:
    pass

def f3(a):
    # type: (Any) -> r3
    pass

def f4(a, b):
    # type: (e4, Any) -> None
    pass

def f5(a):
    # type: (Any) -> Any
    pass
