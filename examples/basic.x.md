This is and `.x.md` file.

Regular [markdown](https://daringfireball.net/projects/markdown/) can go in here.

## Also you can include code chunks:

### In scripting languages like python or R
```{python}
print("hello world!")
```

```{r}
print("hello world!")
```


This raw text file is designed to be maximally human-legible and more machine-legible outputs (like html) can be rendered from it using a knit-engine to *"knit"* an output.

To knit this file into html you can do:

```{bash, eval=FALSE}
xmd_knit basic.x.md ./tests/output/basic.x.html
```
