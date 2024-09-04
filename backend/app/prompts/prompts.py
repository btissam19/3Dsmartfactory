
from langchain.prompts import PromptTemplate

extract_resume_info = """
Given the following resume text, extract the following key details and present them as a JSON object. The keys should correspond to the detail categories, and the values should be the extracted information:

1. Name: The full name of the individual.
2. Profile: A brief summary or objective statement from the resume.
3. Contact Information: Phone number, email address, and any other relevant contact details.
4. Education: The degrees obtained, institutions attended, and graduation dates.
5. Work Experience: The job titles, companies, and duration of employment.
6. Projects: A summary of notable projects, including the project name, description, and technologies used.
7. Skills: The technical and soft skills mentioned in the resume.
8. Certifications: The certifications or courses completed, including the certification name and issuing organization.

The response should be formatted  with this schema:
{{
  "Name": str,
  "Profile": str,
  "Contact Information": str,
  "Education": str,
  "Work Experience": str,
  "Projects": str,
  "Skills": str,
  "Certifications": str
}}

Resume Text:
{resume_text}
"""

question_prompt_template = """
Based on the following extracted resume details, generate relevant interview questions:
1. Profile : {Profile}
2. Work Experience: {Work Experience}
3. Projects: {Projects}
4. Skills: {Skills}

Please generate insightful and relevant interview questions related to each section of the resume.
"""

jobs_match_prompt_tamplete="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide
best assistance for improving thr resumes. Assign the percentage Matching based
on Jd and
the missing keywords with high accuracy
Resume Details:
{resume_details}

Job Description:
{job_description}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":"" , "final decision":" "}}
"""

cover_letter_tamplete = """
Please generate a detailed and well-structured cover letter for a job application based on the following information:

1. **Resume Details:**
   {resume_details}

2. **Job Description:**
   {job_description}

The cover letter should:
- Begin with a strong introduction that expresses enthusiasm for the position and the company.
- Clearly outline relevant skills, experiences, and achievements from the resume that align with the job description.
- Highlight specific projects, accomplishments, or qualifications that make the applicant a strong candidate for the role.
- Include a professional and engaging narrative that demonstrates the applicant's suitability for the position.
- Conclude with a compelling closing statement that reaffirms interest in the role and expresses a desire for further discussion.

Ensure that the cover letter is personalized, specific to the job description, and long enough to cover all relevant aspects of the applicant's background and fit for the position.

"""


tips_template = """
Based on the following resume details and job description, please provide actionable tips and tricks to enhance the chances of securing the job.

**Resume Details:**
{resume_details}

**Job Description:**
{job_description}

Please include the following in your advice:

1. **Resume Optimization:** Suggest specific changes or improvements to the resume that would better align it with the job description.

2. **Cover Letter Tips:** Provide guidance on tailoring a cover letter for this particular job. Mention key elements to include or emphasize.

3. **Interview Preparation:** Offer tips on preparing for an interview for this role. This could involve common questions to anticipate, skills to highlight, or strategies for presenting oneself effectively.

4. **Networking Strategies:** Advise on how to leverage networking to increase the chances of landing this job, such as connecting with industry professionals or using social media.

5. **Skills and Experience:** Highlight any additional skills or experiences that could be beneficial for this role, including how to acquire or demonstrate them.

6. **Application Strategy:** Provide recommendations on the overall application strategy, including any steps to follow up or additional materials to submit.

"""

advice_template = """
Please provide detailed and actionable advice based on the following resume details:

**Resume Details:**
{resume_details}

In your advice, please include the following:

1. **Strengths:** Highlight the key strengths and skills evident from the resume. Explain how these strengths could be leveraged in a job search or career development.

2. **Areas for Improvement:** Identify any gaps or areas where the resume could be improved. This might include skills, experience, or formatting suggestions.

3. **Career Development Recommendations:** Offer specific recommendations for enhancing the resume or overall career prospects. This could involve additional skills to acquire, certifications to pursue, or types of experience to gain.

4. **Tailoring for Specific Roles:** Provide advice on how to tailor the resume for specific types of roles or industries, if applicable. This might include emphasizing certain skills or experiences.

5. **General Advice:** Include any other relevant advice for improving the resume or advancing in the chosen career path.

"""


extract_resume_info_prompt = PromptTemplate(
    input_variables=["resume_text"], template=extract_resume_info
)




