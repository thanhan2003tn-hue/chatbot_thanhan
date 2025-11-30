<p align="center"><h1 align="center">CHATBOT_RAG</h1></p>
<p align="center">
	<img src="https://img.shields.io/github/license/nd-wuangr26/Chatbot_RAG?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/nd-wuangr26/Chatbot_RAG?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/nd-wuangr26/Chatbot_RAG?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/nd-wuangr26/Chatbot_RAG?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

<strong>Chatbot_RAG</strong> is a custom-built AI chatbot that leverages the Retrieval-Augmented Generation (RAG) architecture to provide accurate and context-aware answers based on external documents. Unlike traditional language models that rely solely on pre-trained knowledge, this chatbot retrieves relevant information from a custom knowledge base and combines it with generative capabilities for more reliable responses.


---

##  Features

 The <strong>Chatbot_RAG</strong> project integrates Retrieval-Augmented Generation (RAG) to create a more intelligent and reliable chatbot by combining the strengths of information retrieval and generative language models. It supports loading and processing documents from various formats (such as PDF and text), chunking them semantically or by fixed size, and generating embeddings using HuggingFace or OpenAI models. These embeddings are stored in efficient vector databases like FAISS or Chroma, allowing fast and accurate retrieval of relevant content. Built on the LangChain framework, the chatbot architecture is modular and flexible—making it easy to plug in different components such as retrievers, language models, or custom prompts. With support for natural language queries, dynamic knowledge updates, and a configurable pipeline, this chatbot is designed for scalability, adaptability, and real-world deployment.

---

##  Project Structure

```sh
└── Chatbot_RAG/
    ├── __pycache__
    │   ├── main.cpython-310.pyc
    │   ├── serve.cpython-310.pyc
    │   └── service.cpython-310.pyc
    ├── core
    │   ├── chunking
    │   ├── embeding
    │   ├── llm
    │   ├── rag
    │   └── retreival
    ├── frontend
    │   └── app.py
    ├── main.py
    ├── requirments.txt
    └── serve.py
```


###  Project Index
<details open>
	<summary><b><code>CHATBOT_RAG/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/serve.py'>serve.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/main.py'>main.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/requirment.txt'>requirment.txt</a></b></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- core Submodule -->
		<summary><b>core</b></summary>
		<blockquote>
			<details>
				<summary><b>chunking</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/chunking/fixsize_chunks.py'>fixsize_chunks.py</a></b></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/chunking/semantic_chunk.py'>semantic_chunk.py</a></b></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/chunking/docling_chunk.py'>docling_chunk.py</a></b></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>rag</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/rag/rag.py'>rag.py</a></b></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>embeding</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/embeding/base.py'>base.py</a></b></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/embeding/HuggingEmbed.py'>HuggingEmbed.py</a></b></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/embeding/embedings.py'>embedings.py</a></b></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/embeding/Sentence_Transformer.py'>Sentence_Transformer.py</a></b></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/embeding/doc_embeding.py'>doc_embeding.py</a></b></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>llm</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/llm/gemini_llm.py'>gemini_llm.py</a></b></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/llm/deepseek_llm.py'>deepseek_llm.py</a></b></td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>retreival</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/retreival/retrieval_FAISS.py'>retrieval_FAISS.py</a></b></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/core/retreival/test.py'>test.py</a></b></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- frontend Submodule -->
		<summary><b>font-end</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/nd-wuangr26/Chatbot_RAG/blob/master/font-end/app.py'>app.py</a></b></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with Chatbot_RAG, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python


###  Installation

Install Chatbot_RAG using one of the following methods:

**Build from source:**

1. Clone the Chatbot_RAG repository:
```sh
❯ git clone https://github.com/nd-wuangr26/Chatbot_RAG
```

2. Navigate to the project directory:
```sh
❯ cd Chatbot_RAG
```

3. Install the project dependencies:

echo 'INSERT-INSTALL-COMMAND-HERE'



###  Usage
Run Chatbot_RAG using the following command:
echo 'INSERT-RUN-COMMAND-HERE'

###  Testing
Run the test suite using the following command:
echo 'INSERT-TEST-COMMAND-HERE'

---

##  Contributing

- **[Join the Discussions](https://github.com/nd-wuangr26/Chatbot_RAG/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/nd-wuangr26/Chatbot_RAG/issues)**: Submit bugs found or log feature requests for the `Chatbot_RAG` project.
- **[Submit Pull Requests](https://github.com/nd-wuangr26/Chatbot_RAG/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/nd-wuangr26/Chatbot_RAG
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/nd-wuangr26/Chatbot_RAG/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=nd-wuangr26/Chatbot_RAG">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
