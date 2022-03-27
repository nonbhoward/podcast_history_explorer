from content.link import Endpoint

root = \
    f"""
    root<br>
    {Endpoint.branch}<br>
    {Endpoint.hello}<br>
    """

branch = \
    f"""
    {Endpoint.root}<br>
    branch<br>
    {Endpoint.hello}<br>
    """

hello = \
    f"""
    {Endpoint.root}<br>
    {Endpoint.branch}<br>
    hello
    """
