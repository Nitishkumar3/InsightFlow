

from parrot import Parrot
import warnings
from time import time
warnings.filterwarnings("ignore")
import re

def split_into_sentences(text):
    pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
    sentences = re.split(pattern, text)
    return sentences



parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

String = "Almost twenty years ago Gmail was announced on April Fools Day, but despite many assuming it was a hoax, the service was in fact real. Gmail's launch was revolutionary in that it offered a massive gigabyte of storage, a far cry from the 15 megabyte inboxes of the time, at no cost. However, what truly set Gmail apart was its fast search capabilities and a whole new way of presenting ads. Instead of traditional banner ads, Gmail employed a small strip along the top of the inbox that displayed targeted ads related to the user's emails. Gmail's journey over the past two decades has been marked by constant evolution. The clean and uncluttered interface from launch remains the same today. However, new features have been introduced, such as the ability to archive emails, smart replies, summary cards, and a one-click unsubscribe button. While Gmail may not be as central to our lives as it once was, with the rise of messaging apps like Slack and WhatsApp, it remains an indispensable tool for online communication. Its search capabilities are unmatched, and it serves as a reliable repository for important information. Google is aware of the changing landscape of online communication and is working to reintroduce delight to the inbox while alleviating the laborious aspects of managing an inbox. The company is exploring new ways to utilize AI to help users with tasks such as scheduling appointments and suggesting relevant emails."
phrases = split_into_sentences(String)



# phrases = ["Can you recommend some upscale restaurants in Newyork?",
#            "What are the famous places we should not miss in Russia?"
# ]

s = time()

final = []
count=1
for phrase in phrases:
  print(count, " / ", len(phrases))
  para_phrases = parrot.augment(input_phrase=phrase, use_gpu=False, max_return_phrases = 1)
  final.append(para_phrases[0][0])

stringf = " ".join(final)
print(stringf)
e = time()
print(e-s)