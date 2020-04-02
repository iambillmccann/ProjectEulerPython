# ProjectEuler
Project Euler was started by Colin Hughes (a.k.a. euler) in October 2001 as a sub-section on mathschallenge.net. Who could have known how popular these types of problems would turn out to be? Since then the membership has continued to grow and Project Euler moved to its own domain in 2006.

## What is this?
It is important to code every day to keep our skills sharp. I have created this repository for my solutions to Project Euler challenges. This particular repository contains my solutions written in Python. I have similar repositories for C#, Rust, Java, Scala, and C++.

## Structure of this code
This application runs as a console application. It is build for Python 3.6. It was developed on Ubuntu Linux via the WSL and a virtual environment named "venv". The main program (main.py) runs from the root folder. There are two modules off the root. These are:

- ** projecteuler ** this is the modules for the solution's classes and function libraries.
- ** tests ** these are the unit tests for the solution.

## Main Program
The main program prompts the user for a problem number, then runs the appropriate problem and reprompts the user. To end the program the user types "q" and presses enter.

The main program calls functions to validate the user's input, and then uses a factory pattern to obtain the class for the selected problem. Run times are tracked and reported by the main program.

## projecteuler
The EulerLibrary is the SDK for the solutions. The library is composed to two child libraries: MathLibrary and Problems.

### MathLibrary
The MathLibrary contains the algorithms needed to solve the problems. There are two source files in this module, these are:

- ** MathLibrary.cs ** this contains match functions, such as finding lowest common denominators or prime numbers.
- ** Utilities.cs ** this contains miscellaneous utilities, such as formatting of milliseconds as HH:MM:SS:mmm.

## Problems
The Problems module contains the solutions to the Project Euler problems. Each problem has its' own source file. In addition, the factory class (ProblemFactory.py) is here. The factory accepts an integer problem number and returns the appropriate class to solve that problem. The problems are based on the base class *IEulerSolution*.