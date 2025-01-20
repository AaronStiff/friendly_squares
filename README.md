# friendly_squares

An incredibly niche and literally useless foray into a fascinating puzzle posed in [Matthew Scrogg's 2024 Advent calendar](https://www.mscroggs.co.uk/puzzles/advent2024)

**Requirements:**
- numpy
- sympy
- mpermute (install with `pip install git+https://github.com/m-stclair/mpermute.git`)
- alive_progress

The original puzzle involves colouring an *n* x *n* grid such that every square touches at least 2 coloured squares, which can include itself. Alternatively, place kings on an *n* x *n* grid such that every square is either occupied by or being attacked by at least 2 kings.

The minimum number of coloured squares/kings to do so is given in [A379726](https://oeis.org/A379726) of the OEIS and a proof is given in [one of Scrogg's blog posts](https://www.mscroggs.co.uk/blog/114).

This script bruteforces the total number of possible "colourings" for each minimum solution. So for example, for a 2 x 2 grid, there are 6 possible colourings. This obviously includes rotations/reflections. Here are the number of colourings for each size of grid:

| Grid     | Colourings |
| -------- | ---------- |
| 2 x 2    | 6          |
| 3 x 3    | 2          |
| 4 x 4    | 1296       |
| 5 x 5    | 371        |
| 6 x 6    | 8          |

I have not been able to find anything past a 6 x 6 grid with the current script, despite copious amounts of optimization. Grids from 2 x 2 to 4 x 4 took about a second each, 5 x 5 took around 10 seconds, and 6 x 6 took a whopping 50 minutes, at least on my poor little Surface Pro. Do note the irony of there being only 8 valid colourings out of the over 250 million the script checked.

I'm heartily accepting suggestions for ways to speed the script up or clever strategies for cutting down the number of matrices it checks, if you're really looking for a time sink with no obvious benefits. The code is virtually undocumented for an extra challenge. Currently it lazily generates every possible binary matrix with the minimum number of ones and checks each as it goes to see if it meets the "friendly square" rules.

Thanks [@mscroggs](https://github.com/mscroggs) for the Advent calendar, and such an interesting puzzle!

Thanks [@m-stclair](https://github.com/m-stclair) for the super fast multiset permutations script!

Thanks [@rsalmei](https://github.com/rsalmei) for the cool and useful progress bar!
