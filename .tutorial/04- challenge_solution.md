# Solution (No Peeking!)
![](https://www.youtube.com/watch?v=Dr_dGJEt-dA)

<details> <summary> 👀 Answer </summary>

```python
def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])

print(palindrome("racecar"))

```

</details>

- Join our [100 Days Community](https://replit.com/100-days-help)
- Join our [Discord](https://replit.com/discord)
- Want [live support?](https://replit.com/replit-101)