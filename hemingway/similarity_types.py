import redbaron
import sys

SIMILARITIY_NODE_TYPES = set(
    slot[:-4]
    for slot in dir(redbaron)
    if slot.endswith('Node'))
