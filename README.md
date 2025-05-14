# Nodezilla

A simple and flexible tool to **visualize graphs** either from a JSON file or by generating random graphs.

## Features

- Load and display graphs from a `.json` file
- Generate random graphs with configurable options
- Customizable node positions, labels, and colors
- Global graph settings for consistent styling
- Automatic override of individual node/edge colors when a global color is specified

---

## JSON Graph Format

To load a graph from a JSON file, use the following format:

```json
"graph3": {
  "global_settings": { "name": "Triangle", "color": "blue" },
  "nodes": [
    { "pos": [0, 3], "id": 1, "label": "A", "color": "blue" },
    { "pos": [-2.5, -2], "id": 2, "label": "B" },
    { "pos": [2.5, -2], "id": 3, "label": "C" }
  ],
  "edges": [
    { "source": 1, "target": 2 },
    { "source": 2, "target": 3 },
    { "source": 3, "target": 1 }
  ]
}
```

### Field Details

#### `global_settings` (optional)

- `name`: A string representing the graph name (for UI or labeling purposes)
- `color`: A string specifying a color that overrides all individual node and edge colors

#### `nodes`

- `id`: Unique integer identifier for the node
- `label`: (Optional) A string label for the node
- `color`: (Optional) Color of the individual node (overridden if a global color is set)
- `pos`: A list of two numbers `[x, y]` representing the position of the node. Both integers and floats are supported, including mixed types.

#### `edges`

- `source`: ID of the source node
- `target`: ID of the target node

> **Note:** If a `color` is provided in `global_settings`, it will override all individual `color` values for nodes and edges.

---

## Random Graph Generation

You can also generate random graphs with parameters like:

- Number of nodes
- Edge density
- Optional random labels or colors
