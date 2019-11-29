This is an `.postknit.x.md` file which includes inline output for each code chunk.
The knitting process first produces a human-readable .x.md document like this and then knits the full document together to the final output in a second step.
The inline output is inserted below each code chunk in code blocks named like `output__*`.
Multiple inline output code blocks can be included below a chunk of code.
This file can be read directly or could be read by a client IDE to render outputs.
For example, these could be shown in tabs or sequentially like Rstudio, jupyter, and nteract.

------------------------------------------------------------------------------

Regular [markdown](https://daringfireball.net/projects/markdown/) can go in here.

## Also you can include code chunks:

### In scripting languages like python or R
```{python}
print("hello world!")
```
```{output__md}
hello world!
```
```{output__html}
hello world!
```

```{r}
print("hello world!")
```
```{output__md}
hello world!
```

This raw text file is designed to be maximally human-legible and more machine-legible outputs (like html) can be rendered from it using a knit-engine to *"knit"* an output.
