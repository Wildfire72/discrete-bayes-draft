This repository contains a simulator for a Magic: the Gathering draft that utilizes a Discrete-Bayes Filter.

Dependencies:
  - MatPlotLib
  - NumPy

Files:
  - main.py
      - Runs Simulatation
      - Can perform a single iteration or run a suite
  - Filter.py
      - Player's Discrete Bayes Filter
  - Sim.py
      - Main interface for simulation
      - Contains "true state"
  - Player.py
      - Superclass for a generic drafter
  - Pack
      - Collection of cards
