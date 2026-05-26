# Guido's Command Dispatch Pattern

I've got a favorite Python design pattern but it now seems to have been lost in the mists of time, a Command Dispatch pattern.  Guido van Rossum described the pattern in a Python mailing list in 1997. Amazingly, I can't find that mailing list archived anywhere.  You would hope that every word that Guido ever wrote about Python would be archived somewhere! There's a pointer to it here but the link no longer exists. Look for "Guido van Rossum's Command Dispatch pattern":
> https://legacy.python.org/workshops/1997-10/proceedings/savikko.html

The pattern itself is, in my opinion, amazingly elegant and like all elegant things, quite simple. Maybe the reason I can't find it documented anywhere is because it's so simple that it's obvious to everybody else. But for years, I had to go look it up every time I wanted to use it and when I couldn't find it online anymore, I had to re-write it from memory as best I could, updating for the latest Python syntax, of course.

The heart of the pattern is the fact that you can access methods in a class by name by passing a string into `getattr()`. This makes it simple to turn strings into method calls.
