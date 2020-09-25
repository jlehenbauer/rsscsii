# Karel Reference

## Karel's Abilities

 - `move()` - Karel moves one space in the direction Karel is facing
 - `turn_left()` - Karel turns left once (90 degrees counter-clockwise)
 - `pick_beeper()` - Karel picks up a beeper on Karel's current spot
 - `put_beeper()` - Karel places a beeper on Karel's current spot

## Karel's Checks

| Positive conditions | Negative conditions |
| ------------------- | ------------------- |
| `frontIsClear()` | `frontIsBlocked()` |
| `leftIsClear()` | `leftIsBlocked()` |
| `rightIsClear()` | `rightIsBlocked()` |
| `beepersPresent()` | `noBeepersPresent()` |
| `beepersInBag()` | `noBeepersInBag()` |
| `facingNorth()` | `notFacingNorth()` |
| `facingEast()` | `notFacingEast()` |
| `facingSouth()` | `notFacingSouth()` |
| `facingWest()` | `notFacingWest()` |