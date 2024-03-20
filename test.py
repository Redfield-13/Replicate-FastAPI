import json

# Sample JSON data (replace with your actual data)
data = [{"start": 0.169, "end": 7.617, "text": " After reading tons of productivity books, I came across so many rules like the two year rule, the five minute rule, the five second rule.", "words": [...]}, {"start": 7.797, "end": 9.319, "text": "No, not that five second rule.", "words": [...]}]






combined_text = ""
for item in data:
  combined_text += item["text"] + " "  # Add a space after each text chunk

# Print the combined text
print(combined_text.strip())