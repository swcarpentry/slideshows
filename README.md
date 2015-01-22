Software Carpentry Slideshows
=============================

Ideas

*  [Introducing Software Carpentry](http://swcarpentry.github.io/slideshows/introducing-software-carpentry/index.html)
*  [Software Carpentry: Lessons Learned](http://swcarpentry.github.io/slideshows/lessons-learned/index.html)
*  [Best Practices for Scientific Computing](http://swcarpentry.github.io/slideshows/best-practices/index.html)

Tutorials

*  [Creating a Workshop Website](http://swcarpentry.github.io/slideshows/creating-workshop/index.html)
*  [Creating a Lesson](http://swcarpentry.github.io/slideshows/creating-lesson/index.html)


Visualizing Presentations Locally
---------------------------------

If you get a popup message mentioning that the timing file could not be loaded,
the problem may be your browser refusing to dynamically load files
(such as the timing file)
from the local filesystem.
The solution is to start a webserver and access the presentation through it:

1.  Go to the root of the repository.
2.  Run `python -m SimpleHTTPServer 7777` (or with Python 3: `python3 -m http.server 7777`).
3.  View the presentations at `http://localhost:7777`.

Alternatively, if you are using Google Chrome, start it with `chrome --disable-web-security`.
**Warning:** for security reasons, you should not navigate the open web with this option enabled.
