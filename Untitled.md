**[Open with the live app on screen at [https://nlp-moviereview.streamlit.app/](https://nlp-moviereview.streamlit.app/)]**

Hey, so for Topic 4 I built a movie review sentiment analyzer using PyTorch and Streamlit, and I actually deployed it live — you can see it running right here. I'm going to walk you through what it does, how I built it, and some interesting things I found when I tested it with translations.

---

**[Point to the two tabs]**

So the app has two tabs. The first one is the main sentiment analysis tab where you can paste in any movie review and it'll tell you whether it's positive or negative and how confident it is. The second tab is for comparing an original review to a translated version, which I'll get to in a minute.

Let me start with a quick demo.

---

**[Paste the Shawshank Redemption review into the text box and click Analyze]**

I'm going to paste in a review for Shawshank Redemption — something along the lines of "the ultimate story of friendship, of hope, and of life. If you haven't seen it, you need to watch it, it's amazing, 10 out of 10."

**[Point to the result]**

So the model comes back 99.9% confident that this is positive, and you can see the score bar is basically full. That makes sense — words like "amazing", "hope", and "best" are ones the model saw a lot in positive reviews during training, so it's very sure about this one.

Now if I open up the Preprocessing Pipeline section here, you can actually see what the model is reading. It lowercases everything, strips out the punctuation and numbers, splits it into individual words, and converts each word to a number using a lookup table called the vocabulary. Everything gets padded or trimmed to exactly 200 words before it goes into the model. That step is important — without it you can't feed different-length reviews through the same network.

---

**[Clear and paste a negative review — use something like "This movie was a complete waste of time, the acting was terrible and the script made no sense"]**

Now let me try a negative one.

**[Point to result — should show Negative with high confidence]**

And you can see it flips to negative. The score bar is close to empty. Words like "terrible" and "waste" are ones the model heavily associates with negative reviews.

---

**[Briefly talk to camera or narrate over a static shot of the code/documentation]**

So quickly on how this is actually built — the app is split into two layers. The backend, which is in model_service.py, handles all the model logic. It loads the trained weights, runs the preprocessing, and returns a prediction as a dictionary. The frontend, which is the Streamlit app, just takes that dictionary and displays it. The two layers don't know about each other's details, which means if I wanted to swap out the interface or upgrade the model later, I only have to change one side.

The model itself is trained on the IMDB dataset — about 20,000 movie reviews. It uses an embedding layer to turn each word into a list of 128 numbers, averages those across the whole review to get one summary vector, and then runs that through two fully connected layers to get a final probability. Training ran for 5 epochs and hit about 83% validation accuracy.

---

**[Show the training curves plot — either in the documentation HTML or as an image]**

Looking at the training curves, you can see both lines dropping nicely for the first three epochs, but after that the training loss keeps falling while the validation loss starts ticking back up. That's overfitting — the model starts memorizing the training data instead of learning patterns that work generally. 83% is a solid result for this architecture, but stopping at epoch 3 would've been slightly better.

---

**[Switch to the Translation Comparison tab]**

Now the translation comparison tab is where things get really interesting. The idea was to take a review, translate it into another language and back to English, and see if the model's prediction changes.

**[Paste in Experiment 3 — original and translated versions side by side]**

So here's one that surprised me. The original review says "I don't know why I like this movie so well, but I never get tired of watching it." The model correctly reads that as Positive. But after translating it through Spanish and back, it comes out as "I don't know why I like this movie so much." Just "well" changed to "much." And that flipped the prediction all the way from Positive down to Negative, with a score change of about 0.6.

**[Paste in Experiment 10]**

And this one is even more dramatic. "Malcolm McDowell has not had too many good movies lately, and this is no different." Clearly negative, and the model gets it right. But after translation it becomes "Malcolm McDowell has made many good films lately." The word "not" basically disappeared from the sentence structure, and the model sees "good films" and calls it 80% positive. That's a 0.8 swing just from one translation step.

**[Point to the delta and changed warning]**

You can see the app flags that the label changed and shows you the delta score. It also lists the words that were in one version but not the other, which helps you figure out exactly what the translation changed.

---

**[Wrap up — can be talking to camera or narrating over the app]**

Out of 10 experiments I ran, 8 preserved the correct label and 2 flipped completely. The model handles direct synonym swaps pretty well — like "boring" becoming "tedious" barely moved the score. Where it really struggles is when translation changes the structure of a sentence, especially anything involving negation. The model averages all the words together equally, so it doesn't give any extra weight to words like "not" or "never." That's a known limitation of this kind of architecture, and it's something that more advanced models like transformers are designed to handle better.

Overall this was a solid project for getting hands-on with the full pipeline from raw text all the way to a deployed application, and the translation testing gave me a much better feel for where these models actually break down in real use.

Thanks for watching.