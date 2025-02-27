# Copyright 2024 NVIDIA Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
cuPyNumeric
=====

Provides a distributed task-parallel implementation of the Numpy interface
with GPU acceleration.

:meta private:
"""
from __future__ import annotations

import numpy as _np

from . import linalg, random, fft, ma
from ._array.array import ndarray
from ._array.util import maybe_convert_to_np_ndarray
from ._module import *
from ._ufunc import *
from ._utils.array import is_supported_dtype
from ._utils.coverage import clone_module

clone_module(_np, globals(), maybe_convert_to_np_ndarray)

del maybe_convert_to_np_ndarray
del clone_module
del _np

from . import _version

__version__ = _version.get_versions()["version"]  # type: ignore [no-untyped-call]
