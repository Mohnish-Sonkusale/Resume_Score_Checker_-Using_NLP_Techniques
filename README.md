

# Resume Score Checker
## Introduction
Resume Score Checker is an application that analyzes a job seeker's resume and provides a score based on how well it matches the job requirements. Resume Score Checker is designed to scan a job seeker resume template for work experience, skills, education, and other relevant information. It determines if the resume is a good match for the position/Job choosed by the user. It evaluates the resume with the Job Description on scale of 100. This tool can be helpful for job seekers to understand how well their resume is aligned with the job they are applying for.

## Features
1. Analyze resumes based on job requirements
2. Provide a score based on the match between the resume and job requirements
3. Suggest changes to the resume to improve the score

## Text Preprocess Steps

- Convert to lower cases

- Remove Stopwords , new line character (]n) and tab (\t)

- Spell Correction 

- Lemmaitization

## Metrics Used to generate Score 

-  cosine and jaccard similarity
   (TF-IDF of resume and job description is done to similarity )

-   Experience 

-   Skills set match

## Deployment
> Checkout the Live Application - S
> treamlitapp.com/

## Requirements
- Python 3.7 or higher
- pandas
- numpy
- scikit-learn
- nltk

## Usage
To use the Resume Score Checker, follow the steps below:
> Clone the repository: git clone https://github.com/Mohnish-Sonkusale/Resume_Score_Checker_-Using_NLP_Techniques.git
> Install the required packages: pip install -r requirements.txt 
> Run the application: python app.py<br> Make sure all the codes are working fine.
> Run the Application: streamlit run app.py 
> Open a web browser and navigate to Local URL: http://localhost:8501
> Upload your resume and job description, and the application will provide you with a score and suggestions for improvement.

## Contributing
We welcome contributions to Resume Score Checker! If you have any suggestions or ideas for new features, please open an issue or submit a pull request.

## License
Resume Score Checker is licensed under the MIT License. See the LICENSE file for more details.



