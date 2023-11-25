---
source: https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#jupyterlab

created: 2023-11-25T12:39:12 (UTC +01:00)

tags: []

author: 

---
# Jupyter — Bokeh 3.3.1 Documentation
---
## Working in notebooks[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#working-in-notebooks "Permalink to this heading")

[Jupyter](https://jupyter.org/) notebooks are computable documents often used for exploratory work, data analysis, teaching, and demonstration. A notebook is a series of _input cells_ that can execute individually to immediately display their output. In addition to _Classic_ notebooks, there are also notebooks for the newer _JupyterLab_ project. Bokeh can embed both standalone and Bokeh server content with either.

### Standalone output[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#standalone-output "Permalink to this heading")

Standalone Bokeh content doesn’t require a Bokeh server and can be embedded directly in classic Jupyter notebooks as well as in JupyterLab.

#### Classic notebooks[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#classic-notebooks "Permalink to this heading")

To display Bokeh plots inline in a classic Jupyter notebook, use the [`output_notebook()`](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.output_notebook "bokeh.io.output_notebook") function from [bokeh.io](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh-io) instead of (or in addition to) the [`output_file()`](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.output_file "bokeh.io.output_file") function. No other modifications are required. When you call [`show()`](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.show "bokeh.io.show"), the plot will display inline in the next notebook output cell. See a screenshot of Jupyter below:

[![Screenshot of a Jupyter notebook displaying a Bokeh scatterplot inline after calling show().](https://docs.bokeh.org/en/latest/_images/notebook_inline.png)](https://docs.bokeh.org/en/latest/_images/notebook_inline.png)

To have a single notebook output cell display multiple plots, call [`show()`](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.show "bokeh.io.show") multiple times in the input cell. The plots will display in order.

[![Screenshot of a Jupyter notebook displaying multiple Bokeh scatterplots inline after calling show() multiple times.](https://docs.bokeh.org/en/latest/_images/notebook_inline_multiple.png)](https://docs.bokeh.org/en/latest/_images/notebook_inline_multiple.png)

#### JupyterLab[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#jupyterlab "Permalink to this heading")

To use JupyterLab with Bokeh, you should at least use version 3.0 of JupyterLab. Enabling Bokeh visualizations in JupyterLab also requires the [jupyter\_bokeh](https://github.com/bokeh/jupyter_bokeh) extension to be installed.

After installing JupyterLab, you can use either `pip` or `conda` to install jupyter\_bokeh:

Make sure you have either [Anaconda](https://www.anaconda.com/products/individual#Downloads) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed. Use this command to install jupyter\_bokeh:

```
conda install jupyter_bokeh

```

Use this command to install jupyter\_bokeh:

```
pip install jupyter_bokeh

```

For instructions on installing jupyter\_bokeh with versions of JupyterLab older than 3.0, see the [README](https://github.com/bokeh/jupyter_bokeh/blob/main/README.md) in the GitHub repository of [jupyter\_bokeh](https://github.com/bokeh/jupyter_bokeh).

Once you have jupyter\_bokeh installed, you can use Bokeh just like you would with a [classic notebook](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#ug-output-jupyter-notebook-inline-plots).

[![Screenshot of Jupyterlab with a Bokeh ridgeplot displayed inline.](https://docs.bokeh.org/en/latest/_images/ridgeplot_jupyter_lab.png)](https://docs.bokeh.org/en/latest/_images/ridgeplot_jupyter_lab.png)

### Bokeh server applications[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#bokeh-server-applications "Permalink to this heading")

You can also embed full Bokeh server applications connecting plot events and Bokeh’s built-in widgets directly to Python callback code. See [Bokeh server](https://docs.bokeh.org/en/latest/docs/user_guide/server.html#ug-server) for general information about Bokeh server applications. For a complete example of a Bokeh application embedded in a Jupyter notebook, refer to the following notebook:

-   [examples/server/api/notebook\_embed.ipynb](https://github.com/bokeh/bokeh/tree/3.3.1/examples/server/api/notebook_embed.ipynb)
    

#### JupyterHub[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#jupyterhub "Permalink to this heading")

When running notebooks from your own JupyterHub instance, some additional steps are necessary to embed Bokeh server applications and to enable network connectivity between the client browser and the Bokeh server running in a JupyterLab cell. This is because your browser needs to connect to the port the Bokeh server is listening on. However, JupyterHub is acting as a reverse proxy between your browser and your JupyterLab container.

Bokeh solves this problem by providing a notebook\_url parameter which can be passed a callable to compute the final URL based on an integer port. Further, if the JupyterHub admin defines the environment variable `JUPYTER_BOKEH_EXTERNAL_URL` the process of defining notebook\_url becomes fully automatic and `notebook_url` no longer needs to be specified. This has the advantage that the same notebook will run unmodified both on JupyterHub and in a standalone JupyterLab session.

### Required Dependencies[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#required-dependencies "Permalink to this heading")

Follow all the JupyterLab (not JupyterHub) instructions above, then continue by installing the `jupyter-server-proxy` package and enable the server extension as follows:

> ```
> pip install jupyter-server-proxy && jupyter serverextension enable --py jupyter-server-proxy
> 
> ```

If you intend to work with JupyterLab you need to install the corresponding extension, either from the GUI or with the following command:

> ```
> jupyter labextension install @jupyterlab/server-proxy
> 
> ```

### JupyterHub for Administrators[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#jupyterhub-for-administrators "Permalink to this heading")

If you are a JupyterHub admin you can make Bokeh work autotomatically with unchanged notebooks by setting an environment variable in the notebook environment:

> ```
> export JUPYTER_BOKEH_EXTERNAL_URL="https//our-hub.science.edu"
> 
> ```

Often this is done in JupyterHub Helm chart configuration YAML like this:

> ```
> hub:
>   single_user:
>     extraEnv:
>       JUPYTER_BOKEH_EXTERNAL_URL="https://our-public-hub-name.edu"
> 
> ```

The net effect of the above is that the techniques of the next section are automatically used by bokeh and no additional actions are required.

### JupyterHub for Users[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#jupyterhub-for-users "Permalink to this heading")

For Hubs on which `JUPYTER_BOKEH_EXTERNAL_URL` is not set, define a function to help create the URL for the browser to connect to the Bokeh server. See below for a reference implementation. You’ll have to either modify this code or assign the URL of your JupyterHub installation to the environment variable `EXTERNAL_URL`. JupyterHub defaults to `JUPYTERHUB_SERVICE_PREFIX` in this case.

> ```
> def remote_jupyter_proxy_url(port):
>     """
>     Callable to configure Bokeh's show method when a proxy must be
>     configured.
> 
>     If port is None we're asking about the URL
>     for the origin header.
>     """
>     base_url = os.environ['EXTERNAL_URL']
>     host = urllib.parse.urlparse(base_url).netloc
> 
>     # If port is None we're asking for the URL origin
>     # so return the public hostname.
>     if port is None:
>         return host
> 
>     service_url_path = os.environ['JUPYTERHUB_SERVICE_PREFIX']
>     proxy_url_path = 'proxy/%d' % port
> 
>     user_url = urllib.parse.urljoin(base_url, service_url_path)
>     full_url = urllib.parse.urljoin(user_url, proxy_url_path)
>     return full_url
> 
> ```

Pass the function you defined above to the [`show()`](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.show "bokeh.io.show") function as the `notebook_url` keyword argument. Bokeh then calls this function when it sets up the server and creates the URL to load a graph:

> ```
> show(obj, notebook_url=remote_jupyter_proxy_url)
> 
> ```

You may need to restart your server after this, and then Bokeh content should load and execute Python callbacks defined in your Jupyter environment.

### Trusting notebooks[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#trusting-notebooks "Permalink to this heading")

Depending on the version of the notebook you are using, you may have to [trust the notebook](https://jupyter-notebook.readthedocs.io/en/stable/security.html#explicit-trust) for Bokeh plots to re-render when the notebook is closed and re- opened. The **Trust Notebook** option is typically located under the **File** menu:

[![Screenshot of the Jupyter File menu expanded to show the Trust Notebook option.](https://docs.bokeh.org/en/latest/_images/notebook_trust.png)](https://docs.bokeh.org/en/latest/_images/notebook_trust.png)

### Notebook slides[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#notebook-slides "Permalink to this heading")

You can use a notebook with [Reveal.js](http://lab.hakim.se/reveal-js/#/) to generate slideshows from cells. You can also include standalone (i.e. non-server) Bokeh plots in such sideshows. However, you will need to take a few extra steps to display the output correctly. Particularly, make sure that **the cell containing the** `output_notebook` **is not be skipped**.

Rendered cell output of the `output_notebook` call ensures that the BokehJS library loads. Otherwise, Bokeh plots will not work. If this cell’s type is set to _“skip”_, BokehJS will not load, and Bokeh plots will not display. If you want to hide this cell, assign it the _“notes”_ slide type.

### Notebook handles[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#notebook-handles "Permalink to this heading")

You can update a displayed plot without reloading it. To do so, pass the `notebook_handle=True` argument to [`show()`](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.show "bokeh.io.show") for it to return a handle object. You can use this handle object with the [`push_notebook()`](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.push_notebook "bokeh.io.push_notebook") function to update the plot with any recent changes to plots properties, data source values, etc.

This notebook handle functionality is only supported in classic Jupyter notebooks and is not implemented in JupyterLab or Zeppelin yet.

The following screenshots illustrate basic usage of notebook handles:

1.  Import standard functions and [`push_notebook()`](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.push_notebook "bokeh.io.push_notebook"):
    

[![Screenshot of Jupyter showing Bokeh push_notebook being imported .](https://docs.bokeh.org/en/latest/_images/notebook_comms1.png)](https://docs.bokeh.org/en/latest/_images/notebook_comms1.png)

2.  Create some plots and pass `notebook_handle=True` to [`show()`](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.show "bokeh.io.show"):
    

[![Screenshot of Jupyter with Bokeh content created with notebook comms enabled.](https://docs.bokeh.org/en/latest/_images/notebook_comms2.png)](https://docs.bokeh.org/en/latest/_images/notebook_comms2.png)

3.  Check that the handle is associated with the output cell for `In[2]` just displayed:
    

[![Screenshot of Jupyter showing the representation of a notebook comms handle in an output cell.](https://docs.bokeh.org/en/latest/_images/notebook_comms3.png)](https://docs.bokeh.org/en/latest/_images/notebook_comms3.png)

4.  Update some properties of the plot, then call [`push_notebook()`](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.push_notebook "bokeh.io.push_notebook") with the handle:
    

[![Screenshot of Jupyter input cell modifying Bokeh properties and calling push_notebook.](https://docs.bokeh.org/en/latest/_images/notebook_comms4.png)](https://docs.bokeh.org/en/latest/_images/notebook_comms4.png)

5.  Note that the output cell for `In[2]` has changed (_without_ being re-executed):
    

[![Screenshot of Jupyter showing the previous plot updated in place, with glyph color white now.](https://docs.bokeh.org/en/latest/_images/notebook_comms5.png)](https://docs.bokeh.org/en/latest/_images/notebook_comms5.png)

See the following notebooks for more detailed examples of notebook handle use:

-   [examples/output/jupyter/push\_notebook/Basic Usage.ipynb](https://github.com/bokeh/bokeh/tree/3.3.1/examples/output/jupyter/push_notebook/Basic%20Usage.ipynb)
    
-   [examples/output/jupyter/push\_notebook/Continuous Updating.ipynb](https://github.com/bokeh/bokeh/tree/3.3.1/examples/output/jupyter/push_notebook/Continuous%20Updating.ipynb)
    
-   [examples/output/jupyter/push\_notebook/Jupyter Interactors.ipynb](https://github.com/bokeh/bokeh/tree/3.3.1/examples/output/jupyter/push_notebook/Jupyter%20Interactors.ipynb)
    
-   [examples/output/jupyter/push\_notebook/Numba Image Example.ipynb](https://github.com/bokeh/bokeh/tree/3.3.1/examples/output/jupyter/push_notebook/Numba%20Image%20Example.ipynb)
    

### Jupyter interactors[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#jupyter-interactors "Permalink to this heading")

You can use notebook widgets, known as [interactors](http://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html), to update Bokeh plots. The key to doing this is the [`push_notebook()`](https://docs.bokeh.org/en/latest/docs/reference/io.html#bokeh.io.push_notebook "bokeh.io.push_notebook") function. The update callback for the interactors calls this function to update the plot from widget values. See a screenshot of the [examples/output/jupyter/push\_notebook/Jupyter Interactors.ipynb](https://github.com/bokeh/bokeh/tree/3.3.1/examples/output/jupyter/push_notebook/Jupyter%20Interactors.ipynb) example notebook below:

[![Screenshot of Jupyter showing a Bokeh plot together with ipywidget sliders.](https://docs.bokeh.org/en/latest/_images/notebook_interactors.png)](https://docs.bokeh.org/en/latest/_images/notebook_interactors.png)

### More example notebooks[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#more-example-notebooks "Permalink to this heading")

You can find many more examples of notebook use in the [bokeh-notebook](https://github.com/bokeh/bokeh-notebooks) repository:

1.  Clone the repository locally:
    
    ```
    git clone https://github.com/bokeh/bokeh-notebooks.git
    
    ```
    
2.  Launch the Jupyter notebooks in your web browser.
    

Alternatively, [Binder](https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/HEAD?labpath=index.iynb) hosts live notebooks that you can run online.

The main [Bokeh](https://github.com/bokeh/bokeh) repository also includes some notebook comms examples:

-   [examples/output/jupyter/push\_notebook/Basic Usage.ipynb](https://github.com/bokeh/bokeh/tree/3.3.1/examples/output/jupyter/push_notebook/Basic%20Usage.ipynb)
    
-   [examples/output/jupyter/push\_notebook/Continuous Updating.ipynb](https://github.com/bokeh/bokeh/tree/3.3.1/examples/output/jupyter/push_notebook/Continuous%20Updating.ipynb)
    
-   [examples/output/jupyter/push\_notebook/Jupyter Interactors.ipynb](https://github.com/bokeh/bokeh/tree/3.3.1/examples/output/jupyter/push_notebook/Jupyter%20Interactors.ipynb)
    
-   [examples/output/jupyter/push\_notebook/Numba Image Example.ipynb](https://github.com/bokeh/bokeh/tree/3.3.1/examples/output/jupyter/push_notebook/Numba%20Image%20Example.ipynb)
    

## IPyWidgets outside the notebook[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#ipywidgets-outside-the-notebook "Permalink to this heading")

Now that you know how to use Bokeh in the JupyterLab and classical notebook environments, you might want to take advantage of the vibrant Jupyter ecosystem outside of these environments. You can do so with the [ipywidgets\_bokeh](https://github.com/bokeh/ipywidgets_bokeh) extension for Bokeh:

```
$ conda install -c bokeh ipywidgets_bokeh

```

or

```
$ pip install ipywidgets_bokeh

```

This extension lets you use [IPyWidgets](https://ipywidgets.readthedocs.io/) in Bokeh. Simply wrap a widget in an `IPyWidget` model and add the wrapper to a document or include it in a layout. You don’t have to install or enable any other extensions.

### Example[#](https://docs.bokeh.org/en/latest/docs/user_guide/output/jupyter.html#example "Permalink to this heading")

Follow these steps to build an application with a single Jupyter slider that logs its adjustments to the console:

1.  Start by constructing a widget and configuring an observer:
    
    ```
    from ipywidgets import FloatSlider
    angle = FloatSlider(min=0, max=360, value=0, step=1, description="Angle")
    
    def on_change(change):
        print(f"angle={change['new']} deg")
    angle.observe(on_change, names="value")
    
    ```
    
2.  To integrate the widget with Bokeh, wrap it in `IPyWidget`:
    
    ```
    from ipywidgets_bokeh import IPyWidget
    ipywidget = IPyWidget(widget=angle)
    
    ```
    
3.  Add the wrapper to a Bokeh document:
    
    ```
    from bokeh.plotting import curdoc
    doc = curdoc()
    doc.add_root(ipywidget)
    
    ```
    

To run the app, enter `bokeh serve ipy_slider.py`, where `ipy_slider.py` is the name of the application (see [Bokeh server](https://docs.bokeh.org/en/latest/docs/user_guide/server.html#ug-server) for details). This application is available at [http://localhost:5006/ipy\_slider](http://localhost:5006/ipy_slider).

You can build on the above to create more complex layouts and include advanced widgets, such as [ipyleaflet](https://jupyter.org/widgets#ipyleaflet) and [ipyvolume](https://jupyter.org/widgets#ipyvolume). For more examples, see `examples/howto/ipywidgets` in the Bokeh repository.
