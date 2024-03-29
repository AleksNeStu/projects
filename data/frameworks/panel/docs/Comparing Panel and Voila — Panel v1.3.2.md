---
source: https://panel.holoviz.org/explanation/comparisons/compare_voila.html

created: 2023-11-25T13:10:38 (UTC +01:00)

tags: []

author: 

---
# Comparing Panel and Voila — Panel v1.3.2
---
Voila is a technology for deploying Jupyter notebooks (with or without Panel code) as standalone web pages backed by Python. Voila is thus one way you can deploy your Panel apps, your ipywidgets-based apps, or any other content visible in a Jupyter notebook (including multiple languages, like R or C++). Voila is an alternative to the Bokeh Server component that is available through `panel serve`; Panel works with either one, and you can deploy with _either_ Bokeh Server (panel serve) or Voila. To serve a Panel app with Voila, just install [jupyter\_bokeh](https://github.com/bokeh/jupyter_bokeh) and do `pn.ipywidget(panel_obj)`, which makes an ipywidget out of your Panel object that Voila (or Jupyter itself) can then display and let you interact with.

Similarly, widgets and plots that use ipywidgets, such as ipyvolume, ipyleaflet, or bqplot, can be used in your Panel app and deployed with Bokeh/Panel Server without needing Voila, as long as you have installed [ipywidgets\_bokeh](https://github.com/bokeh/ipywidgets_bokeh).

So, how do you choose between using Voila or Bokeh server if you are using Panel objects? Both servers are based on Tornado under the hood, but they differ in the fact that Jupyter will launch a new Python kernel for each user, while the Bokeh server can serve multiple users on the same Python process. This subtle difference has two major implications:

1.  The per-user overhead for an app is much lower for Bokeh Server than for Voila. Once the relevant libraries are imported, there is only a tiny bit of overhead for creating each new user session. The Jupyter server, on the other hand, always launches an entirely new process per user session, with all the overhead that entails. For a session that imports nothing but pandas and matplotlib the per-user overhead is 75 MB (as of 10/2019), which increases for more complex environments, limiting the number of users a Voila server can handle for a given application.
    
2.  Since a Bokeh server shares a single process for multiple sessions, data or processing can also be shared between the different sessions where appropriate. Such sharing makes it possible to drastically reduce the memory footprint of a Bokeh-Server app, to make it practical to support larger numbers of users and to provide faster startup or data-access times. (Dash goes even further, with no state stored per user, which is the opposite extreme from Voila, with the opposite issues and downsides.)
    

The other major difference between Bokeh Server and Voila is the way they process notebook files. Voila is built directly on the notebook format, though it also provides some support for bare Python files. By default, all output in the notebook (including Markdown cells) is included in the rendered Voila app, which has the benefit that existing notebooks can be served as apps _unchanged_. While that approach can be useful to get a quick set of plots, an existing notebook is unlikely to be organized and formatted in a way that forms a coherent dashboard, so in practice a notebook will need to be rewritten (suppressing most of the markdown and cell outputs, rearranging other cell outputs, etc.) before it will make a good Voila dashboard. In practice, you will then end up with two copies of the notebook: one optimized to be a narrative, storytelling notebook with a series of cells, and another organized as a dashboard. Or you can write a template to select only the cells you want in the dashboard and rearrange them, but then you need to maintain both the notebook and the template separately.

Panel takes a different approach, in that output from a notebook cell needs to be explicitly wrapped in a Panel object and marked as being “servable”; cell outputs and Markdown cells by default are shown only in the notebook, and not with `panel serve`. Panel in fact entirely ignores the fact that your notebook is organized into cells; it simply processes all the cells as Python code, and serves all the items that ended up being marked “servable”. Although this approach means editing the original notebook before you can see a dashboard, it makes it fully practical for the same notebook to serve both an exploratory or storytelling purpose (in Jupyter) and act as a dashboard deployment (of a designated subset of the functionality). The Panel developers very often use this functionality to provide detailed documentation for any given panel, with the cell-by-cell output showing the dataset, intermediate steps, interesting features, caveats, and how-tos, while the final deployed dashboard focuses on the final result, with the content in each case organized to best suit its purpose.
