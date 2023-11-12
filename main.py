import sys
from cloudquery.sdk import serve

from plugin import CountsPlugin


def main():
    p = CountsPlugin()
    serve.PluginCommand(p).run(sys.argv[1:])


if __name__ == "__main__":
    main()
