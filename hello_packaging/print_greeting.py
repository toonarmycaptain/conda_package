

def greeting(name: str = None) -> None:
    """Prints a greeting."""
    addressee = f'to {name} ' if name else ''
    print(f"Hello {addressee}from a package!")

if __name__ == "__main__":
    ...


