############
# This script parses an inventory and connects via SSH to a host
#
# TODOs:
# - optionnaly read ansible.cfg to get remote_user / or take it from the command line
# - read inventory group/host var to get specific ansible_user value
############

import argparse
import os
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager

parser = argparse.ArgumentParser(description='Connect to host declared in inventory, using group name. If several hosts in group, the rank can be provided either on command line or interactively')
parser.add_argument('--environment', '-i', required=True, help='Environment directory (containing hosts file) - or path to inventory')
parser.add_argument('--group', '-g', required=True, help='Group name')
parser.add_argument('--rank', '-r', required=False, help='Host rank in group')

args = parser.parse_args()

def error(message):
    """
    display error message and exits
    """
    print('ERROR ', message)
    exit(1)


def print_hosts(group):
    """
    display the hosts from a group
    """
    print("The "+args.group+" group contains "+ str(len(group)) +" hosts:")
    i=0
    for h in group:
        print("[", i, "] ", h)
        i += 1

def connect(group, rank):
    """
    connects to a host
    """
    print("connecting to ", group[rank])
    os.system("ssh " + group[rank])
    exit(0)

# Load inventory
inventory = InventoryManager(DataLoader(), sources=args.environment)

rank = None;
if args.rank is not None:
    rank = args.rank

try:
    group = inventory.get_groups_dict()[args.group]
except KeyError as ke:
    error("Unknown group " + args.group)

if len(group) == 0:
    error("Group "+group+" is empty")

if rank is None:
    if len(group) == 1:
        # connect
        connect(group, 0)
    else:
        # ask for rank
        print_hosts(group)
        rank = int(input("Choose host rank: "))

if rank < len(group):
    # connect
    connect(group, rank)
else:
    # error
    error(str(rank) + " is not valid - must be in [0 ; " + str(len(group) - 1) + "]")


