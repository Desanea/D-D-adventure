answer = input("""Welcome to ''Hunters of the truth'' a D&D choose-your-own-adventure game" 

You have been summoned to the tiny hamlet of Erwan, as many people have disappearance in the last weeks. 
As an heroic adventurer, this could be your first step into glory!...Or a certain death.
Are you ready to fulfill your destiny and become a hero to be reckon by? (yes/no)""")

if answer.lower().strip() == "yes":

   answer = input("""As so, your adventure begins...
After a few days of traveling you reach the hamlet of Erwan. 
The place seems desolate, as not a single soul can be seen around. An eerie silence engulfs the place as a shallow yellow 
mist engulfs the surroundings. Among the few battered houses, you see two places of interest, one seems to be an inn and
the other a trade post. Where do you want to go? (Inn/trade post""").lower().strip()
    if answer == "inn":
        print("""There's an old crooked wooden post hanging outside of the inn with the name ''The Snappy Raven'' 
on it. As you enter the place you only see one person in the abandon place. A man stands behind the bar.""")

elif answer == "trade post":
     print("""A nice place indeed!""")

else:
    print("Invalid choice. choose the inn or the trade post, sucker")


else:
    print("""An unwise choice. As you choose to leave the hamlet of Erwan, darkness takes over the place.
In a few months it disappears in a mist of shadows, never to be seen again.""")
