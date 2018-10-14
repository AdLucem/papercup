"""Parse the command-line input and return the command mapping for it"""


def tokenize(cmd):
    """Tokenize the incoming command string"""

    tokens = cmd.split(" ")
    return tokens


def parse_add(opts):
    """If first token is 'add', parse the options"""

    if opts = []:
        return ["add_paper"]
    else:
        return ["invalid"]


def parse_show(opts):
    """If first token is 'show', parse the options"""

    if opts == []:
        return ["show_paper"]
    elif opts[0] == "--all" and opts[1] == "--titles":
        return ["list_titles"]
    elif opts[0] == "--all" and len(opts) == 1:
        return ["show_all"]
    else:
        return ["invalid"]


def parse_scan(opts):
    """If first token is 'scan', parse the options"""

    if opts == []:
        """Scan all the papers in the /data directory and include them in the table"""
        return ["scan"]

    elif opts[0] == "--all" and len(opts) == 1:
        """Initialise the table- empty all existing entries- then call scan"""
        return ["init", "scan"]

    else:
        return ["invalid"]


def parse(cmd):
    """Parse the input command and return a list
    of tasks for the program to perform"""

    tokens = tokenize(cmd)

    if tokens[0] == "scan":
        return parse_scan(tokens[1:])

    elif cmd == "query":
        """Query a paper in the database by title"""
        return ["query"]

    elif cmd == "del":
        """Delete a paper in the database by title"""
        return ["delete"]

    elif cmd == "list":
        """List the titles of all the papers in the database"""
        return ["list_titles"]

    elif cmd == "show --all":
        """Show the contents of all papers in the database"""
        return ["show_all"]

    elif cmd == "show":
        """Show the content of a specific paper, identified by title"""
        return ["show"]

    elif cmd == "exit":
        return ["exit"]

