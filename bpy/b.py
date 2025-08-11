def print_hello() -> int:  # Wrong return type annotation
    # This will cause a pytype error but run fine at runtime
    # Function claims to return int but actually returns None
    print("Hello from bpy!")
    # No return statement, so returns None, but annotation says int
