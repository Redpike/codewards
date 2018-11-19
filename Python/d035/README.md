### Sat Nav directions

**Background**

It is the middle of the night.

You are jet-lagged from your long cartesian plane trip, and find yourself in a rental car office in an unfamiliar city.

You have no idea how to get to your hotel.

Oh, and it's raining.

Could you be any more miserable?

But the friendly rental-car dude behind the desk says not to worry! He kindly pre-programs the car Sat Nav system with your destination. He smiles and assures you that the device works OK. What excellent service! What a nice man!

Maybe things are not so bad after all.

Then he sniggers...

**City streets**

The city extends as far as the eye can see in all directions, and is laid out as a giant grid where all blocks are 1km across.

Notice that [x,y] coordinates are described with units of 100m

![satnav city streets](https://i.imgur.com/6MFbhPO.png)

**Kata task**

Your starting point is [0,0]

Simply follow the Sat Nav directions!

When you arrive at the destination return the final coordinates.
Sat Nav directions

The device gives directions as text messages:

The first message

    Head <NORTH,EAST,SOUTH,WEST>

The en-route messages

    Take the <NEXT,2nd,3rd,4th,5th> <LEFT,RIGHT>
    Go straight on for <100,200,300,...,900>m
    Go straight on for <1.0,1.1,1.2,...,5.0>km
    Turn around!

The last message

    You have reached your destination!

NOTES

    First and last messages are always present
    There may be any number of en-route messages
    Messages are always formatted corrrectly
    A NEXT turn message means you must to proceed to the next cross-street even if you are currently at an intersection
    But Turn around does not need to be done at an intersection. Just do a U-turn wherever you are!
