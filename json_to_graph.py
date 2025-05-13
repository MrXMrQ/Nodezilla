from json_reader import JSONReader
from Graph.node import Node
from Graph.edge import Edge
from Graph.graph import Graph


class JSONtoGraph:
    def __init__(self) -> None:
        self._data: dict = JSONReader().data
        self._graphes = []

    def merge(self) -> None:
        for key, data in self._data.items():
            color = None

            global_settings = data.get("global_settings")
            if "color" in global_settings:
                color = global_settings["color"]

            n = []
            nodes = data.get("nodes")
            for node in nodes:
                if color:
                    node["color"] = color

                n.append(Node(**node))

            e = []
            edges = data.get("edges")
            for edge in edges:
                for i in n:
                    if i.id == edge["source"]:
                        source = i

                    if i.id == edge["target"]:
                        target = i

                if color:
                    edge["color"] = color

                e.append(Edge(source, target, color if color else "#000000"))

            self._graphes.append(Graph(n, e, **global_settings))

    @property
    def data(self) -> dict:
        return self._data

    @property
    def graphes(self) -> list[Graph]:
        return self._graphes
