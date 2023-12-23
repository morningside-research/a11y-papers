- https://github.com/plottertools/hatched/blob/master/hatched/hatched.py
- https://github.com/GravO8/halftone
- https://github.com/GravO8/halftone-lines
- Nanou https://www.youtube.com/watch?v=hyyeLtJ7SQk

https://github.com/rksm/hot-lib-reloader-rs/tree/master/examples/nannou-vector-field
https://en.wikipedia.org/wiki/Screentone


Related work Manga Filling

https://arxiv.org/pdf/2306.04114.pdf
https://arxiv.org/pdf/2305.08325.pdf
https://www.cse.cuhk.edu.hk/~ttwong/papers/screenstyle/screenstyle.pdf


kmeans clustering

pull color? ignore black? 

Can I balance it? Can I make a kernelized k-means? 

What if I just count the modes directly and then seeded them there even though the cluster is smaller?

What about spectral clustering
https://pypi.org/project/svgtrace/

https://pypi.org/project/pypotrace/


0. get image some how -- "clip" svg from pdf? or get pdf
1. Use something like vtracer,
1. then find contiguous regions of color larger than a particular threshold (perceptual, cm scale on the page)
1. then OVERLAY patterns (semantic textures) upon those large contiguous regions 


Vtracer

- color clustering
- cutout (disjoint)
- high fitler speckle threshold

use vtracer, download dirty svg, compute area, then retexture


new problem: 