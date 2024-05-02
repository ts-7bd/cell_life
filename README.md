# Game of life

## Starting the game

python main.py

## Prerequesites

here I used conda 24.3.0 with python 3.11.8
install package pygame

## Description

This module simulates Conway's Game of Life. Cell are reproducing, just surviving, or decaying. At the start an initial set of active cells is set and they grow after following three rules

1. A live cells with fewer than 2 living neighbours dies (underpopulation)
2. A live cell with two or three living neighbours remains alive (survive)
3. A live cell with more than living neighbours dies (overpopulation)

## Interactive mode

This game serves several interactiv features. Just click on one of the following keys.

- _ESC_ - quit the game
- _SPACE_ - pause or continue the simulation
- _c_ - clean up the board
- _g_ - generate a new set of living cells

## Acknowledgements

This simulation was inspired by Tim Ruscica using his [GitHub Page](https://github.com/techwithtim/Conways-Game-Of-Life) and [Youtube Cannel](https://www.youtube.com/watch?v=YDKuknw9WGs&t=1614s).
