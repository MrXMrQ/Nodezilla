from Graph.edge import Edge
from Graph.node import Node


class Graph:
    def __init__(
        self,
        nodes: list[Node],
        edges: list[Edge],
        name: str = "Graph",
        color: str = "#000000",
        visible: bool = True,
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
        self._visible = visible

    def __str__(self) -> None:
        return f"Name: {self._name} \nColor: {self._color}\nNodes: {[f"{x}" for x in self._nodes]} \nEdges: {[f"{x}" for x in self._edges]}\n"

    def __eq__(self, value) -> None:
        if not isinstance(value, Graph):
            raise TypeError(
                f"Invalid 'value to compare': expected a Graph, got {value!r}"
            )

        if not len(self._nodes) == len(value._nodes) or not len(self._edges) == len(
            value._edges
        ):
            return False

        return True

    @property
    def nodes(self) -> list[Node]:
        return self._nodes

    @property
    def edges(self) -> list[Edge]:
        return self._edges

    @property
    def name(self) -> str:
        return self._name

    @property
    def color(self) -> str:
        return self._color

    @property
    def visible(self) -> bool:
        return self._visible

    @visible.setter
    def visible(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError(
                f"Invalid type for 'visible': expected 'bool', got '{type(value)}' instead."
            )
        self._visible = value
