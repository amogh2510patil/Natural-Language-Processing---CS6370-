# Assignment 1 - Basic Text Processing on Cranfield Dataset

To run your code, run main.py with the appropriate arguments as shown below:

Usage: 
````
main.py [-custom] [-dataset DATASET FOLDER] [-out_folder OUTPUT FOLDER]
        [-segmenter SEGMENTER TYPE (naive|punkt)] [-tokenizer TOKENIZER TYPE (naive|ptb)] 
````

The `DATASET FOLDER` and `OUTPUT FOLDER` are in this directory, at `cranfield/` and `output/` respectively, so the expression to run it with them would be:

`main.py [-custom] -dataset ./cranfield/ -out ./output/ -segmenter (naive|punkt) -tokenizer (naive|ptb)`

Leaving out the `dataset` and `out` arguments will default to the same as above.

When the -custom flag is passed, the system will take a query from the user as input. When the flag is not passed, all the queries in the Cranfield dataset are considered, for example:

````
> python main.py -custom
> Enter query below
> Papers on Aerodynamics
````

This will generate *queries.txt files in the `OUTPUT FOLDER` after each stage of preprocessing of the query and *docs.txt files in the `OUTPUT FOLDER` after each stage of preprocessing of the documents.