import logging
import pprint
import subprocess
import sys

from shared_utils import InstrDict, signed

pp = pprint.PrettyPrinter(indent=2)
logging.basicConfig(level=logging.INFO, format="%(levelname)s:: %(message)s")


def make_go(instr_dict: InstrDict):

    args = " ".join(sys.argv)
    prelude = f"""// Code generated by {args}; DO NOT EDIT."""

    prelude += """
package riscv

import "cmd/internal/obj"

// matchFor returns the fixed bits for the given As.
func matchFor(a obj.As) (_ uint32, found bool) {
	switch a {
"""

    endoffile = """	}
	return 0, false
}
"""

    instr_str = ""
    for i in instr_dict:
        instr_str += f"""	case A{i.upper().replace("_","")}:
		return {hex(int(instr_dict[i]["match"], 0))}, true
"""

    with open("inst.go", "w", encoding="utf-8") as file:
        file.write(prelude)
        file.write(instr_str)
        file.write(endoffile)
