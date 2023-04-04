# Assignment 1: Grid World

DO NOT FORK THIS REPO 
-----
Clone it and work on it locally and never push commits anywhere public.


Due Date
-----
Apr-16 11:59pm Pacific Time. 


Submission
----
You only need to submit the `ai.py` file on Gradescope for grading.

If you have changed other files, make sure that your implementation works properly with the original, unchanged given files (`main.py`, `game.py`, `test.py`), which we will use for grading.


Setting Up
----
First, make sure you have Python 3.\* and the latest pip >= 20.\* (Check the `Notes & FAQ` section below if you're having trouble with this). Then, here is the preferred way to set up (if you have another way, feel free to do it):

1. Install [anaconda](https://docs.anaconda.com/anaconda/install/) to set up a virtual environment
2. `conda create -n cse150b python=3.10`
3. `conda activate cse150b`
4. To install PyGame, `pip install pygame`. We will use PyGame for all assignments in this class.
 
You can run `conda deactivate` to deactivate the environment. The next time you want to work on the assignment, type `conda activate cse150b` first to use the exact same environment with PyGame installed.

Tasks To Complete
----
The task is to find paths from the start (yellow node) to the goal (orange node). Once you load up the program (You'll see how in the `Usage` section below) and press `enter` you will see what that means. In class I briefly explained the meaning of the different colors of the nodes (green is "grass" that incurs high cost, blue is "puddle" that the agent can not pass through). Check slides, lecture recording, and read the code to figure things out. If you are stuck, feel free to discuss on slack or schedule office hours.

The code for DFS is **partially** given to make it easy for you to understand the code. But it is intentionally buggy. Before you start implementing the other algorithms, fix DFS first.

Implement the following search strategies in `ai.py`:

- DFS (buggy)
- BFS
- Uniform Cost Search
- A\* Search using Manhattan Distance as the heuristic

You can find the function definitions in the file. Feel free to add more auxiliary functions if needed. You can use other **standard Python libraries** such as math etc. but they are not really needed. Do not use libraries not standard to Python (i.e. numpy, torch); if you are not sure whether a library is ok to use or not, ask in the slack group.

Usage
----
Simply run `python main.py` and you will see the grid world window. By pressing `enter` you see how DFS finds a path (given DFS is buggy, as you will see). Pressing 2, 3, or 4 should respectively run BFS, UCS, A\* in a similar way, which you will implement (since right now it does nothing). 

The `tests` file contains a few test maps. If you want to load in the maps as test cases (`python main.py -l [test case number]`), we have provided a few fun cases for you to play with:

0. Random 1
1. Random 2
2. Spiral
3. Zigzag
4. "Two roads diverged in a wood, and I - I took the one less traveled by, and that has made all the difference."
5. CSE ~~11~~ 150b style (homage to Rick Ord)
6. "It's a-me, Mario!"

You can also do `python main.py -t` which autogrades the algorithms with respect to the correct optimal costs in the seven maps above.


Grading
-----
We will have a different set of test cases similar to those in `tests` and check if the path your algorithms compute return the right cost values. We will also read your code and see if you are implementing the right algorithms. 

There are four possible scores, as explained in the first lecture.

- Full (15 points): Everything is correct, passing all tests and implementing the right algorithms.
- Almost (13 points): Passed all given tests but there are minor mistakes that led to failure of some hidden tests. 
- Half (8 points): Major problems, such as not implementing some of the algorithms, but are in the right direction. 
- Null (1 point): Almost no attempt but at least you sent something in. 

Tips & FAQ
------
- Before you begin, it's wise to first get familiar with the workflow of the program and instance variables across files. This will be important for each assignment going forward (and save you a lot of time!)
- You can click mouse to put down more puddles when search is not running.
- You are encouraged to write your own tests for testing correctness of your solution. 
- You may find `pdb` extremely helpful to understand and debug your code. It is the Python debugger, similar to `GDB`. Here's a [quick tutorial](https://www.youtube.com/watch?v=VQjCx3P89yk&ab_channel=TutorialEdge).

**I'm having trouble loading up Pygame after installing it on MacOS.**
- If you encounter difficulty loading things after installing Pygame, this post https://stackoverflow.com/questions/52718921/problems-getting-pygame-to-show-anything-but-a-blank-screen-on-macos-mojave (in particular, the second answer by "Rafael") may likely help you. 

**Why does `python` show up as Python 2.\* instead of Python 3.\*?**
- If `python --version` shows Python 2.\*, but `python3 --version` shows Python 3.\*, you will either need to run all your commands with `python3` (e.g. `python3 main.py`) or change your default `python` to Python 3.\*. All `python` commands we make going forward will be assumed to be Python 3.\*. Here's a [link](https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3) that shows you how to set `python` to Python 3.\* by default instead of Python 2.\*. 

**My pip shows a version lower than 20.\*; how do I update it?**
- First, check if you have the right Python version; your pip version should be up to date if you have the correct Python. If this isn't the case, check [this](https://pip.pypa.io/en/stable/installation/#upgrading-pip) out.

**My system says `pip not found` when I try to run `pip`. What do I do?**
- First, check that you have Python 3.\* installed correctly. If you can't find any problems there, here's a [resource](https://pip.pypa.io/en/stable/installing/) you can check out. Again, all `pip` commands we make going forward are assumed with the latest `pip` version (>=20.\*).
