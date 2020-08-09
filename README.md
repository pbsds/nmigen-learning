# This thing

This is me playing around with my new Icebreaker FPGA and nmigen(_dg).
The goal is to find a nice project structure and perhaps find a way to
work on my Arty a7 with a fully FOSS toolchain for once.

My focus is currently on:

	* Effortless dependency management
	* Helper functions for inspection and documentation of the design
	* Helper functions for targeting multiple FPGA platforms and boards
	* Creating PRs to other projects with stuff i find here
	* Having fun with my FPGA

# Setup

	pip install --user poetry
	poetry config --local virtualenvs.in-project true # optional, makes cleanup easier
	poetry install

And these optional dependencies, installed inside the virtualenv:

	poetry install -E yosys
	poetry install -E nextpnr-ice40
	poetry install -E nextpnr-ecp5

# Running stuff

	poetry run python -m fpga.icebreaker
	poetry run python -m fpga.modules.blinker generate

To reduce the amount of typing:

	poetry shell


# todo:

* Diagrams are nice
* Documentation generation would be nice
* A central nmigen-pmod library would be nice
* A RISCV toolchain would be nice (make socs, and compile C, C++ or Rust)
* nextpnr-xray or vtr would be nice
* Batch setup of Vivado would be nice
* Ability to synth on a host accessible with ssh would be nice
