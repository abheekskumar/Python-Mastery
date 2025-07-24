def main(*args,**kwargs) -> None:
    """
    Prints out poitional and keyword arguments
    """
    ar1 = args[0]
    v = kwargs["name"]
    print(ar1,v)
    print("Positional:",args)
    print("Keyword:",kwargs)


# allows us to input multiple function arguments
main(23,234,name = "balls")
    