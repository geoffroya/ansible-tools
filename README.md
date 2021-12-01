# ansible-tools
Various tools around ansible

## Requirements

Those tools obviously require that ansible is installed :)

## Tools list

### ansible-connect

Having big inventories, and long server names?
Why don't using inventory to log into a server using the group name?

Usage: see 'ansible-connect.py -h'

Ok, the command can be quite long, but it can be aliased efficiently:

```bash
$ alias project-connect="python3 ansible-connect.py -i /path/to/env -g "
$ project-connect foo
The foo group contains 3 hosts:
[ 0 ]  server1
[ 1 ]  server2
[ 2 ]  server3
Choose host rank: 2
connecting to  server3
[user@server3 ~]$
```
