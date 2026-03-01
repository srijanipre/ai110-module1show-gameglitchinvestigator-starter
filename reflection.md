# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
The hint boundaries seem like they're switched. If the number was 45, the hints say "go higher" for a guess of 46 and "go lower" for a guess of 44. The update_score function is wrong and gives the user 5 points even though the user got the guess wrong, and this only happens on even attempts. Another bug is that the hard difficulty level is actually easier than the normal level, the HARD being 1-50, while normal is 1-100. Finally, when we reset the game, the secret number actually ignores what easy mode the user set, and automatically goes to a 1-100 range. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I used Claude code to explain the instructions in a more detailed way to me, and I also used Claude chat integration to help debug my code. One example of an AI suggestion that was correct was I mistakenly identified where in the code the bug for the hardcode reset for 1-100 was. AI correctly identified that it was within the app.py file and not the logic_utils.py file. I verified this by changing the hardcoded result and it was actually reflected in the local host. One example of an AI suggetion that was wrong wasn't something concrete, but I noticed that if we don't tell AI what the exact bug was and where in the code we found it, it edits more files than what is actually necessary. For example for the bug where the difficulty level is actualy easier than the easy level, the AI actually started fixing other bugs that were not a part of this one as I didn't specify where in the code I found this bug. I fixed this by again prompting it to focus on the logic file with this specific bug.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
After the AI debugged an error, I would immedietly go an check that on the local host. Even for the testcases, I would make sure to run pytest within the virtual environment to make sure that all tests had passed. One testcase for the easy difficulty being harder than the hard difficulty was when it checked to see if the boundaries for the easy difficulty were lower than the hard. AI helped design and understand these test cases as it showed the user it's thought process for every step it took.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
