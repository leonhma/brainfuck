## "brainfuck"

This is a interpreter for the complicated language that is ["brainfuck"](https://youtu.be/hdHjjBS4cs8). To use it, download the repo and run `python brainfuck.py text.txt`. Supply the file your program is in as the 2nd argument. It can be in any arbitrary fileformat, as long as it's encoded as `text/*`. Have fun and build something useful! Here's another video to get you started: [link](https://youtu.be/dQw4w9WgXcQ).

## Additional twists

This interpreter has an input-queue. That means, that when `,` is executed, the user is asked for input, which then gets put into the input queue. A following `,` will check the input queue for the next character first, before asking the user for input if nothing is in the queue. This effectively lets you input multiple characters at a time.
