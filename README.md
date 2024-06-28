# skimlit-pubmed-rct-200k-data

SkimLit: Extracting Information from PubMed RCT 20k Data
Overview
This project, named SkimLit, aims to extract and classify information from the PubMed RCT (Randomized Controlled Trials) 20k dataset. The dataset consists of 20,000 abstracts of randomized controlled trials, which are annotated with different sections such as background, objective, methods, results, and conclusions. The main goal of the project is to build models that can accurately classify these sections and extract relevant information.

Project Structure
Data Pre-processing
Pre-processing Our Data: The first step involves cleaning and preparing the data for modeling. This includes tokenizing the text, removing stop words, and other standard text pre-processing techniques.

One Hot Encoding and Label Encoding: The target labels (sections of the abstracts) are encoded using one hot encoding and label encoding techniques to convert them into a format suitable for machine learning models.

Baseline Model
A baseline machine learning (ML) model is created to set a benchmark for performance. This model uses traditional ML techniques to classify the sections of the abstracts.

Deep Learning Models
Character Level Embeddings
Deep learning models are employed to improve upon the baseline model. Character-level embeddings are used to capture the detailed structure of the text. These embeddings represent the text at the character level, which helps in understanding the finer nuances of the language used in the abstracts.

Multimodal Model
The project explores a multimodal model that combines different types of embeddings. Specifically, it combines character and token embeddings to leverage both the detailed and high-level information from the text.

Combining Char and Token Datasets: The character and token datasets are merged to create a comprehensive dataset that can be used for training the multimodal model.
Positional Embeddings: Positional embeddings are created to capture the order of words and characters in the text, which is crucial for understanding the context and structure of the abstracts.
Tribrid Model
The final model explored in this project is a tribrid model, which integrates multiple types of embeddings and advanced deep learning techniques to achieve the best performance in classifying the sections of the abstracts.

Results
The models are evaluated based on their accuracy and ability to correctly classify the sections of the abstracts. Detailed results and comparisons between the baseline and advanced models are provided in the project.

Conclusion
The SkimLit project demonstrates the effectiveness of using deep learning and multimodal approaches to classify and extract information from scientific texts. By leveraging character and token embeddings, along with positional embeddings, the models achieve high accuracy and provide valuable insights into the structure of randomized controlled trial abstracts.

Acknowledgments
This project utilizes the PubMed RCT 20k dataset, provided by the authors of the research paper: "An Extensive Study on Automated Scientific Paper Summarization". We thank them for making this dataset publicly available.
The research paper served as a key reference for developing the models used in this project.
