# === headers
HEADER_MINIMAL_PARAMS = [
    "params:",
    "    x: True",
]

# === chunks
MINIMAL_CHUNK_LINES_1 = ["print('hellow')"]
MINIMAL_CHUNK_LINES_2 = [
    "print('this is a 2nd chunk')",
    "print('this chunk has 2 lines too')"
]

# === full XMD file contents lines
XMD_LINES_MINIMAL = [
    "---",
    "```{python}",
    *MINIMAL_CHUNK_LINES_1,
    "```"
]
XMD_LINES_TWO_CHUNK = [
    "---",
    "```{python}",
    *MINIMAL_CHUNK_LINES_1,
    "```"
    "",
    "This is raw *markdown* text",
    "",
    "```{python}",
    *MINIMAL_CHUNK_LINES_2,
    "```"
]
XMD_LINES_W_HEADER = [
    *HEADER_MINIMAL_PARAMS,
    "---",
    "```{python}",
    *MINIMAL_CHUNK_LINES_1,
    "```"
    "",
    "This is raw *markdown* text",
    "",
    "```{python}",
    *MINIMAL_CHUNK_LINES_2,
    "```"
]
