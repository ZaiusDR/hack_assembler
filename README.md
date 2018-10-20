# Hack Assembler

Final project for the Assembler to compile "Hack" assembly language, used in the computer architecture proposed in Coursera's MOOC [From Nand to Tetris I](https://www.coursera.org/learn/build-a-computer/).

## Installing

`pip install git+https://github.com/ZaiusDR/hack_assembler`

## Usage

After installation, a `hack_assembler` command is available:

`hack_assembler File.asm`

This will produce a `.hack` file which can be used in the CPU Emulator provided in the course.

## Running tests

### Unit testing

Tests run with pytest. You can install this library with:

`pip install pytest`

In order to run unit tests:

- Clone repository: `git clone https://github.com/ZaiusDR/hack_assembler.git`

- Navigate to the repository folder: `cd hack_assembler`

- Install in development mode: `pip install -e .`

- Run tests: `pytest`
