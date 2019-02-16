
## BCE 4.2: Team Exercise

Code: [BCE_4_2.py](./BCE_4_2.py)

1. Accept two command line arguments (following the name of the program file):

    * the day (e.g., Sunday, Monday…) and
    * the meal (breakfast, lunch, dinner).

    Values for these, as well as the planned specials for the day/meal, are given in the table below.
    
    |         |breakfast | lunch       | dinner    |
    | ------- | -------- | ----------- | --------- |
    |Sunday   |scones    |quesadillas  |veg lasagna|
    |Monday   |oatmeal   |veg burgers  |veg chili|
    |Tuesday  |pancakes  |salad        |veg curry|
    |Wednesday|croissants|burritos     |pad thai|
    |Thursday |waffles   |calzones     |pizza|
    |Friday   |brownies  |veg kabobs   |broccoli quiche|
    |Saturday |eggs      |tortas       |penne with pesto|
    
2. Use the two arguments to look up the special. Print out a statement about these things, similar to “The special for Friday dinner will be broccoli quiche.” 
(Hint: one might store the table above as a dictionary of dictionaries in Python 3.) 

    When the program is run, things should look like the following:
    ```shell
    $ python3 ex3b.py Friday dinner
    The special for Friday dinner will be broccoli quiche.
    $ python3 ex3b.py Tuesday breakfast
    The special for Tuesday breakfast will be pancakes.
    ```

## BCE 4.3: Team Exercise

Code: [BCE_4_3.py](./BCE_4_3.py)

1. Define four classes: Hammer, Pliers, Knife, Screwdriver. Each has only one method: used_for(). The method must return ‘pounds things’ (for Hammer), ‘pulls things’ (for Pliers), ‘cuts things’ (for Knife), and ‘screws things’ (for Screwdriver).

2. Define the class Toolbelt that has one instance of each of these. It also has a used_for() method, but his one returns what the Toolbelt’s component objects are used for. 

3. Create enough code to create object instances to show how the classes can be used with different instantiations.