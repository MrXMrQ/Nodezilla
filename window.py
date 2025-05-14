import customtkinter as ctk
import random
import matplotlib.patches as mpatches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from JSONTools.json_to_graph import JSONtoGraph
from Graph.graph import Graph
from Graph.edge import Edge
from Graph.node import Node


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Graph Manager")
        self.geometry("1000x700")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self._x_min = -10
        self._x_max = 10
        self._y_min = -10
        self._y_max = 10

        self._graphes = []

        self.create_widgets()
        self.update_plot()

    def create_widgets(self) -> None:
        self._main_frame = ctk.CTkFrame(self)
        self._main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self._settings_frame = ctk.CTkFrame(self._main_frame)
        self._settings_frame.pack(side="top", fill="x", padx=5, pady=5)

        self._x_label = ctk.CTkLabel(self._settings_frame, text="X-Achse:")
        self._x_label.grid(row=0, column=0, padx=5, pady=5)

        self._x_min_label = ctk.CTkLabel(self._settings_frame, text="Min:")
        self._x_min_label.grid(row=0, column=1, padx=5, pady=5)

        self._x_min_entry = ctk.CTkEntry(self._settings_frame, width=60)
        self._x_min_entry.grid(row=0, column=2, padx=5, pady=5)
        self._x_min_entry.insert(0, str(self._x_min))

        self._x_max_label = ctk.CTkLabel(self._settings_frame, text="Max:")
        self._x_max_label.grid(row=0, column=3, padx=5, pady=5)

        self._x_max_entry = ctk.CTkEntry(self._settings_frame, width=60)
        self._x_max_entry.grid(row=0, column=4, padx=5, pady=5)
        self._x_max_entry.insert(0, str(self._x_max))

        self._y_label = ctk.CTkLabel(self._settings_frame, text="Y-Achse:")
        self._y_label.grid(row=1, column=0, padx=5, pady=5)

        self._y_min_label = ctk.CTkLabel(self._settings_frame, text="Min:")
        self._y_min_label.grid(row=1, column=1, padx=5, pady=5)

        self._y_min_entry = ctk.CTkEntry(self._settings_frame, width=60)
        self._y_min_entry.grid(row=1, column=2, padx=5, pady=5)
        self._y_min_entry.insert(0, str(self._y_min))

        self._y_max_label = ctk.CTkLabel(self._settings_frame, text="Max:")
        self._y_max_label.grid(row=1, column=3, padx=5, pady=5)

        self._y_max_entry = ctk.CTkEntry(self._settings_frame, width=60)
        self._y_max_entry.grid(row=1, column=4, padx=5, pady=5)
        self._y_max_entry.insert(0, str(self._y_max))

        self._update_button = ctk.CTkButton(
            self._settings_frame, text="Update", command=self.update_plot
        )
        self._update_button.grid(row=0, column=5, rowspan=2, padx=10, pady=5)

        self._graph_control_frame = ctk.CTkFrame(self._main_frame)
        self._graph_control_frame.pack(side="left", fill="y", padx=5, pady=5)

        self._graph_list_label = ctk.CTkLabel(
            self._graph_control_frame, text="Geladene Graphen:"
        )
        self._graph_list_label.pack(padx=10, pady=(10, 5))

        self._graph_list_frame = ctk.CTkScrollableFrame(
            self._graph_control_frame, width=200, height=300
        )
        self._graph_list_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self._graph_buttons_frame = ctk.CTkFrame(self._graph_control_frame)
        self._graph_buttons_frame.pack(fill="x", padx=10, pady=5)

        self._load_json_graph_button = ctk.CTkButton(
            self._graph_buttons_frame,
            text="JSON Graph",
            command=self.load_json_graph,
        )
        self._load_json_graph_button.pack(fill="x", padx=5, pady=2)

        self._random_button = ctk.CTkButton(
            self._graph_buttons_frame,
            text="Random graph",
            command=self.create_random_graph,
        )
        self._random_button.pack(fill="x", padx=5, pady=2)

        self._clear_button = ctk.CTkButton(
            self._graph_buttons_frame,
            text="Clear",
            command=self.clear_all_graphs,
            fg_color="#FF5555",
            hover_color="#AA3333",
        )
        self._clear_button.pack(fill="x", padx=5, pady=2)

        self._plot_frame = ctk.CTkFrame(self._main_frame)
        self._plot_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        self._figure = Figure(figsize=(5, 4), dpi=100)
        self._plot = self._figure.add_subplot(111)

        self._canvas = FigureCanvasTkAgg(self._figure, master=self._plot_frame)
        self._canvas.get_tk_widget().pack(fill="both", expand=True)

    def update_graph_list(self) -> None:
        for widget in self._graph_list_frame.winfo_children():
            widget.destroy()

        for i, graph in enumerate(self._graphes):
            frame = ctk.CTkFrame(self._graph_list_frame)
            frame.pack(fill="x", padx=2, pady=2)

            checkbox = ctk.CTkCheckBox(
                frame,
                text="",
                command=lambda i=i: self.toggle_graph_visibility(i),
                width=20,
            )
            checkbox.pack(side="left", padx=5)

            if graph.visible:
                checkbox.select()
            else:
                checkbox.deselect()

            label = ctk.CTkLabel(frame, text=f"{graph.name}", width=120, anchor="w")
            label.pack(side="left", padx=5)

            delete_btn = ctk.CTkButton(
                frame,
                text="X",
                command=lambda i=i: self.delete_graph(i),
                width=30,
                fg_color="#FF5555",
                hover_color="#AA3333",
            )
            delete_btn.pack(side="right", padx=5)

    def toggle_graph_visibility(self, graph_index) -> None:
        if 0 <= graph_index < len(self._graphes):
            self._graphes[graph_index].visible = not self._graphes[graph_index].visible
            self.update_plot()

    def delete_graph(self, graph_index) -> None:
        if 0 <= graph_index < len(self._graphes):
            del self._graphes[graph_index]
            self.update_graph_list()
            self.update_plot()

    def clear_all_graphs(self) -> None:
        self._graphes = []
        self.update_graph_list()
        self.update_plot()

    def update_plot(self) -> None:
        try:
            self._x_min = float(self._x_min_entry.get())
            self._x_max = float(self._x_max_entry.get())
            self._y_min = float(self._y_min_entry.get())
            self._y_max = float(self._y_max_entry.get())

            self._plot.clear()

            self._figure.patch.set_facecolor("#1a1a1a")
            self._plot.set_facecolor("#1a1a1a")

            self._plot.set_xlim(self._x_min, self._x_max)
            self._plot.set_ylim(self._y_min, self._y_max)

            self._plot.axhline(y=0, color="white", linestyle="-", alpha=0.6)
            self._plot.axvline(x=0, color="white", linestyle="-", alpha=0.6)

            self._plot.grid(True, linestyle="--", alpha=0.3, color="white")

            self._plot.set_xlabel("X-Achse", color="white")
            self._plot.set_ylabel("Y-Achse", color="white")

            visible_graphs = sum(1 for graph in self._graphes if graph.visible)

            if visible_graphs == 0:
                self._plot.set_title(
                    "2D-Koordinatensystem (Keine Graphen)", color="white"
                )
            elif visible_graphs == 1:
                self._plot.set_title("2D-Koordinatensystem (1 Graph)", color="white")
            else:
                self._plot.set_title(
                    f"2D-Koordinatensystem ({visible_graphs} Graphen)", color="white"
                )

            self._plot.tick_params(axis="x", colors="white")
            self._plot.tick_params(axis="y", colors="white")

            for spine in self._plot.spines.values():
                spine.set_edgecolor("white")

            for graph in self._graphes:
                if graph.visible:
                    self.draw_graph(graph)

            self._canvas.draw()

        except ValueError:
            error_window = ctk.CTkToplevel(self)
            error_window.title("Fehler")
            error_window.geometry("300x100")

            error_label = ctk.CTkLabel(
                error_window, text="Bitte geben Sie gültige Zahlen ein!"
            )
            error_label.pack(padx=20, pady=20)

            error_window.lift()
            error_window.focus_force()

    def draw_graph(self, graph: Graph) -> None:
        if not graph:
            return

        for node in graph.nodes:
            circle = mpatches.Circle(
                (node.x, node.y),
                radius=0.3,
                facecolor=node.color,
                edgecolor="white",
                alpha=0.8,
                zorder=10,
            )
            self._plot.add_patch(circle)

            label_text = node.label if node.label else str(node.id)
            self._plot.annotate(
                label_text,
                (node.x, node.y),
                color="white",
                ha="center",
                va="center",
                fontsize=9,
                fontweight="bold",
                zorder=11,
            )

        for edge in graph.edges:
            x1, y1 = edge.source.x, edge.source.y
            x2, y2 = edge.target.x, edge.target.y

            self._plot.plot(
                [x1, x2], [y1, y2], color=edge.color, linewidth=1.5, alpha=0.7, zorder=5
            )

    def create_random_graph(self) -> None:
        num_nodes = random.randint(3, 8)

        colors = [
            "#FF5733",
            "#33FF57",
            "#3357FF",
            "#F3FF33",
            "#FF33F3",
            "#33FFF3",
            "#FF9A33",
        ]

        graph_name = f"Random graph {len(self._graphes) + 1}"

        nodes = []
        for i in range(num_nodes):
            pos_x = random.randint(int(self._x_min + 2), int(self._x_max - 2))
            pos_y = random.randint(int(self._y_min + 2), int(self._y_max - 2))

            node_color = random.choice(colors)

            label = chr(65 + i)  # A, B, C, ...

            nodes.append(
                Node(pos=[pos_x, pos_y], id=i + 1, label=label, color=node_color)
            )

        edges = []

        for i in range(1, num_nodes):
            source = nodes[i]
            target = nodes[random.randint(0, i - 1)]
            edge_color = random.choice(colors)
            edges.append(Edge(source=source, target=target, color=edge_color))

        extra_edges = random.randint(0, num_nodes)
        for _ in range(extra_edges):
            source_idx = random.randint(0, num_nodes - 1)
            target_idx = random.randint(0, num_nodes - 1)

            if source_idx != target_idx:
                edge_color = random.choice(colors)
                edges.append(
                    Edge(
                        source=nodes[source_idx],
                        target=nodes[target_idx],
                        color=edge_color,
                    )
                )

        graph = Graph(
            nodes=nodes,
            edges=edges,
            name=graph_name,
            color=random.choice(colors),
            visible=True,
        )

        self._graphes.append(graph)

        self.update_graph_list()
        self.update_plot()

    def load_json_graph(self) -> None:
        json_to_graph_tool = JSONtoGraph()
        json_to_graph_tool.merge()

        for graph in json_to_graph_tool.graphes:
            self._graphes.append(graph)

        self.update_graph_list()
        self.update_plot()
