class Node:
    def __init__(
        self, pos: tuple[int, int], label: str = "Node", color: str = "#000000"
    ) -> None:
        if not (
            isinstance(pos, tuple)
            and len(pos) == 2
            and all(isinstance(x, int) for x in pos)
        ):
            raise TypeError(
                f"Invalid 'pos': expected a tuple of two integers, got {pos!r}"
            )

        if not isinstance(label, str):
            raise TypeError(
                f"Invalid type for 'label': expected 'str', got '{type(label)}' instead."
            )

        if not isinstance(color, str):
            raise TypeError(
                f"Invalid type for 'color': expected 'str', got '{type(color)}' instead."
            )

        self._pos: tuple[int, int] = pos
        self._x: int = pos[0]
        self._y: int = pos[1]

        self._label: str = label
        self._color: str = color

    @property
    def pos(self) -> tuple[int, int]:
        return self._pos

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def label(self) -> str:
        return self._label

    @property
    def color(self) -> str:
        return self._color
