# eggsmark
:egg: executable markdown framework

---------------------------------------------------------------------------------------

jupyter and Rmd notebooks have become ubiquitious in the domain of data science.
These competing technologies provide alternate approaches to the problem of organizing notes, documentation, and data visualization alongside code.

Both technologies work with multiple languages but generally speaking: jupyter is best for python and Rmd is best for R.
This project establishes a framework for code notebooks that is language-agnostic.
"Knit-engines" can be implemented in any language.
The default knit-engine (py-knit) is written in python.

Both technologies are tied to a operational kernel which computes the notebook output.
This executable-markdown (xmd) project asserts that code notebooks should be human-legible raw text notebook files which are kernel-independent.

`.xmd` documents build on `.Rmd` documents but do not rely on R to "knit" the document into a legible output.
"Knitters" can be implemented in any language and `.xmd` documents can be partially knit by the relevant kernel.

Consider the following example `xmd` document:

    ------
    ```{R}
        print("this is an R chunk")
    ```
    This is **raw** markdown.
    ```{python}
        print("this is a python chunk")
    ```
    ## Let's get weird
    ```{C++}
        printf("this is a c++ chunk")
    ```

Like in `Rmd` documents, chunks are annotated with the language used.
Rmarkdown would knit this document using the following pattern:

1. start the R kernel
2. use the R kernel and relevant libraries (eg reticulate for the python chunk)
    to execute the code chunks
3. write the output to the requested format (eg html)

In constrast, `xmd` works like:

1. parse the file & build the framework for kernels to contribute to the output
2. launch relevant kernel(s) to execute outputs of code chunks
3. stitch together kernel outputs into a final output document (eg html)

---------------------------------------------------------------------------

## Why not jupyter `.ipynb` notebooks
* .json inner representation is not human-readable
* VCS troubles
* code not easily editable as plain-text

## Why not Rmarkdown `.Rmd` documents
* tightly coupled to the R ecosystem
* templating is underdeveloped
* support for other languages only through R driver libraries
* capitalized file extension

---------------------------------------------------------------------------

## Joel's Notebook War

How does this address [Joel’s thoughts on notebooks](https://yihui.org/en/2018/09/notebook-war/)?

### [complaints](https://yihui.org/en/2018/09/notebook-war/#joel-s-complaints-about-notebooks)

TODO

1. Hidden state and out-of-order execution
2. Notebooks are difficult for beginners
3. Notebooks encourage bad habits
4. Notebooks discourage modularity and testing
5. Jupyter’s autocomplete, linting, and way of looking up the help are awkward
6. Notebooks encourage bad processes
7. Notebooks hinder reproducible + extensible science
8. Notebooks make it hard to copy and paste into Slack/Github issues
9. Errors will always halt execution
10. Notebooks make it easy to teach poorly
11. Notebooks make it hard to teach well

### [How you could win Joel over](https://yihui.org/en/2018/09/notebook-war/#how-you-could-win-joel-over)

TODO
