---
source: https://alexandra-zaharia.github.io/posts/python-color-enum-class-for-ansi-color-codes/ \
created: 2022-12-26T23:24:15 (UTC +01:00) \
tags: [] \
author: Alexandra Zaharia
---
# Python color enum class for ANSI color codes | Alexandra Zaharia
---
When you want to print something with color and/or styling in a terminal, you can use one of the existing modules, such as [`colorama`](https://github.com/tartley/colorama) or [`sty`](https://github.com/feluxe/sty). They are well-documented, flexible and easy to use.

## Enum class

A very good guideline in software engineering is to avoid reinventing the wheel ![:upside_down_face:](https://github.githubassets.com/images/icons/emoji/unicode/1f643.png ":upside_down_face:")

But let’s face it, for some projects you really don’t want to bring in an external dependency. If the task is simple enough, you can just roll your own implementation. In this case, you’d just need to look into [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters) and find some [examples](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html).

For my very limited use cases when printing with color in a terminal, I just need to define a few foreground colors as well as the bold and the blink styles. I’m using an `Enum` class such that color names are class members, thus avoiding any possible misspelling issues:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 </pre></td><td><pre><span>from</span> <span>enum</span> <span>import</span> <span>Enum</span><span>,</span> <span>auto</span>   <span>class</span> <span>Color</span><span>(</span><span>Enum</span><span>):</span>     <span>RED</span> <span>=</span> <span>31</span>     <span>GREEN</span> <span>=</span> <span>auto</span><span>()</span>     <span>YELLOW</span> <span>=</span> <span>auto</span><span>()</span>     <span>BLUE</span> <span>=</span> <span>auto</span><span>()</span>     <span>MAGENTA</span> <span>=</span> <span>auto</span><span>()</span>     <span>CYAN</span> <span>=</span> <span>auto</span><span>()</span>     <span>LIGHTRED</span> <span>=</span> <span>91</span>     <span>LIGHTGREEN</span> <span>=</span> <span>auto</span><span>()</span>     <span>LIGHTYELLOW</span> <span>=</span> <span>auto</span><span>()</span>     <span>LIGHTBLUE</span> <span>=</span> <span>auto</span><span>()</span>     <span>LIGHTMAGENTA</span> <span>=</span> <span>auto</span><span>()</span>     <span>LIGHTCYAN</span> <span>=</span> <span>auto</span><span>()</span>      <span>_START</span> <span>=</span> <span>'</span><span>\u001b</span><span>['</span>     <span>_BOLD</span> <span>=</span> <span>';1'</span>     <span>_BLINK</span> <span>=</span> <span>';5'</span>     <span>_END</span> <span>=</span> <span>'m'</span>     <span>_RESET</span> <span>=</span> <span>'</span><span>\u001b</span><span>[0m'</span>      <span>@</span><span>staticmethod</span>     <span>def</span> <span>colored</span><span>(</span><span>color</span><span>,</span> <span>msg</span><span>,</span> <span>bold</span><span>=</span><span>False</span><span>,</span> <span>blink</span><span>=</span><span>False</span><span>):</span>         <span>if</span> <span>not</span><span>(</span><span>isinstance</span><span>(</span><span>color</span><span>,</span> <span>Color</span><span>)):</span>             <span>raise</span> <span>TypeError</span><span>(</span><span>f</span><span>'Unknown color </span><span>{</span><span>color</span><span>}</span><span>'</span><span>)</span>          <span>fmt_msg</span> <span>=</span> <span>Color</span><span>.</span><span>_START</span><span>.</span><span>value</span> <span>+</span> <span>str</span><span>(</span><span>color</span><span>.</span><span>value</span><span>)</span>          <span>if</span> <span>bold</span><span>:</span>             <span>fmt_msg</span> <span>+=</span> <span>Color</span><span>.</span><span>_BOLD</span><span>.</span><span>value</span>         <span>if</span> <span>blink</span><span>:</span>             <span>fmt_msg</span> <span>+=</span> <span>Color</span><span>.</span><span>_BLINK</span><span>.</span><span>value</span>          <span>return</span> <span>fmt_msg</span> <span>+</span> <span>Color</span><span>.</span><span>_END</span><span>.</span><span>value</span> <span>+</span> <span>str</span><span>(</span><span>msg</span><span>)</span> <span>+</span> <span>Color</span><span>.</span><span>_RESET</span><span>.</span><span>value</span> </pre></td></tr></tbody></table>`

We can use this class as follows:

`<table><tbody><tr><td><pre>1 2 3 4 5 6 7 8 9 </pre></td><td><pre><span>from</span> <span>color</span> <span>import</span> <span>Color</span>  <span>for</span> <span>item</span> <span>in</span> <span>Color</span><span>:</span>     <span>if</span> <span>item</span><span>.</span><span>name</span><span>.</span><span>startswith</span><span>(</span><span>'_'</span><span>):</span>         <span>continue</span>     <span>print</span><span>(</span><span>Color</span><span>.</span><span>colored</span><span>(</span><span>item</span><span>,</span> <span>item</span><span>.</span><span>name</span><span>))</span>     <span>if</span> <span>item</span><span>.</span><span>name</span><span>.</span><span>startswith</span><span>(</span><span>'LIGHT'</span><span>):</span>         <span>print</span><span>(</span><span>Color</span><span>.</span><span>colored</span><span>(</span><span>item</span><span>,</span> <span>'{} bold == {} bold'</span><span>.</span><span>format</span><span>(</span>             <span>item</span><span>.</span><span>name</span><span>[</span><span>5</span><span>:],</span> <span>item</span><span>.</span><span>name</span><span>),</span> <span>bold</span><span>=</span><span>True</span><span>))</span> </pre></td></tr></tbody></table>`

Here’s the output:

[![Colored output using the Color enum](https://alexandra-zaharia.github.io/assets/img/posts/color_enum.png)](https://alexandra-zaharia.github.io/assets/img/posts/color_enum.png)

## Accompanying code

The full code accompanying this post can be found on my [GitHub](https://github.com/alexandra-zaharia/python-playground/tree/main/color_enum) repository.

This post is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) by the author.
