# Analysis of a Wikipedia Webpage Using Python and Docker

## 1. Introduction

This project presents a Python-based application designed to analyze the structural and textual characteristics of a Wikipedia webpage. The program retrieves the HTML content of the *University of Calgary* Wikipedia page and extracts meaningful information, such as the number of headings, links, paragraphs, word frequencies, and paragraph lengths. The results are partially visualized using a bar chart.

To ensure portability and reproducibility, the application is containerized using Docker. This allows the program to be executed in a consistent environment without requiring local dependency installation.

---

## 2. Objectives

The primary objectives of this project are:

- To demonstrate web scraping techniques using Python
- To analyze the structure and textual content of an HTML document
- To perform basic text processing and frequency analysis
- To visualize extracted data using Python libraries
- To deploy the application in a containerized environment using Docker

---

## 3. Tools and Technologies

The following tools and technologies were used in this project:

- **Python 3**
- **Requests**
- **BeautifulSoup4**
- **Matplotlib**
- **Docker**

---

## 4. Program Description

### 4.1 Webpage Retrieval

The application sends an HTTP GET request to the Wikipedia page using the `requests` library. Error handling is implemented to ensure the request was successful before continuing execution.

### 4.2 HTML Parsing and Structural Analysis

The retrieved HTML content is parsed using BeautifulSoup. The program counts the occurrences of the following HTML elements:

- Headings (`h1` through `h6`)
- Hyperlinks (`<a>`)
- Paragraphs (`<p>`)

The total number of headings is computed by summing all heading levels.

---

### 4.3 Text Processing and Word Analysis

The textual content of the webpage is extracted and processed to:

- Allow the user to input a word and count its occurrences
- Remove non-alphanumeric characters
- Identify the five most frequently occurring words
- Determine the largest paragraph based on word count

---

### 4.4 Data Visualization

The program generates a bar chart comparing the counts of:

- Headings
- Links
- Paragraphs

This visualization is produced using Matplotlib.

---

## 5. Docker Usage

The application is containerized using Docker to ensure portability and consistent execution across different systems.

### 5.1 Building the Docker Image

To build the Docker image, run the following command from the project directory:

```bash
docker build -t web-analyzer .
```

To run the container:

```bash
docker run -it --rm web-analyzer
```




