
# Chinese Caligraphy Vectorization (CCV) Project

## Objective

- Transfer famous Chinese caligraphy works to vector graphics, and establish a library
- Develop interesting applications based on the library

# Method of vectorization

The method I employ is as follows:

- find a high-resolution bitmap of the caligraphy work
- crop the bitmap into small bitmaps each contains a character
- vectorize each character bitmap by the aid of some software (I use [Inkscape](www.inkscape.org)) and save it to svg file

It should be noted that the vectorization process has no rigid or unique rule to follow. It is a physical yet artistic job, and no "best" result exists. The ambiguous edges should be decide objectively.

# What is finished about the library

From 2008 to 2009, I vectorized many characters in ["兰亭集序"](http://zh.wikipedia.org/wiki/%E8%98%AD%E4%BA%AD%E9%9B%86%E5%BA%8F).

## Application

- Calligraphy copybook. I write a app to re-typeset the characters to produce a copybook of the caligraphy. A demo is [here](copybooks/lantingxu.svg).

usage:

```
import ccv
ccv.produce_copybook(character_dir   = os.path.join(os.getcwd(), 'calligraphy', 'lantingxu', 'svg'), 
					 title           = 'lantingxu', 
					 rows            = 8, 
					 direction       = 'v', 
					 character_ratio = 0.7, 
					 grid            = 'on', 
					 canvas_width    = 1300)
```


