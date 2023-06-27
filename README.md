# Game_of_graphs
Repository for the project of Analysis of Large Scale Social Networks at KU Leuven

## About
Game of Thrones is an American fantasy drama television series created by David Benioff and D. B. Weiss for HBO. It is an adaptation of A Song of Ice and Fire, a series of fantasy novels by George R. R. Martin, the first of which is A Game of Thrones. 

<img src="https://m.media-amazon.com/images/M/MV5BN2IzYzBiOTQtNGZmMi00NDI5LTgxMzMtN2EzZjA1NjhlOGMxXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_FMjpg_UX1000_.jpg" height = "600" width="500"></img>

Set on the fictional continents of Westeros and Essos, Game of Thrones has a large ensemble cast and follows several story arcs throughout the course of the show. The first major arc concerns the Iron Throne of the Seven Kingdoms of Westeros through a web of political conflicts among the noble families either vying to claim the throne or fighting for independence from whoever sits on it. The second focuses on the last descendant of the realm's deposed ruling dynasty, who has been exiled to Essos and is plotting to return and reclaim the throne. The third follows the Night's Watch, a military order defending the realm against threats from beyond Westeros's northern border.

## Dataset

The dataset for this project can be found at [gameofthrones](https://github.com/mathbeveridge/gameofthrones) by Andrew Beveridge. It is based on the interactions between the characters in the series.

## Instructions

The repo has two folders:

- Final  - this is the final set of notebooks that are being submited for grading. There are 3 notebooks:
  - Part1_Introduction_AND_Graph_Creation: This notebook concerns with creating the neo4j database with the nodes and edges.
  - Part2_Community_Mining: This notebook contains the community detection and various centrality measures.
  - Part3_Link_Prediction: This notebook contains the link prediction on the network.
- notebooks - this folder contains the initial notebook and experimental work done throughout the project.

Before running the notebooks, please follow the following steps:
  - create a virtual environment
    ```Python
    conda create -n game_of_graphs
    ```
  - activate the virtual environment
    ```Python
    conda activate game_of_graphs
    conda install pip
    ```
  - install the modules using the requirements.txt
    ```Python
    pip install -r requirements.txt
    ```
  - create a new database in neo4j and start it
  
  Now you can run the notebooks in chronological order from Part1 to Part3.

## Individual contribution and gained knowledge:

### Aleksandra Elena Getman
I contributed to this project by developing the 5 centrality measures (i.e., degree, weighted degree, eigenvector, PageRank, and betweenness) and deriving the communities in different seasons using Leiden Algorithm. I was also responsible for generating the training, validation, and testing sets by creating positive instances using the true edges and nodes from the graph and developing negative instances (i.e., non-existing edges) by looking what are the possible pairs of nodes that are between 2 and 3 hops away from each other. After a random forest classifier was introduced using the number of common neighbors, preferential attachment, and Adamic Adar as features. This project taught me how valuable and powerful graph databases are, as basic information about the nodes and weighted edges enables them to provide details on which nodes are the most important in a network and allows them to introduce graph embeddings for link prediction. This project also allowed me to understand deeper how Neo4j works and how it can be integrated in Jupiter's notebook.

### Vaishnav Dilip


## References:
  - [Game of Thrones](https://en.wikipedia.org/wiki/Game_of_Thrones)
  - [Dataset](https://github.com/mathbeveridge/gameofthrones)
