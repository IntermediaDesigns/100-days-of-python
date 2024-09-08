# 👉 Day 61 Challenge


### Someone is *wrong* on the Internet!


Today, we're going to fix the major malfunction with social media - other people and their stupid opinions- and create a Twitter for one! 

I know you like to hear the sound of your own voice!

Your program should.

1. Display a menu - Add or View tweets.
2. 'Add' should:
     1. Get the tweet input.
     2. Store it to the database with the current timestamp as the key value.

4. 'View' should:
     1. Show the tweets in reverse chronological order.
     2. Show 10 tweets at a time.
     3. Prompt the user to show another 10 tweets (yes or no).
     4. A 'no' choice goes back to the menu.


Timestamp Code:
```python
timestamp = datetime.datetime.now()
```



<details> <summary> 💡 Hints </summary>
  
- Use the `datetime` library to get the current timestamp.
- Use the `os` library to clear the console between each 10 tweets shown.

</details>
