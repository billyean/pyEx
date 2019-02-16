import re

def main():
    with open('plain_story.txt', 'rt') as plainf:
        p_alice_start = '^Alice'
        alice_lines = [line.rstrip('\n') for line in plainf if re.match(p_alice_start, line)]
        alice_thought_lines = [line for line in alice_lines if 'thought' in line]

    with open('Alice_thought.txt', 'wt') as outputf:
        for line in alice_thought_lines:
            print(line, file=outputf)

        print(f'File plain_story.txt has {len(alice_lines)} lines that start with Alice', file=outputf)
        print(f'File plain_story.txt has {len(alice_thought_lines)} lines that start with Alice and contain thought',
              file=outputf)


if __name__ == "__main__":
    main()