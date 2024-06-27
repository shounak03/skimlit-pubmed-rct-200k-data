import tensorflow as tf
import streamlit as st
loaded_model = tf.keras.models.load_model("skimlit_tribrid_model")

def split_char(text):
  return " ".join(list(text))

from spacy.lang.en import English
class_names = ['BACKGROUND', 'CONCLUSIONS', 'METHODS', 'OBJECTIVE', 'RESULTS']
def predict(input_txt):


  nlp = English()


  sentencizer = nlp.add_pipe("sentencizer")

  doc = nlp(input_txt)
  abstract_lines = [str(sent) for sent in list(doc.sents)]

  total_lines_in_sample = len(abstract_lines)


  lines = []
  for i, line in enumerate(abstract_lines):
    sample_dict = {}
    sample_dict["text"] = str(line)
    sample_dict["line_number"] = i
    sample_dict["total_lines"] = total_lines_in_sample - 1
    lines.append(sample_dict)


  line_numbers = [line["line_number"] for line in lines]
  line_numbers_one_hot = tf.one_hot(line_numbers, depth=15)
  line_numbers_one_hot

  total_lines = [line["total_lines"] for line in lines]
  total_lines_one_hot = tf.one_hot(total_lines, depth=20)
  total_lines_one_hot

  abstract_chars = [split_char(sentence) for sentence in abstract_lines]
  abstract_chars

  data = (line_numbers_one_hot, total_lines_one_hot, tf.constant(abstract_lines), tf.constant(abstract_chars))


  pred = tf.argmax(loaded_model.predict(x=data, verbose=0),axis=1)


  res = [class_names[i] for i in pred]

  for i, line in enumerate(abstract_lines):
    print(f"{res[i]}: {line}")


def main():
  st.title("skimlit - medical text made easy to understand")

  input = st.text_input("enter the paragraph")

  res = ''
  if st.button("simplify text"):
    res = predict(input)

  st.success(res)

if __name__ == '__main__':
  main()
