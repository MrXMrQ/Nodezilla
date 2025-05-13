from Graph.node import Node


class Edge:
    def __init__(self, source: Node, target: Node, color: str = "#000000") -> None:
        if not isinstance(source, Node):
            raise TypeError(
                f"Invalid type for 'source': expected 'Node', got '{type(source)}' instead."
            )

        if not isinstance(target, Node):
            raise TypeError(
                f"Invalid type for 'target': expected 'Node', got '{type(target)}' instead."
            )

        if not isinstance(color, str):
            raise TypeError(
                f"Invalid type for 'color': expected 'str', got '{type(color)}' instead."
            )

        self._source: Node = source
        self._target: Node = target
        self._color: str = color

    def __str__(self) -> str:
        return f"Connection: {self._source.pos} -> {self._target.pos}, Color: {self._color}"

    @property
    def source(self) -> Node:
        return self._source

    @property
    def sourcePos(self) -> Node:
        return self._source.pos

    @property
    def target(self) -> Node:
        return self._target

    @property
    def color(self) -> Node:
        return self._color
