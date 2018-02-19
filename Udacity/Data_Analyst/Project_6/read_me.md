Data Visualization: Baseball: The average performance by height

Summary
The goal of this graph is to show that height does not play a big role in a player's batting average and/or number of home runs. The graph animates between each height group depicting the values for each player and the average for that height group. With the animation, viewers can see where the average falls and make comparisons with other height groups.

Data
The data is was provided by Udacity. The data has 1158 elements, each contain 6 fields. When working with the baseball data, some variables data types were transformed from strings to integers. The data that is visualized are people who have some value in batting average other than 0. A player that doesn’t bat cannot have any home runs. Due to this, 266 players have been removed.

Design
While exploring the data, I realized that batting averages has the most visual impact when making the home run comparisons, which is why batting average is on the X-axis. The Y-Axis displays number of home run values, and we can view the data by height, on the right side of the graph.

This time around, a white circle outlined in black (the average circle) has been added to signify the average home runs for the height group. This feature has beed added for venires to gain perspective on how well a player is performing in relations to the average.

Having the average circle along with a point for each player can help show additional anomalies in the data as well. When the average circle is higher or lower, we can see that it is because there are not enough player data in that height group to get accurate measure of player performance.

First Graph - Index1
Interviewer’s Feedback:
- No descriptive enough
- Why do very short players or very tall players have more home runs on average?
- Why are there spikes in the data (drastic changes in averages with just one inches in difference)
- Seems like for the most part, there is only a small relation between height and number of home runs
Changes made:
- Changed graph to show each player value instead of the average
- Change graph to a scatter plot to better show relationships
- Used better labeling for the title and axis

Second Graph - Index2
Interviewer’s Feedback:
- Most players are between 69 inches and 76 inches in height
- Players that bat with both hands have lower number of home runs
- As height increases, there are more variance in number of home runs.
- There are too many data points overlapping and it is hard to tell if there is any type of trend in the data.
- Why is 0 on top of the y axis?
- Too many tick marks

Changes made:
- I have tried on multiple occasions to fix the tick marks, but was never able to solve the problem. I’ve used some dimple.js api and D3 functions but nothing was able to fix the ticks when the “addAxis” was used. The only way I could make it better it is to used a different dimple.js chart object to better organize the data. In doing so, this also fixed the 0 on the Y-axis
- In the 2nd graph it was a little difficult to spot any trends within the data. By placing batting average on the x-axis, a trend can be spotted. I also removed handedness and replaced it with height, because I wanted to stay true to the question of how height plays a role in number of home runs.

third Graph - Index3
Interviewer’s Feedback:
- Better batting averages does not guarantee more home runs, it just gives a better chance of more home runs
- Most players have under 50 home runs
- There are more variance in height as batting averages increases
  height plays a little role in number of home runs
- There are too many ticks are the x-axis
- Challenge to myself: Add animation to the graph and bring back handedness
Changes made:
- By animating the graph allowed me to fix the following issues
  - Reduced the number tick marks
  - Fix the over plotting of data
  - Easier for viewers to read the graph

Udacity Graph 1st review
Feedback:
- The Reviewer stated that the submission of final_index.html was lacking in explanatory  visualization
- A friend mentioned that the graph was a little difficult to process due to the speed of the  animation
Changes made:
- Added the average circle to explain how well baseball players performed overall
- The frame rate has been changed from 3000 to 4000 milliseconds


Resources
Udacity's Data Analyst Course
Stack Overflow
Dimpljs.org
