"""
story = 

The Power of Consistency

Rohan was a young student who dreamed of getting a good job in the IT industry. He knew that learning new skills was important, but he often felt confused about where to begin. Every day he watched different videos on YouTube, read articles, and searched for new courses. However, he never completed anything because he kept changing his learning path.

One day, Rohan met his old teacher at a local library. The teacher asked him about his studies and future plans. Rohan explained that he wanted to become a data analyst, but he was worried because there were so many topics to learn. His teacher smiled and said, "Success does not come from learning everything at once. It comes from learning one thing every day."

Those words changed Rohan's thinking. He created a simple study plan. On Monday he studied Excel. On Tuesday he practiced SQL. On Wednesday he learned Python. On Thursday he revised everything he had learned. On Friday he worked on small projects. During the weekend he solved interview questions and improved his communication skills.

The first few weeks were difficult. Sometimes he felt tired. Sometimes he wanted to skip his studies. But he remembered his teacher's advice and continued to follow his plan. Instead of studying for many hours, he focused on studying with full attention for a short time every day.

After three months, Rohan noticed a big improvement. He could write SQL queries without looking at notes. He created Excel dashboards and cleaned data using Python. He also uploaded his projects to GitHub and practiced explaining them in simple English. Every completed project gave him more confidence.

One day, Rohan received an interview call from a company. During the interview, the interviewer asked him about his projects and learning journey. Instead of giving memorized answers, Rohan explained how he had solved real problems using Excel, SQL, and Python. The interviewer appreciated his confidence and practical knowledge.

A week later, Rohan received an email saying that he had been selected for the job. He was excited and immediately thanked his teacher for the valuable advice. His teacher replied, "Talent is useful, but consistency is more powerful. Never stop learning."

Rohan continued to improve his skills even after getting the job. He learned Power BI, statistics, and data visualization. He also helped beginners by sharing his knowledge. He understood that success was not about being perfect but about making small improvements every day.

with open("story.txt", "w") as file:
    file.write(story)
print("Story saved successfully.")
"""
# 1. Read the complete story.txt file.
"""file = open("story.txt", "r")
data = file.read()
print(data)
file.close()"""

# 2. Print only the first line of the file.
"""file = open("story.txt", "r")
data = file.readline()
print(data)
file.close()"""

# 3. Store all lines in a list and print them.
"""file = open("story.txt", "r")
data = file.readlines()
print(data)
file.close()"""

# 4. Add "Thank you!" at the end of the file.
"""
file = open("story.txt", "a")
file.write("\nI love Python.")
file.close()
"""
# 5. Count the total number of characters in the file.

# 6. Count the total number of words in the file.

# 7. Count the total number of lines in the file.

# 8. Check whether the word "Rohan" exists in the file or not.

# 9. Replace the word "Rohan" with "Suraj" and save it in a new file.

# 10. Convert the first character of the file content into uppercase.

# 11. Print the complete text in uppercase.

# 12. Print the complete text in lowercase.

# 13. Take a word from the user and count how many times it appears in the file.

# 14. Copy the file and create a new file named backup.txt.

# 15. Check whether the file exists before deleting it.