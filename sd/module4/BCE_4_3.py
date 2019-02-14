
class Hammer:
    def used_for(self):
        return 'pounds things'


class Pliers:
    def used_for(self):
        return 'pulls things'


class Knife:
    def used_for(self):
        return 'cuts things'


class Screwdriver:
    def used_for(self):
        return 'screws things'


class Toolbelt:
    def __init__(self, tool):
        self.tool = tool

    def used_for(self):
        return self.tool.used_for()


def main():
    hammer = Hammer()
    pliers = Pliers()
    knife = Knife()
    screwdriver = Screwdriver()

    # Create a Toolbelt with hammer and call used_for
    toolbelt = Toolbelt(hammer)
    print(f"Toolbelt with Hammer can {toolbelt.used_for()}.")

    # Change Toolbelt's tool to Pliers and call used_for
    toolbelt.tool = pliers
    print(f"Toolbelt with Pliers can {toolbelt.used_for()}.")

    # Change Toolbelt's tool to Knife and call used_for
    toolbelt.tool = knife
    print(f"Toolbelt with Knife can {toolbelt.used_for()}.")

    # Change Toolbelt's tool to Screwdriver and call used_for
    toolbelt.tool = screwdriver
    print(f"Toolbelt with Screwdriver can {toolbelt.used_for()}.")



if __name__ == "__main__":
    main()