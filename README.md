# TikTok_Performance_Predictor

Project coded in Python: using pandas to read TikTok Performance Data, scikit-learn to train/test model making predictions, matplotlib to plot the results...

# Why I built this:
There's so much information circulating about the importance of TikTok post times. But, something that didn't circulate was a general sense of skepticism for the importance of this variable. Because, recall that there isn't any publicly available information from TikTok about its algorithm. Therefore, any claim about post times is speculative, giving me a perfect reason to test these claims on my own.

# The data:
I collected this data from using TikTok's "Download your data" in-app feature. Performance data for a total of 71 videos is what was produced. The export lacked view counts, had to collect it by hand. I gitignored the raw export of data. 

# Results:
Test accuracy was ~60%, versus a 50% coin-flip baseline - and only 15 test videos, so it's noisy and modest, not a slam dunk.
Feature importance ranked hour highest (~58%), then sound (~32%), then weekday (~10%).
The tree's biggest single split was sound: your borrowed/trending sounds tended to outperform your own original audio.


# What this project does:
It parses the messy Posts.txt file into a clean table, taking note of hour, weekday, and original vs non-original sound. Also, the prediction metric I created is called "hit," which is how I determine if a video performed well or not (calculated by seeing if video performs above account's median view count).

# How to run it:
First, run the parser. That'll get the raw data formatted correctly. Then use the notebook to train the DecisionTree model, and plot its observations.

# Future improvements:
Honestly, it'd be to use a larger dataset. 71 videos is small. Additionally, I'd like to add video length as another feature that the model could use in order to make stronger predictions.
