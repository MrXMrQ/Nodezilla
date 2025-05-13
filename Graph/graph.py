from Graph.edge import Edge
from Graph.node import Node


class Graph:
    def __init__(
        self,
        nodes: list[Node],
        edges: list[Edge],
        name: str = "Graph",
        color: str = "#000000",
    ) -> None:
        if not (isinstance(nodes, list) and all(isinstance(x, Node) for x in nodes)):
            raise TypeError(f"Invalid 'nodes': expected a list of Nodes, got {nodes!r}")

        if not (isinstance(edges, list) and all(isinstance(x, Edge) for x in edges)):
            raise TypeError(f"Invalid 'edges': expected a list of Edges, got {edges!r}")

        if not isinstance(name, str):
            raise TypeError(
                f"Invalid type for 'name': expected 'str', got '{type(name)}' instead."
            )

        if not isinstance(color, str):
            raise TypeError(
                f"Invalid type for 'color': expected 'str', got '{type(color)}' instead."
            )

        self._nodes = nodes
        self._edges = edges
        self._name = name
        self._color = color

    def __str__(self) -> None:
        return f"Name: {self._name} \nColor: {self._color}\nNodes: {[f"{x}" for x in self._nodes]} \nEdges: {[f"{x}" for x in self._edges]}\n"
