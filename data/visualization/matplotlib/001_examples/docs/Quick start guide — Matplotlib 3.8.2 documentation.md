---
source: https://matplotlib.org/stable/users/explain/quick_start.html

created: 2023-11-24T19:16:34 (UTC +01:00)

tags: [codex]

author: 

---
# Quick start guide — Matplotlib 3.8.2 documentation
---
Note

[Go to the end](https://matplotlib.org/stable/users/explain/quick_start.html#sphx-glr-download-users-explain-quick-start-py) to download the full example code

This tutorial covers some basic usage patterns and best practices to help you get started with Matplotlib.

```
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

```

## A simple example[#](https://matplotlib.org/stable/users/explain/quick_start.html#a-simple-example "Link to this heading")

Matplotlib graphs your data on [`Figure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure "matplotlib.figure.Figure")s (e.g., windows, Jupyter widgets, etc.), each of which can contain one or more [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes"), an area where points can be specified in terms of x-y coordinates (or theta-r in a polar plot, x-y-z in a 3D plot, etc.). The simplest way of creating a Figure with an Axes is using [`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots"). We can then use [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot") to draw some data on the Axes:

```
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

```

![quick start](https://matplotlib.org/stable/_images/sphx_glr_quick_start_001.png)

Note that to get this Figure to display, you may have to call `plt.show()`, depending on your backend. For more details of Figures and backends, see [Introduction to Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#figure-intro).

## Parts of a Figure[#](https://matplotlib.org/stable/users/explain/quick_start.html#parts-of-a-figure "Link to this heading")

Here are the components of a Matplotlib Figure.

![../../_images/anatomy.png](https://matplotlib.org/stable/_images/anatomy.png)

### [`Figure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure "matplotlib.figure.Figure")[#](https://matplotlib.org/stable/users/explain/quick_start.html#figure "Link to this heading")

The **whole** figure. The Figure keeps track of all the child [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes"), a group of 'special' Artists (titles, figure legends, colorbars, etc), and even nested subfigures.

The easiest way to create a new Figure is with pyplot:

It is often convenient to create the Axes together with the Figure, but you can also manually add Axes later on. Note that many [Matplotlib backends](https://matplotlib.org/stable/users/explain/figure/backends.html#backends) support zooming and panning on figure windows.

For more on Figures, see [Introduction to Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#figure-intro).

### [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")[#](https://matplotlib.org/stable/users/explain/quick_start.html#axes "Link to this heading")

An Axes is an Artist attached to a Figure that contains a region for plotting data, and usually includes two (or three in the case of 3D) [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis") objects (be aware of the difference between **Axes** and **Axis**) that provide ticks and tick labels to provide scales for the data in the Axes. Each [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") also has a title (set via [`set_title()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")), an x-label (set via [`set_xlabel()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")), and a y-label set via [`set_ylabel()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")).

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") class and its member functions are the primary entry point to working with the OOP interface, and have most of the plotting methods defined on them (e.g. `ax.plot()`, shown above, uses the [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot") method)

### [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")[#](https://matplotlib.org/stable/users/explain/quick_start.html#axis "Link to this heading")

These objects set the scale and limits and generate ticks (the marks on the Axis) and ticklabels (strings labeling the ticks). The location of the ticks is determined by a [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator") object and the ticklabel strings are formatted by a [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter"). The combination of the correct [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator") and [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter") gives very fine control over the tick locations and labels.

### [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")[#](https://matplotlib.org/stable/users/explain/quick_start.html#artist "Link to this heading")

Basically, everything visible on the Figure is an Artist (even [`Figure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure "matplotlib.figure.Figure"), [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes"), and [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis") objects). This includes [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text") objects, [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D") objects, [`collections`](https://matplotlib.org/stable/api/collections_api.html#module-matplotlib.collections "matplotlib.collections") objects, [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch") objects, etc. When the Figure is rendered, all of the Artists are drawn to the **canvas**. Most Artists are tied to an Axes; such an Artist cannot be shared by multiple Axes, or moved from one to another.

## Types of inputs to plotting functions[#](https://matplotlib.org/stable/users/explain/quick_start.html#types-of-inputs-to-plotting-functions "Link to this heading")

Plotting functions expect [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "(in NumPy v1.26)") or [`numpy.ma.masked_array`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.html#numpy.ma.masked_array "(in NumPy v1.26)") as input, or objects that can be passed to [`numpy.asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "(in NumPy v1.26)"). Classes that are similar to arrays ('array-like') such as [`pandas`](https://pandas.pydata.org/pandas-docs/stable/index.html#module-pandas "(in pandas v2.1.3)") data objects and [`numpy.matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "(in NumPy v1.26)") may not work as intended. Common convention is to convert these to [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "(in NumPy v1.26)") objects prior to plotting. For example, to convert a [`numpy.matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "(in NumPy v1.26)")

```
b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)

```

Most methods will also parse a string-indexable object like a _dict_, a [structured numpy array](https://numpy.org/doc/stable/user/basics.rec.html#structured-arrays#noqa:E501), or a [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v2.1.3)"). Matplotlib allows you to provide the `data` keyword argument and generate plots passing the strings corresponding to the _x_ and _y_ variables.

```
np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')

```

![quick start](https://matplotlib.org/stable/_images/sphx_glr_quick_start_002.png)

## Coding styles[#](https://matplotlib.org/stable/users/explain/quick_start.html#coding-styles "Link to this heading")

### The explicit and the implicit interfaces[#](https://matplotlib.org/stable/users/explain/quick_start.html#the-explicit-and-the-implicit-interfaces "Link to this heading")

As noted above, there are essentially two ways to use Matplotlib:

-   Explicitly create Figures and Axes, and call methods on them (the "object-oriented (OO) style").
    
-   Rely on pyplot to implicitly create and manage the Figures and Axes, and use pyplot functions for plotting.
    

See [Matplotlib Application Interfaces (APIs)](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#api-interfaces) for an explanation of the tradeoffs between the implicit and explicit interfaces.

So one can use the OO-style

```
x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.

```

![Simple Plot](https://matplotlib.org/stable/_images/sphx_glr_quick_start_003.png)

or the pyplot-style:

```
x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

```

![Simple Plot](https://matplotlib.org/stable/_images/sphx_glr_quick_start_004.png)

(In addition, there is a third approach, for the case when embedding Matplotlib in a GUI application, which completely drops pyplot, even for figure creation. See the corresponding section in the gallery for more info: [Embedding Matplotlib in graphical user interfaces](https://matplotlib.org/stable/gallery/user_interfaces/index.html#user-interfaces).)

Matplotlib's documentation and examples use both the OO and the pyplot styles. In general, we suggest using the OO style, particularly for complicated plots, and functions and scripts that are intended to be reused as part of a larger project. However, the pyplot style can be very convenient for quick interactive work.

Note

You may find older examples that use the `pylab` interface, via `from pylab import *`. This approach is strongly deprecated.

### Making a helper functions[#](https://matplotlib.org/stable/users/explain/quick_start.html#making-a-helper-functions "Link to this heading")

If you need to make the same plots over and over again with different data sets, or want to easily wrap Matplotlib methods, use the recommended signature function below.

which you would then use twice to populate two subplots:

```
data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})

```

![quick start](https://matplotlib.org/stable/_images/sphx_glr_quick_start_005.png)

Note that if you want to install these as a python package, or any other customizations you could use one of the many templates on the web; Matplotlib has one at [mpl-cookiecutter](https://github.com/matplotlib/matplotlib-extension-cookiecutter)

## Styling Artists[#](https://matplotlib.org/stable/users/explain/quick_start.html#styling-artists "Link to this heading")

Most plotting methods have styling options for the Artists, accessible either when a plotting method is called, or from a "setter" on the Artist. In the plot below we manually set the _color_, _linewidth_, and _linestyle_ of the Artists created by [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot"), and we set the linestyle of the second line after the fact with [`set_linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle").

```
fig, ax = plt.subplots(figsize=(5, 2.7))
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
l.set_linestyle(':')

```

![quick start](https://matplotlib.org/stable/_images/sphx_glr_quick_start_006.png)

### Colors[#](https://matplotlib.org/stable/users/explain/quick_start.html#colors "Link to this heading")

Matplotlib has a very flexible array of colors that are accepted for most Artists; see [allowable color definitions](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) for a list of specifications. Some Artists will take multiple colors. i.e. for a [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter") plot, the edge of the markers can be different colors from the interior:

![quick start](https://matplotlib.org/stable/_images/sphx_glr_quick_start_007.png)

### Linewidths, linestyles, and markersizes[#](https://matplotlib.org/stable/users/explain/quick_start.html#linewidths-linestyles-and-markersizes "Link to this heading")

Line widths are typically in typographic points (1 pt = 1/72 inch) and available for Artists that have stroked lines. Similarly, stroked lines can have a linestyle. See the [linestyles example](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html).

Marker size depends on the method being used. [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot") specifies markersize in points, and is generally the "diameter" or width of the marker. [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter") specifies markersize as approximately proportional to the visual area of the marker. There is an array of markerstyles available as string codes (see [`markers`](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers "matplotlib.markers")), or users can define their own [`MarkerStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle") (see [Marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)):

```
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(data1, 'o', label='data1')
ax.plot(data2, 'd', label='data2')
ax.plot(data3, 'v', label='data3')
ax.plot(data4, 's', label='data4')
ax.legend()

```

![quick start](https://matplotlib.org/stable/_images/sphx_glr_quick_start_008.png)

## Labelling plots[#](https://matplotlib.org/stable/users/explain/quick_start.html#labelling-plots "Link to this heading")

### Axes labels and text[#](https://matplotlib.org/stable/users/explain/quick_start.html#axes-labels-and-text "Link to this heading")

[`set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel"), [`set_ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel"), and [`set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") are used to add text in the indicated locations (see [Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html#text-intro) for more discussion). Text can also be directly added to plots using [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text"):

```
mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# the histogram of the data
n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)

ax.set_xlabel('Length [cm]')
ax.set_ylabel('Probability')
ax.set_title('Aardvark lengths\n (not really)')
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.axis([55, 175, 0, 0.03])
ax.grid(True)

```

![Aardvark lengths  (not really)](https://matplotlib.org/stable/_images/sphx_glr_quick_start_009.png)

All of the [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text") functions return a [`matplotlib.text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text") instance. Just as with lines above, you can customize the properties by passing keyword arguments into the text functions:

These properties are covered in more detail in [Text properties and layout](https://matplotlib.org/stable/users/explain/text/text_props.html#text-props).

### Using mathematical expressions in text[#](https://matplotlib.org/stable/users/explain/quick_start.html#using-mathematical-expressions-in-text "Link to this heading")

Matplotlib accepts TeX equation expressions in any text expression. For example to write the expression in the title, you can write a TeX expression surrounded by dollar signs:

where the `r` preceding the title string signifies that the string is a _raw_ string and not to treat backslashes as python escapes. Matplotlib has a built-in TeX expression parser and layout engine, and ships its own math fonts – for details see [Writing mathematical expressions](https://matplotlib.org/stable/users/explain/text/mathtext.html#mathtext). You can also use LaTeX directly to format your text and incorporate the output directly into your display figures or saved postscript – see [Text rendering with LaTeX](https://matplotlib.org/stable/users/explain/text/usetex.html#usetex).

### Annotations[#](https://matplotlib.org/stable/users/explain/quick_start.html#annotations "Link to this heading")

We can also annotate points on a plot, often by connecting an arrow pointing to _xy_, to a piece of text at _xytext_:

```
fig, ax = plt.subplots(figsize=(5, 2.7))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.set_ylim(-2, 2)

```

![quick start](https://matplotlib.org/stable/_images/sphx_glr_quick_start_010.png)

In this basic example, both _xy_ and _xytext_ are in data coordinates. There are a variety of other coordinate systems one can choose -- see [Basic annotation](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations-tutorial) and [Advanced annotation](https://matplotlib.org/stable/users/explain/text/annotations.html#plotting-guide-annotation) for details. More examples also can be found in [Annotating Plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html).

## Axis scales and ticks[#](https://matplotlib.org/stable/users/explain/quick_start.html#axis-scales-and-ticks "Link to this heading")

Each Axes has two (or three) [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis") objects representing the x- and y-axis. These control the _scale_ of the Axis, the tick _locators_ and the tick _formatters_. Additional Axes can be attached to display further Axis objects.

### Scales[#](https://matplotlib.org/stable/users/explain/quick_start.html#scales "Link to this heading")

In addition to the linear scale, Matplotlib supplies non-linear scales, such as a log-scale. Since log-scales are used so much there are also direct methods like [`loglog`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.loglog.html#matplotlib.axes.Axes.loglog "matplotlib.axes.Axes.loglog"), [`semilogx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogx.html#matplotlib.axes.Axes.semilogx "matplotlib.axes.Axes.semilogx"), and [`semilogy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogy.html#matplotlib.axes.Axes.semilogy "matplotlib.axes.Axes.semilogy"). There are a number of scales (see [Scales](https://matplotlib.org/stable/gallery/scales/scales.html) for other examples). Here we set the scale manually:

![quick start](https://matplotlib.org/stable/_images/sphx_glr_quick_start_012.png)

The scale sets the mapping from data values to spacing along the Axis. This happens in both directions, and gets combined into a _transform_, which is the way that Matplotlib maps from data coordinates to Axes, Figure, or screen coordinates. See [Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transforms-tutorial).

### Tick locators and formatters[#](https://matplotlib.org/stable/users/explain/quick_start.html#tick-locators-and-formatters "Link to this heading")

Each Axis has a tick _locator_ and _formatter_ that choose where along the Axis objects to put tick marks. A simple interface to this is [`set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks"):

```
fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(xdata, data1)
axs[0].set_title('Automatic ticks')

axs[1].plot(xdata, data1)
axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
axs[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
axs[1].set_title('Manual ticks')

```

![Automatic ticks, Manual ticks](https://matplotlib.org/stable/_images/sphx_glr_quick_start_013.png)

Different scales can have different locators and formatters; for instance the log-scale above uses [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator") and [`LogFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter "matplotlib.ticker.LogFormatter"). See [Tick locators](https://matplotlib.org/stable/gallery/ticks/tick-locators.html) and [Tick formatters](https://matplotlib.org/stable/gallery/ticks/tick-formatters.html) for other formatters and locators and information for writing your own.

### Plotting dates and strings[#](https://matplotlib.org/stable/users/explain/quick_start.html#plotting-dates-and-strings "Link to this heading")

Matplotlib can handle plotting arrays of dates and arrays of strings, as well as floating point numbers. These get special locators and formatters as appropriate. For dates:

![quick start](https://matplotlib.org/stable/_images/sphx_glr_quick_start_014.png)

For more information see the date examples (e.g. [Date tick labels](https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html))

For strings, we get categorical plotting (see: [Plotting categorical variables](https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html)).

![quick start](https://matplotlib.org/stable/_images/sphx_glr_quick_start_015.png)

One caveat about categorical plotting is that some methods of parsing text files return a list of strings, even if the strings all represent numbers or dates. If you pass 1000 strings, Matplotlib will think you meant 1000 categories and will add 1000 ticks to your plot!

### Additional Axis objects[#](https://matplotlib.org/stable/users/explain/quick_start.html#additional-axis-objects "Link to this heading")

Plotting data of different magnitude in one chart may require an additional y-axis. Such an Axis can be created by using [`twinx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx") to add a new Axes with an invisible x-axis and a y-axis positioned at the right (analogously for [`twiny`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twiny.html#matplotlib.axes.Axes.twiny "matplotlib.axes.Axes.twiny")). See [Plots with different scales](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html) for another example.

Similarly, you can add a [`secondary_xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_xaxis.html#matplotlib.axes.Axes.secondary_xaxis "matplotlib.axes.Axes.secondary_xaxis") or [`secondary_yaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_yaxis.html#matplotlib.axes.Axes.secondary_yaxis "matplotlib.axes.Axes.secondary_yaxis") having a different scale than the main Axis to represent the data in different scales or units. See [Secondary Axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/secondary_axis.html) for further examples.

```
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(7, 2.7), layout='constrained')
l1, = ax1.plot(t, s)
ax2 = ax1.twinx()
l2, = ax2.plot(t, range(len(t)), 'C1')
ax2.legend([l1, l2], ['Sine (left)', 'Straight (right)'])

ax3.plot(t, s)
ax3.set_xlabel('Angle [rad]')
ax4 = ax3.secondary_xaxis('top', functions=(np.rad2deg, np.deg2rad))
ax4.set_xlabel('Angle [°]')

```

![quick start](https://matplotlib.org/stable/_images/sphx_glr_quick_start_016.png)

## Color mapped data[#](https://matplotlib.org/stable/users/explain/quick_start.html#color-mapped-data "Link to this heading")

Often we want to have a third dimension in a plot represented by a colors in a colormap. Matplotlib has a number of plot types that do this:

```
X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

fig, axs = plt.subplots(2, 2, layout='constrained')
pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[0, 0])
axs[0, 0].set_title('pcolormesh()')

co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
fig.colorbar(co, ax=axs[0, 1])
axs[0, 1].set_title('contourf()')

pc = axs[1, 0].imshow(Z**2 * 100, cmap='plasma',
                          norm=mpl.colors.LogNorm(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=axs[1, 0], extend='both')
axs[1, 0].set_title('imshow() with LogNorm()')

pc = axs[1, 1].scatter(data1, data2, c=data3, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[1, 1], extend='both')
axs[1, 1].set_title('scatter()')

```

![pcolormesh(), contourf(), imshow() with LogNorm(), scatter()](https://matplotlib.org/stable/_images/sphx_glr_quick_start_017.png)

### Colormaps[#](https://matplotlib.org/stable/users/explain/quick_start.html#colormaps "Link to this heading")

These are all examples of Artists that derive from [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable") objects. They all can set a linear mapping between _vmin_ and _vmax_ into the colormap specified by _cmap_. Matplotlib has many colormaps to choose from ([Choosing Colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html#colormaps)) you can make your own ([Creating Colormaps](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#colormap-manipulation)) or download as [third-party packages](https://matplotlib.org/mpl-third-party/#colormaps-and-styles).

### Normalizations[#](https://matplotlib.org/stable/users/explain/quick_start.html#normalizations "Link to this heading")

Sometimes we want a non-linear mapping of the data to the colormap, as in the `LogNorm` example above. We do this by supplying the ScalarMappable with the _norm_ argument instead of _vmin_ and _vmax_. More normalizations are shown at [Colormap Normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html#colormapnorms).

### Colorbars[#](https://matplotlib.org/stable/users/explain/quick_start.html#colorbars "Link to this heading")

Adding a [`colorbar`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar") gives a key to relate the color back to the underlying data. Colorbars are figure-level Artists, and are attached to a ScalarMappable (where they get their information about the norm and colormap) and usually steal space from a parent Axes. Placement of colorbars can be complex: see [Placing Colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html#colorbar-placement) for details. You can also change the appearance of colorbars with the _extend_ keyword to add arrows to the ends, and _shrink_ and _aspect_ to control the size. Finally, the colorbar will have default locators and formatters appropriate to the norm. These can be changed as for other Axis objects.

## Working with multiple Figures and Axes[#](https://matplotlib.org/stable/users/explain/quick_start.html#working-with-multiple-figures-and-axes "Link to this heading")

You can open multiple Figures with multiple calls to `fig = plt.figure()` or `fig2, ax = plt.subplots()`. By keeping the object references you can add Artists to either Figure.

Multiple Axes can be added a number of ways, but the most basic is `plt.subplots()` as used above. One can achieve more complex layouts, with Axes objects spanning columns or rows, using [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic").

```
fig, axd = plt.subplot_mosaic([['upleft', 'right'],
                               ['lowleft', 'right']], layout='constrained')
axd['upleft'].set_title('upleft')
axd['lowleft'].set_title('lowleft')
axd['right'].set_title('right')

```

![upleft, right, lowleft](https://matplotlib.org/stable/_images/sphx_glr_quick_start_018.png)

Matplotlib has quite sophisticated tools for arranging Axes: See [Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#arranging-axes) and [Complex and semantic figure composition (subplot\_mosaic)](https://matplotlib.org/stable/users/explain/axes/mosaic.html#mosaic).

## More reading[#](https://matplotlib.org/stable/users/explain/quick_start.html#more-reading "Link to this heading")

For more plot types see [Plot types](https://matplotlib.org/stable/plot_types/index.html) and the [API reference](https://matplotlib.org/stable/api/index.html), in particular the [Axes API](https://matplotlib.org/stable/api/axes_api.html).

**Total running time of the script:** (0 minutes 3.980 seconds)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)
