from content.link import Endpoint

root = \
    f"""
    root<br>
    {Endpoint.branch}
    {Endpoint.hello}
    """

branch = \
    f"""
    {Endpoint.root}
    branch<br>
    {Endpoint.hello}
    """

hello = \
    f"""
    {Endpoint.root}
    {Endpoint.branch}
    hello
    """
