
# Chinese Caligraphy Vectorization (CCV) Project

## Goal

- Transfer famous Chinese caligraphy works to vector graphics, and establish a library
- Develop interesting applications based on the library

## Method of vectorization

The method I employ is generally as follows:

- find a high-resolution bitmap of the caligraphy work
- crop the bitmap into small bitmaps each contains a character
- vectorize each character bitmap by the aid of vector graph editor (I use [Inkscape](www.inkscape.org))
- export to svg file

It should be noted that the vectorization process has no rigid or unique rule to follow. It is a physical yet artistic job, and no "best" result exists. The ambiguous edges should be decide objectively.

Specific (important) setups for Inkscape: (in Edit -> Perreferences -> SVG output)
- set "Path string format" to "Absolute"
- check "Force repeat commands"


## What is done

From 2008 to 2009, I vectorized many characters in ["兰亭集序"](http://zh.wikipedia.org/wiki/%E8%98%AD%E4%BA%AD%E9%9B%86%E5%BA%8F) (not finished). This work will be continued in 2016.

## Applications

- Calligraphy copybook. I write a app to re-typeset the characters to produce a copybook of the caligraphy.

demos:

```python
import ccv
ccv.produce_copybook(character_dir   = os.path.join(os.getcwd(), 'calligraphy', 'lantingxu', 'svg'),
                     title           = 'lantingxu',
                     rows            = 8,
                     direction       = 'v',
                     character_ratio = 0.75,
                     grid            = 'on',
                     canvas_width    = 1300)
```

will produce:

![](https://cdn.rawgit.com/herrkaefer/chinese-calligraphy-vectorization/master/copybooks/lantingxu-withgrid.svg)

```python
import ccv
ccv.produce_copybook(character_dir   = os.path.join(os.getcwd(), 'calligraphy', 'lantingxu', 'svg'),
                     title           = 'lantingxu',
                     rows            = 8,
                     direction       = 'v',
                     character_ratio = 0.75,
                     grid            = 'off',
                     canvas_width    = 1300)
```

will produce:

![](https://cdn.rawgit.com/herrkaefer/chinese-calligraphy-vectorization/master/copybooks/lantingxu-nogrid.svg)


