---
source: https://voila.readthedocs.io/en/stable/using.html

created: 2023-11-25T12:13:00 (UTC +01:00)

tags: []

author: 

---
# Using Voilà — voila 0.5.1 documentation
---
Voilà can be used as a standalone application, or as a Jupyter server extension. This page describes how to do each. Before you begin, make sure that you follow the steps in [Installing Voilà](https://voila.readthedocs.io/en/stable/install.html#install).

The following sections cover how to use Voilà.

## As a standalone application[#](https://voila.readthedocs.io/en/stable/using.html#as-a-standalone-application "Link to this heading")

Voilà can be used to run, convert, and serve a Jupyter notebook as a standalone app. This can be done via the command-line, with the following pattern:

```
voila <path-to-notebook> <options>

```

For example, to render the `bqplot` example notebook as a standalone app, run

```
git clone https://github.com/voila-dashboards/voila
cd voila
voila notebooks/bqplot.ipynb

```

Voilà displays a message when your notebook-based application is live. By default, Voilà runs at `localhost:8866`.

To serve a **directory of Jupyter Notebooks**, navigate to the directory you’d like to serve, then simply run `voila`:

The page served by Voilà will now contain a list of any notebooks in the directory. By clicking on one, you will trigger Voilà’s conversion process. A new Jupyter kernel will be created for each notebook you click.

## As a Jupyter server extension[#](https://voila.readthedocs.io/en/stable/using.html#as-a-jupyter-server-extension "Link to this heading")

You can also use Voilà from within a Jupyter server (e.g., after running `jupyter lab` or `jupyter notebook`).

Note

Voilà can also be used as a notebook server extension, both with the [notebook](https://github.com/jupyter/notebook) server or with the [jupyter\_server](https://github.com/jupyter/jupyter_server).

To use Voilà within a pre-existing Jupyter server, first start the server, then go to the following URL:

For example, if you typed `jupyter lab` and it was running at `http://localhost:8888/lab`, then Voilà would be accessed at `http://localhost:8888/voila`.

In this case, Voilà will serve the directory in which the Jupyter server was started.

## How does Voilà work?[#](https://voila.readthedocs.io/en/stable/using.html#how-does-voila-work "Link to this heading")

When Voilà is run on a notebook, the following steps occur:

1.  Voilà runs the code in the notebook and collects the outputs
    
2.  The notebook and its outputs are converted to HTML. By default, the notebook **code cells are hidden**.
    
3.  This page is served either as a Tornado application, or via the Jupyter server.
    
4.  When users access the page, the widgets on the page have access to the underlying Jupyter kernel.
    

## The example notebooks[#](https://voila.readthedocs.io/en/stable/using.html#the-example-notebooks "Link to this heading")

The [notebooks directory](https://github.com/voila-dashboards/voila/tree/main/notebooks) contains a collection of Jupyter notebooks that can be rendered using Voilà:

-   **basics.ipynb** - a notebook with interactions requiring a roundtrip to the kernel.
    
-   **bqplot.ipynb** - uses custom Jupyter widgets such as [bqplot](https://github.com/bloomberg/bqplot).
    
-   **dashboard.ipynb** - uses gridstack.js for the layout of each output.
    
-   **gridspecLayout.ipynb** - uses [GridspecLayout](https://ipywidgets.readthedocs.io/en/latest/examples/Layout%20Templates.html#Grid-layout) for the layout of different widgets.
    
-   **interactive.ipynb** - makes use of ipywidget’s @interact.
    
-   **ipympl.ipynb** - contains custom interactive matplotlib figures using the [ipympl](https://github.com/matplotlib/jupyter-matplotlib) widget.
    
-   **ipyvolume.ipynb** - uses custom Jupyter widgets such as [ipyvolume](https://github.com/maartenbreddels/ipyvolume).
    
-   **query-strings.ipynb** - uses HTTP query parameters to parametrize a notebook
    
-   **xleaflet.ipynb** - a notebook that uses C++ kernel and interactive widgets
    

These examples demonstrate different interactive HTML widgets and can be used as inspiration for getting started with Voilà.

To **run the example notebooks**, a few additional libraries can be installed using:

```
conda install -c conda-forge ipywidgets ipyvolume bqplot scipy

```

Or alternatively:

The examples can then be served with:
