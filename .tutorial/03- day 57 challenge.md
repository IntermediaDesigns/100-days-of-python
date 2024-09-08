# 👉 Day 57 Challenge

Try to use recursion to build a factorial program.

Yep, it's a math challenge. Recursion is often good for this type of problem.

It could be a real head scratcher, so don't be afraid to use [100 Days of Code Community](https://replit.com/100-days-code) or the [Discord channel](https://replit.com/discord) for help.

A factorial is the product of all the numbers up to a value, starting from 1.

For example, factorial 5 would be 1 * 2 * 3 * 4 * 5 = 120

1. Write a function that:
    1. Starts at the highest number.
    2. Multiplies that by factorial of itself minus one
    3. Terminates when it reaches 1 and returns 1
    4. Outputs the factorial.


Example:

```
🌟Factorial Finder🌟

Input a number > 5

The factorial of 5 is 120.
```

<details> <summary> 💡 Hints </summary>
  
- Don't forget to return 1 in your terminating condition.
- Try multiplying the number by the factorial (n-1) call.

</details>