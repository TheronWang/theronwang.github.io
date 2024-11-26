---
layout: post
title: Examples of blog format
date: 2000-06-29 21:01:00
description: usage of jekyll post format
tags: tutorial
categories: sample-posts
---
## Second Title
### Third Title
#### Forth Title
##### Five
###### Six

### Meta Data

#### categories & tags
- math
- computer science

#### redirect
+ /assets/pdf/example_pdf.pdf

#### table of contents
- toc:
    - beginning: true
    - sidebar: left

<hr>

### Content
#### Hipster list
- first level
    - sub level
- second level

#### Check list
- [ ] empty
- [x] finish

#### quote
> This is a quote

#### Images
```html
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        % include figure.liquid loading="eager" path="assets/img/9.jpg" class="img-fluid rounded z-depth-1" "%}"
    </div>
    <div class="col-sm mt-3 mt-md-0">
        % include figure.liquid loading="eager" path="assets/img/7.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
```

#### Math
This theme supports rendering beautiful math in inline and display modes using [MathJax 3](https://www.mathjax.org/) engine. You just need to surround your math expression with `$$`, like `$$ E = mc^2 $$`. If you leave it inside a paragraph, it will produce an inline expression, just like $$ E = mc^2 $$.

To use display mode, again surround your expression with `$$` and place it as a separate paragraph. Here is an example:

$$
\sum_{k=1}^\infty |\langle x, e_k \rangle|^2 \leq \|x\|^2
$$

You can also use `\begin{equation}...\end{equation}` instead of `$$` for display mode math.
MathJax will automatically number equations:

\begin{equation}
\label{eq:cauchy-schwarz}
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
\end{equation}

and by adding `\label{...}` inside the equation environment, we can now refer to the equation using `\eqref`.

Note that MathJax 3 is [a major re-write of MathJax](https://docs.mathjax.org/en/latest/upgrading/whats-new-3.0.html) that brought a significant improvement to the loading and rendering speed, which is now [on par with KaTeX](http://www.intmath.com/cg5/katex-mathjax-comparison.php).

#### Better Table

#### Videos

#### Audios

#### custom blackquotes

#### Jupyter Notebook

#### bibliography

#### TikZJax

#### Chart.js

#### EChart

#### geojson

#### Vega-Lite

#### Advanced Image - Swiper

#### pseudo code

#### Cite

#### with tabs