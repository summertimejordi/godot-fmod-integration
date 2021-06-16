def can_build(env, platform):
    return platform == "x11" or platform == "windows" or platform == "osx" or platform == "android" or platform == "iphone"


def configure(env):
    pass
