def generate(
    name="Sally Adamson",
    email="sally4359@gmail.com",
    phone="555-986-9855",
    address="Miami, Florida",
    experiences=[
        {
            "position": "Executive Assistant",
            "company": "ACME Inc.",
            "start_date": "August 2017",
            "end_date": "Present",
            "description": "Managed the CEO's daily schedule and travel arrangements, assisted C-suite executives with itineraries, "
            "and onboarded new employees using Bamboo HR.",
        },
        {
            "position": "Secretary",
            "company": "Dover Corporation",
            "start_date": "December 2015",
            "end_date": "July 2017",
            "description": "Managed office supplies inventory using a Microsoft Access database and was in charge of the main corporate phone line.",
        },
    ],
    education=[
        {
            "degree": "Associates degree",
            "field": "Liberal Arts",
            "institution": "Wiggly Community College",
            "graduation_year": "2014",
        }
    ],
    skills=[
        "Microsoft Outlook Tasks",
        "Microsoft Excel",
        "MS PowerPoint",
        "MS Word",
        "fully fluent in English and Spanish",
    ],
    certifications=["Microsoft Office Specialist Certification"],
    awards=["Employee of the Month in 2017", "Employee of the Year in 2022"],
    volunteer_work=["Organized activities for kids at local YMCA on weekends"],
):
    """
    Generates a dynamic resume text based on input parameters.

    Parameters:
    name (str): Full name of the person.
    email (str): Email address.
    phone (str): Phone number.
    address (str): Residential address.
    experiences (list of dicts): List containing job experiences.
    education (list of dicts): List containing educational background.
    skills (list): List of skills.
    certifications (list): List of certifications.
    awards (list): List of awards.
    volunteer_work (list of str): List of volunteer activities.

    Returns:
    str: Formatted resume as a string.
    """

    resume = f"My name is {name}. My email address is {email} and my phone number is {phone}. I live in {address}.\n\n"

    # Adding experience details
    if experiences:
        resume += "Experience:\n"
        for exp in experiences:
            resume += (
                f"I worked as {exp['position']} at {exp['company']} from {exp['start_date']} "
                f"until {exp['end_date']}. {exp['description']}\n"
            )
        resume += "\n"

    # Adding education details
    if education:
        resume += "Education:\n"
        for edu in education:
            resume += (
                f"I hold a {edu['degree']} in {edu['field']} from {edu['institution']} and "
                f"graduated in {edu['graduation_year']}.\n"
            )
        resume += "\n"

    # Adding skills
    if skills:
        resume += "Skills:\n"
        resume += ", ".join(skills) + ".\n\n"

    # Adding certifications
    if certifications:
        resume += "Certifications:\n"
        resume += "\n".join(certifications) + ".\n\n"

    # Adding awards
    if awards:
        resume += "Awards:\n"
        resume += "\n".join(awards) + ".\n\n"

    # Adding volunteer work
    if volunteer_work:
        resume += "Volunteer Work:\n"
        resume += "\n".join(volunteer_work) + ".\n"

    return resume


# Example usage:
