from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# C:\Users\nitis\.cache\huggingface\hub\models--facebook--bart-large-cnn

text = "Almost twenty years ago Gmail was announced on April Fools Day, but despite many assuming it was a hoax, the service was in fact real. Gmail's launch was revolutionary in that it offered a massive gigabyte of storage, a far cry from the 15 megabyte inboxes of the time, at no cost. However, what truly set Gmail apart was its fast search capabilities and a whole new way of presenting ads. Instead of traditional banner ads, Gmail employed a small strip along the top of the inbox that displayed targeted ads related to the user's emails. Gmail's journey over the past two decades has been marked by constant evolution. The clean and uncluttered interface from launch remains the same today. However, new features have been introduced, such as the ability to archive emails, smart replies, summary cards, and a one-click unsubscribe button. While Gmail may not be as central to our lives as it once was, with the rise of messaging apps like Slack and WhatsApp, it remains an indispensable tool for online communication. Its search capabilities are unmatched, and it serves as a reliable repository for important information. Google is aware of the changing landscape of online communication and is working to reintroduce delight to the inbox while alleviating the laborious aspects of managing an inbox. The company is exploring new ways to utilize AI to help users with tasks such as scheduling appointments and suggesting relevant emails."
output = summarizer(text, max_length=250, min_length=200, do_sample=False)
summary = output[0]["summary_text"]
print(summary)