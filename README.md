# CurvyPathGen
**Language:** Python  

**Purpose:** To generate and graph a random curved path between the start and end points input by the user. Note that the user may also choose the type of curved path (i.e. `cubic`, with 2 turning points; `quartic`, with 3 turning points, etc.). The random curved path generator can be used in games when characters (i.e. objects for player to shoot) must move unpredictably between two points.  

**Running the generator:** 
1. Specify parameters in main.py (i.e. start and end point, number of random paths to generate, etc) 
2. The generator will automatically save graphs of each randomly generated path with the name that the user specifies (default name is TESTx, where x is the path number). Note that each new graph of a generated path will also contain previously generated paths from the same program run so that paths may be easily compared. 

`IMPORTANT:` the path generation is based off a typical Pygame coordinate system, where the origin is in the top left corner and the positive y axis points downward instead of upward, so that generated paths may easily be plotted in a game developed with Pygame. The generator is idealized for paths that move from the top of the screen to the bottom of the screen. 

**See `exampleCubic1`, `exampleCubic2`, and `exampleCubic3` (cubic path, 3 randomly paths generated, start point was (0, 0), end point was (0, 10)) for example path generations.** 

