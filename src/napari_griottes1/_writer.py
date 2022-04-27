"""
This module is an example of a barebones writer plugin for napari.

It implements the Writer specification.
see: https://napari.org/plugins/stable/guides.html#writers

Replace code below according to your needs.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Sequence, Tuple, Union

import networkx as nx

if TYPE_CHECKING:
    DataType = Union[Any, Sequence[Any]]
    FullLayerData = Tuple[DataType, dict, str]


def save_graph(path: str, data: FullLayerData):
    """Writes a single layer graph"""
    shapes, meta, tpe = data
    nx.write_gpickle(meta["graph"], path)
