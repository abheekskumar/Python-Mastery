def main(*args,**kwargs) -> None:
    """
    Prints out poitional and keyword arguments
    """
    print("Positional:",args)
    print("Keyword:",kwargs)


main(23,234,name = "balls")
    