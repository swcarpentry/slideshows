Software Carpentry Slideshows
=============================

Ideas

*  [Introducing Software Carpentry](http://swcarpentry.github.io/slideshows/introducing-software-carpentry/index.html)
*  [Software Carpentry: Lessons Learned](http://swcarpentry.github.io/slideshows/lessons-learned/index.html)
*  [Best Practices for Scientific Computing](http://swcarpentry.github.io/slideshows/best-practices/index.html)

Tutorials

*  [Creating a Workshop Website](http://swcarpentry.github.io/slideshows/creating-workshop/index.html)
*  [Creating a Lesson](http://swcarpentry.github.io/slideshows/creating-lesson/index.html)


Visualizing presentations locally with chrome (or chromium)
-----------------------------------------------------------

If you get a popup message mentionning that the timing file could not be loaded, please read on.
When loading a presentation from the local filesystem (address starting with file://), chrome will refuses to dynamically load files such as the timing files.

The solution is to start a webserver and access the presentation through it:
- go to the root of the repository
- run `python -m SimpleHTTPServer 7777` (or with Python 3: `python3 -m http.server 7777`)
- view the presentations at `http://localhost:7777`



Alternatively, start chrome with `chrome --disable-web-security` .
__Warning__: for security reasons, you should not navigate the open web with this option enabled.

