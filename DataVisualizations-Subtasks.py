import numpy as np
import matplotlib.pyplot as plt

# Models
models = ["ChatGPT 5.0", "Claude Sonnet 4.5", "Gemini 2.5 Flash"]

# Subtasks
subtasks = [
    "Task 1a:\n3.3 Difficulty Maze,\n$\it{image\ input}$\n$\it{written\ output}$",
    "Task 1b:\n3.3 Difficulty Maze,\n$\it{image\ input}$\n$\it{image\ output*}$",
    "Task 1c:\n12.5 Difficulty Maze,\n$\it{image\ input}$\n$\it{written\ output}$",
    "Task 1d:\n12.5 Difficulty Maze,\n$\it{image\ input}$\n$\it{image\ output*}$",
    "Task 1e:\n14.7 Difficulty Maze,\n$\it{image\ input}$\n$\it{written\ output}$",
    "Task 1f:\n14.7 Difficulty Maze,\n$\it{image\ input}$\n$\it{image\ output*}$",
]



# Accuracy values (percentages) per model per subtask
# Each sublist corresponds to a model
chatgpt = [21,	21,	26,	21,	29,	0]
claude = [36,	0,	18,	0,	9,	0]
gemini = [29,	77,	27,	64,	36,	72]

x = np.arange(len(subtasks))  # positions for subtasks
width = 0.25  # width of each bar

fig, ax = plt.subplots(figsize=(12, 4))

# Plot bars for each model
ax.bar(x - width, chatgpt, width, label="ChatGPT 5.0")
ax.bar(x, claude, width, label="Claude Sonnet 4.5")
ax.bar(x + width, gemini, width, label="Gemini 2.5 Flash")

# Formatting
ax.set_xticks(x)
ax.set_xticklabels(subtasks, rotation=0)
ax.set_ylabel("Accuracy (%)")
ax.set_ylim(0, 100)
# ax.legend(frameon=False)
ax.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Models
models = ["ChatGPT 5.0", "Claude Sonnet 4.5", "Gemini 2.5 Flash"]

# Subtasks
subtasks = [
    "Task 2a: Decomposition,\n$\it{written\ input,\ written\ output}$",
    "Task 2a: Decomposition,\n$\it{written\ input,\ image\ output*}$",
    "Task 2b: Composition,\n$\it{image\ input,\ text\ output}$"
]

# Accuracy values (percentages) per model per subtask
# Each sublist corresponds to a model
chatgpt = [100, 0, 0]
claude = [100, 100, 10]
gemini = [90, 0, 0]

x = np.arange(len(subtasks))  # positions for subtasks
width = 0.25  # width of each bar

fig, ax = plt.subplots(figsize=(8, 4))

# Plot bars for each model
ax.bar(x - width, chatgpt, width, label="ChatGPT 5.0")
ax.bar(x, claude, width, label="Claude Sonnet 4.5")
ax.bar(x + width, gemini, width, label="Gemini 2.5 Flash")

# Formatting
ax.set_xticks(x)
ax.set_xticklabels(subtasks, rotation=0)
ax.set_ylabel("Accuracy (%)")
ax.set_ylim(0, 100)
# ax.legend(frameon=False)
ax.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Models
models = ["ChatGPT 5.0", "Claude Sonnet 4.5", "Gemini 2.5 Flash"]

# Subtasks
subtasks = [
    "Task 3a: Couch-TV,\n$\it{written\ input, code\ output}$",
    "Task 3b: Table-Chair,\n$\it{written\ input, code\ output}$",
    "Task 3c: Chair-Chair,\n$\it{written\ input, code\ output}$"
]

# Accuracy values (percentages) per model per subtask
# Each sublist corresponds to a model
chatgpt = [10, 100, 100]
claude = [10, 100, 75]
gemini = [40, 60, 83]

x = np.arange(len(subtasks))  # positions for subtasks
width = 0.25  # width of each bar

fig, ax = plt.subplots(figsize=(8, 4))

# Plot bars for each model
ax.bar(x - width, chatgpt, width, label="ChatGPT 5.0")
ax.bar(x, claude, width, label="Claude Sonnet 4.5")
ax.bar(x + width, gemini, width, label="Gemini 2.5 Flash")

# Formatting
ax.set_xticks(x)
ax.set_xticklabels(subtasks, rotation=0)
ax.set_ylabel("Accuracy (%)")
ax.set_ylim(0, 100)
# ax.legend(frameon=False)
ax.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Models
models = ["ChatGPT 5.0", "Claude Sonnet 4.5", "Gemini 2.5 Flash"]

# Subtasks
subtasks = [
    "Task 4a: Cube Folding,\n$\it{image\ input, text\ output}$",
    "Task 4b: Object Rotation,\n$\it{image\ input, text\ output}$",
]

# Accuracy values (percentages) per model per subtask
# Each sublist corresponds to a model
chatgpt = [73.1, 10]
claude = [72.8, 20]
gemini = [76.2, 45]

x = np.arange(len(subtasks))  # positions for subtasks
width = 0.25  # width of each bar

fig, ax = plt.subplots(figsize=(8, 4))

# Plot bars for each model
ax.bar(x - width, chatgpt, width, label="ChatGPT 5.0")
ax.bar(x, claude, width, label="Claude Sonnet 4.5")
ax.bar(x + width, gemini, width, label="Gemini 2.5 Flash")

# Formatting
ax.set_xticks(x)
ax.set_xticklabels(subtasks, rotation=0)
ax.set_ylabel("Accuracy (%)")
ax.set_ylim(0, 100)
# ax.legend(frameon=False)
ax.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()



