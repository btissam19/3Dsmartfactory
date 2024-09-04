import re

def format_extracted_information(output: str) -> dict:
    output_content = f"""{output}"""
    cleaned_content = output_content.strip().strip('```')
    cleaned_content = cleaned_content.replace('\\n', '\n')
    
    headers = [
        "Name", "Profile", "Contact Information", "Education", "Work Experience",
        "Projects", "Skills", "Certifications"
    ]
    
    extracted_info = {}
    for header in headers:
        pattern = rf'"{re.escape(header)}":\s*"([^"]*?)"'
        matches = re.findall(pattern, cleaned_content, re.DOTALL)
        if matches:
            # Join multiple matches if there are any
            extracted_info[header] = ' '.join(matches).replace('\\n', '\n').strip()
        else:
            extracted_info[header] = "Not found"
    
    return extracted_info




def format_generated_questions(output):
    # Initialize the dictionary
    result = {
        "Profile": {},
        "Work Experience": {},
        "Projects": {},
        "Skills": {},
        "Additional Questions": {}
    }

    # Remove extra newline characters and split into sections
    sections = re.split(r'\n\n(?=\*\*[\d\.])', output.strip())
    
    current_section = None
    for section in sections:
        # Check the section header and assign it accordingly
        if section.startswith('**1. Profile:'):
            current_section = 'Profile'
            content = re.sub(r'\*\*[\d\.]\s+', '', section[len('**1. Profile:'):].strip())
            result[current_section] = {
                "Seeking a Summer Internship in Data Science": content.split('\n* ')[1:]
            }
        
        elif section.startswith('**2. Work Experience:'):
            current_section = 'Work Experience'
            work_experience = re.split(r'\n\n\*\*', section[len('**2. Work Experience:'):].strip())
            for exp in work_experience:
                if exp:
                    title, *questions = re.split(r'\n\* ', exp.strip())
                    result[current_section][title.strip()] = questions
        
        elif section.startswith('**3. Projects:'):
            current_section = 'Projects'
            projects = re.split(r'\n\n\*\*', section[len('**3. Projects:'):].strip())
            for proj in projects:
                if proj:
                    title, *questions = re.split(r'\n\* ', proj.strip())
                    result[current_section][title.strip()] = questions
        
        elif section.startswith('**4. Skills:'):
            current_section = 'Skills'
            skills_data = re.sub(r'\*\*[\d\.]\s+', '', section[len('**4. Skills:'):].strip())
            result[current_section] = skills_data.split('\n* ')[1:]
        
        elif section.startswith('**Behavioral Questions:**'):
            current_section = 'Additional Questions'
            behavioral_data = re.sub(r'\*\*Behavioral Questions:\*\*\n', '', section[len('**Behavioral Questions:**'):].strip())
            result[current_section] = behavioral_data.split('\n* ')[1:]

    return result


